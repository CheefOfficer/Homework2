def send_email(message, recipient,*,sender = "university.help@gmail.com"):
    markers = ('.ru', '.com', '.net')
    if ('@' not in recipient
            or '@' not in sender
            or not recipient.endswith(markers)
            or not sender.endswith(markers)):
        print("Невозможно отправить письмо с адреса" , sender,  "на адрес",  recipient)


    elif str(sender) == str(recipient):
        print("Нельзя отправить письмо самому себе!")
    elif str(sender) == 'university.help@gmail.com':
        print("Письмо успешно отправлено с адреса" , sender,  "на адрес",  recipient)
    else:
         print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, 'на адрес', recipient, '.')


#______________________________________________________________________________________________________
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher.mail.ru', sender='urban.teacher,mail')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.su', sender='urban.teacher@mail.pu')


