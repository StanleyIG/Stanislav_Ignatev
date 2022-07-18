import re
def get_logs(file_1):
        for i in file_1:
            #ip = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\w', i) вариант получения ip
            a = i.find('-')
            ip = i[:a]
            get = re.findall('GET', i)
            download = re.findall('\D\Sdownloads\D\S\w\w\w\w\w\w\w\w', i)
            res = [((ip, get, download) for get, download in zip(get, download))]
            result = []
            for i in res:
                result.extend(i)
            yield result

with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    get_log = get_logs(file_1)
    gen_result = []
    for i in get_log:
        gen_result.extend(i)
print(gen_result)




