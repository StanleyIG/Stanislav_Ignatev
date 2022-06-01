def num_translate(l):                     
    number_dict = {'one': 'один',
                   'two': 'два'}
    if l in number_dict:
            return(number_dict[l])

while True:
    l = input()
    print(num_translate(l))