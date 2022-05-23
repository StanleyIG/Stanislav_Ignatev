while True:
        number = int(input('введите N процентов' ))
        n = number
        if n == 1 or (n > 20 and (n % 10) == 1) and (n % 100) != 11:
                print(n, 'процент')
        elif (n > 1 and n < 5) or (n > 20 and (n % 10) > 1 and (n % 10) < 5):
                print(n, 'процента')
        elif n == 0 or (n > 4 and n < 20) or (n % 10) == 0 or (n % 10) >= 5 or (n % 100) >= 10:
                print(n, 'процентов')




