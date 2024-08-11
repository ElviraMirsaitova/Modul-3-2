def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    if str(recipient) == str(sender):
        print(f'Нельзя отправить письмо самому себе!')
        return


    if str(sender) == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        return


    domains = [".com", ".ru", ".net"]
    result = True
    if(not any(domain in recipient for domain in domains)
            or not any(domain in sender for domain in domains)
            or not '@' in recipient or not '@' in sender):
            result = False
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    else:
        result = False
        print(f'"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com', sender = 'elvira@gmail.com')     #хорошо
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com', sender = 'elviragmail.com')      #сломано
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.ru', sender = 'elvira@gmail.net')      #хорошо
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.r', sender = 'elvira@gmail.n')         #сломано
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.ru', sender = 'elvira@gmail.net')      #хорошо
send_email('Письмо самому себе', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')               #на себя
send_email('Отправили письмо в в Urban', 'urban.teacher@mail.ru', sender='university.help@gmail.com')   #в Урбан по умолчанию