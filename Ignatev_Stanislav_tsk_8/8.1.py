import re


def email_parse(msg):
    parse = re.findall(r'[\w]+@[\w]+(\.[\w]+)+', msg.lower())
    try:
        if parse:
            result = re.findall(r'[\w]+', msg.lower())
            username = result[0]
            domain = result[1]
            email_dict = {}
            email_dict.setdefault('username', username)
            email_dict.setdefault('domain', domain)
            return email_dict
        else:
            if not parse:
                raise ValueError
    except ValueError:
        return f'ValueError: wrong email: {msg}'


print(email_parse('sasd76_sjdh_876ru'))
print(email_parse('sasd76_s@jdh_876.ru'))
