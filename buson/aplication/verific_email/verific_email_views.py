import smtplib
from email.message import EmailMessage
import os

def verica_email(email_user, user_name):
    email = 'devdacruz001@gmail.com'
    
    # Caminho do arquivo que contém a senha do aplicativo
    caminho_arquivo = '/home/lan/buson/aplication/account/fake_data/dados.txt'

    print(f"Tentando abrir o arquivo: {caminho_arquivo}")

    # Verifique se o arquivo existe e leia a senha
    if not os.path.isfile(caminho_arquivo):
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return False  # Retorna False se o arquivo não for encontrado

    with open(caminho_arquivo) as file:
        codigo = file.readline().strip()  # Lê a senha e remove espaços em branco

    # Configurando a mensagem
    msg = EmailMessage()
    msg['Subject'] = 'Email de confirmação'
    msg['From'] = email
    msg['To'] = email_user

    # Corpo do email em HTML
    html_content = f"""
    <html>
    <body>
    <p>Olá {user_name},</p>
    <p>Obrigado por se registrar no GoPassgens! Para concluir o processo de registro e ativar sua conta, por favor, confirme seu endereço de email clicando no link abaixo:</p>
    <p><a href="https://www.seusite.com/verify?token=SEU_TOKEN_DE_VERIFICACAO">Confirmar Conta</a></p>
    <p>Se o link acima não funcionar, copie e cole a URL abaixo em seu navegador:</p>
    <p>https://www.seusite.com/verify?token=SEU_TOKEN_DE_VERIFICACAO</p>
    <p>Caso você não tenha se registrado no GoPassgens, por favor, ignore este email.</p>
    <p>Atenciosamente,<br>Equipe GoPassgens</p>
    </body>
    </html>
    """
    msg.add_alternative(html_content, subtype='html')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email, codigo)
            smtp.send_message(msg)
        print("Email enviado com sucesso!")
        return True  # Retorna True se o e-mail for enviado com sucesso
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
        return False  # Retorna False se ocorrer um erro
