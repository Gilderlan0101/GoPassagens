from flask import Blueprint, request, session, flash, render_template, url_for, redirect
from account.account import check_user

tela_login = Blueprint('login', __name__, template_folder='templates')

def is_user_logged_in():
    return 'user' in session


@tela_login.route('/login/', methods=['POST', 'GET'])
def login():
    if is_user_logged_in():
        user_data = session['user']
        next_page = session.get('next', url_for('home.home'))
        session.pop('next', None)
        return redirect(next_page)
   

    error = None

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user_data = check_user(email, password)

        if user_data:
            session['user'] = user_data
            session.permanent = True
            next_page = session.get('next', url_for('home.home'))
            session.pop('next', None)
            return redirect(next_page)
        else:
            flash('Invalid email or password')
            

    return render_template("login.html",error=error)

