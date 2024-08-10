from datetime import datetime


def greetings():
    horas = datetime.now()
    am_pm = datetime.now().strftime('%p')
    if am_pm == 'PM' and horas.hour == 12  or horas.hour == 13 or horas.hour == 14 or horas.hour == 15 or horas.hour == 16 or horas.hour == 17 :
      msg = 'Boa tarde'
      return msg

    elif am_pm == 'PM' and horas.hour == 18 or horas.hour == 19  or horas.hour == 20 or horas.hour == 21 or horas.hour == 22 or horas.hour == 23 :
       msg = 'Boa noite'
       return msg
    
    else:
      msg = 'Bom dia'
      return msg