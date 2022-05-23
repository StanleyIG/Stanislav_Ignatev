import time

while True:
        duration = int(input('введите число '))
        n = duration
        if n < 60:
                time_format = time.strftime('%S сек', time.gmtime(n))
                print(time_format)
        elif n == 60:
                time_format = time.strftime('%M мин', time.gmtime(n))
                print(time_format)
        elif 60 < n <= 3600:
                time_format = time.strftime('%H час:%M мин:%S сек', time.gmtime(n))
                print(time_format)
        elif 3600 < n <= 86400:
            time_format = time.strftime('%d день:%H час:%M мин:%S сек', time.gmtime(n))
            print(time_format)
        else:
            print('введите <= 86400')



