import re


def email_parse(e_mail):
    re_email = re.compile(r'[^@]+@[^@]+\.[^@]+', re.IGNORECASE)
    if not re_email.match(e_mail):
        print(f'wrong email: {e_mail}')
        raise ValueError
    result = {'username': re.search(r'[^@]+', e_mail)[0], 'domain': re.search(r'[^@]+$', e_mail)[0]}
    return result


for i in ['postmaster@mail.ru', 'postm@ster@mail.ru', 'postmaster@mailru']:
    try:
        print(email_parse(i))
    except ValueError as ve:
        print(ve)
