odd_nums = (i for i in range(15) if i % 2 != 0)
print(next(odd_nums))
print(next(odd_nums))
for i in odd_nums:
    print(i)
