import re

def spam_ip(file_1):
    res = []
    for i in file_1:
        ip = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\w', i)
        res.extend(ip)
    yield max(set(res), key=res.count)



with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    get_spam = spam_ip(file_1)
    print(next(get_spam))
