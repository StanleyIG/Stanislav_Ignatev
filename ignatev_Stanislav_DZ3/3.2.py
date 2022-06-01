def num_translate(l):
    number = {'one': 'один',
                   'two': 'два'}
    n = {l.title(): number[l] for l in number}
    if l in n:
        return f'"{n[l].capitalize()}"'
    elif l in number:
        return f'"{number[l]}"'
while True:
    l = input()
    print(num_translate(l))