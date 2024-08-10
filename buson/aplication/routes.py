from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import timedelta

from login_views.login_user import tela_login
from home.home_views import tela_home, cache
from orders.order_views import tela_pedidos
from registre.registre_views import tela_cadastro
from registre.verify_user.verify_account import tela_verifca
from config.comfig_tools import key_projecto

from cache_routes.cache import cache, config
import logging

app = Flask(__name__)
app.secret_key = key_projecto()
app.permanent_session_lifetime = timedelta(minutes=30)  # Session expiration time configuration

app.register_blueprint(tela_home)
app.register_blueprint(tela_login)
app.register_blueprint(tela_pedidos)
app.register_blueprint(tela_cadastro)
app.register_blueprint(tela_verifca)

# Configurações de cache
app.config.from_mapping(config)
cache.init_app(app) 
# log
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def is_user_logged_in():
    return 'user' in session


@app.route('/ticket/')
def ticket():
    if not is_user_logged_in():
        session['next'] = url_for('ticket')
        flash('You need to be logged in to access this page.')
        return redirect(url_for('login.login'))
    
    return render_template('order.html')







@app.route('/account/')
@cache.cached(timeout=60)
def account():
    if not is_user_logged_in():
      
        return redirect(url_for('login.login'))
    flash('You need to be logged in to access this page.')
    return render_template('account.html')


    
        
@app.route('/logout/')
def logout():
    if 'user' in session:   # Posivel erro

        session.pop('user', None)
        flash('You have been logged out.')
        return redirect(url_for('login.login'))

@app.after_request
def add_cache_headers(response):
    if response.content_type.startswith('image'):
        response.headers['Cache-Control'] = 'public, max-age=31536000'  # 1 year
    return response
if __name__ == '__main__':
    app.run(debug=True, port=5000)

