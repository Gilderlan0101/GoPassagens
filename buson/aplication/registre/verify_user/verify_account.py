from flask import render_template, flash, Blueprint
from user_on.comfig_user import is_user_logged_in

tela_verifca = Blueprint('verify', __name__,  template_folder='templates')


@tela_verifca.route('/verify/')
def verify():
    if is_user_logged_in():
        flash("Registration successful! You will be redirected to the homepage.")
    
    
    return render_template('redirect.html')