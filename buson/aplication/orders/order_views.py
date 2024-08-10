from flask import render_template, redirect,  flash, request, url_for, Blueprint
from user_on.comfig_user import is_user_logged_in
from check_order.orders import Order,validar_cpf

tela_pedidos = Blueprint('order',__name__, template_folder='templates')


@tela_pedidos.route('/order/', methods=['POST', 'GET'])
def order():
    if is_user_logged_in():
        errors = {}
        if request.method == 'POST':
            try:
                # Verifica se o campo CPF foi enviado
                cpf = request.form.get('cpf')
                if not cpf:
                    flash('CPF is required.')
                    return redirect(url_for('order'))
                
                code_supplied = request.form.get('number')
                if not code_supplied:
                    errors['order'] = "Please enter a valid number."
                    return render_template('order.html', errors=errors, generated_code=None)

                try:
                    code_supplied = int(code_supplied)
                except ValueError:
                    errors['order'] = "Please enter a valid number."
                    return render_template('order.html', errors=errors, generated_code=None)

                order = Order(order=code_supplied)
                valid, generated_code = order.verify_code(code_supplied)

                # Validate the order
                valida_cpf = validar_cpf(cpf)
                errors = order.validate()

                if not errors:
                    if valid:
                        if valida_cpf:
                            return f'Valid code! The generated code was {generated_code}. CPF {cpf} is valid.'
                        else:
                            flash('CPF is invalid.')
                            return redirect(url_for('order.order'))
                    else:
                        return f'Invalid code. The generated code was {generated_code}.'
                else:
                    return render_template('order.html', errors=errors, generated_code=None)
            
            except ValueError:
                errors['order'] = "Please enter a valid number."
                return render_template('order.html', errors=errors, generated_code=None)

        else:  # GET method
            order = Order(order=None)  # Generated code does not depend on user input
            generated_code = order.generate_code()
            return render_template('order.html', generated_code=generated_code, errors=errors)
    
    else:
        flash('You need to be logged in to check your orders.')
        return redirect(url_for('login.login'))