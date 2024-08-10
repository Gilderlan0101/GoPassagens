from flask import redirect, request, flash, url_for, session, render_template, Blueprint
from account.account import check_user, create_user
from verific_email.verific_email_views import verica_email

tela_cadastro = Blueprint('register', __name__, template_folder='templates')

@tela_cadastro.route('/register/', methods=['POST', 'GET'])
def register():
    message = None
    email_error = None
   
  

    if 'usuario' not in session:
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            password = request.form['password']

            
            if check_user(email, password):
                email_error = f'{email} is already in use'
                print('senha e email validas')
            else:
                success, _ = create_user(name, email, phone, password)
                comfimacao_email = verica_email(email, name)
                if success and comfimacao_email:
                    print('redirecionando user')
                    flash(f'{name}, welcome!')
                    session['user'] = {'name': name, 'email': email}  # Log the user in after registration
                   
                    return redirect(url_for('verify.verify'))
                else:
                    message = 'Error trying to register. Please try again.'
    
    return render_template('register.html', email_error=email_error, message=message)
