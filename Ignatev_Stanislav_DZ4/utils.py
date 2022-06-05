import requests.api
import json

def currency_rates(n):
    response = requests.api.get(URL)
    course_dict = json.loads(response.text)
    course_dict[n] = course_dict
    if n in course_dict:
        try:
            result = f" Курс {course_dict['Valute'][n.upper()]['Name']} на {course_dict['Date']} равен {course_dict['Valute'][n.upper()]['Value']}."
            return result
        except KeyError:
            return None

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
n = ''
# пример использвания: a = utils.currency_rates('usd')
# print(a)