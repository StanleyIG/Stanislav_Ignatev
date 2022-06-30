import re

with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    for i in file_1:
        ip = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',i)
        data = re.findall(r'\d{2}\S\w{3}\S\d{4}\S+\d+ \W\d+',i)
        download = re.findall('\D\Sdownload\D\S\w+', i)
        GET = re.findall(r'[A-Z]{3}',i)
        response_code = re.findall(r' \d{1,10}',i)
        pars_logs = [(ip, data,download,GET,response_code[0],response_code[1])
                     for ip, data,download,GET,a,b
                     in zip(ip, data,download,GET,response_code,response_code)]
        for i in pars_logs:
            print(i)








