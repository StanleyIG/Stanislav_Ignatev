num = [57.8, 46.51, 97, 7, 7.32, 7.05, 95.02]
num_sort = []
num.sort()
print(num)
num.sort(reverse=True)
num_sort.extend(num)
print(num_sort)
five_num = [num_sort[i] for i in range(len(num_sort)) if i < 5]
print(five_num)
for x in num:
    r = x * 100
    c = round(r // 100)
    m = r / 100
    d = round(r % 100)
    if (c < 10 and d < 10):
        c = '0' + str(c)
        d = '0' + str(d)
        print(c, 'руб', d, 'коп')
    elif (c > 10 and d < 10):
        d = '0' + str(d)
        print(c, 'руб', d, 'коп')
    elif (c > 10 and d > 10):
        print(c, 'руб', d, 'коп')
    elif c < 10 and d > 10:
        c = '0' + str(c)
        print(c, 'руб', d, 'коп')
