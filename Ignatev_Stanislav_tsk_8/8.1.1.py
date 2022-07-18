import re


def email_parse(msg):
    email = re.compile(r'(?P<username>[a-zA-Z0-9-\S]+)@(?P<domain>[A-Za-z0-9-]+)(\.[A-Z|a-z]{2,})+')
    try:
        if email.match(msg):
            return email.match(msg).groupdict()
        else:
            raise ValueError(msg)
    except ValueError:
         return f'ValueError: wrong email: {msg}'




print(email_parse('abc123-ABC_123@gmail.ru'))
print(email_parse('abc123-ABC_123gmailru'))

