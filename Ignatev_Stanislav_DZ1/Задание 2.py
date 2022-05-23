for number in range(1, 1000, 2):
    result = number ** 3
    new_number = []
    new_number.append(result)
    print(new_number)
    for i in new_number:
        num = sum(map(int,str(i)))
        if num%7==0:
            print(num)
        for i in new_number:
            second_num = num + 17
            if second_num % 7 == 0:
                print(second_num)





