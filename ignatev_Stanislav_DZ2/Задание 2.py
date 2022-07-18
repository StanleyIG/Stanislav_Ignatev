new_name = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = []
for i in range(len(new_name)):
    if new_name[i].startswith('+'):
        new_name[i] = new_name[i].zfill(3)
    elif new_name[i].isdigit():
        new_name[i] = new_name[i].zfill(2)
result.extend(new_name)
i = 0
while i < len(result):
    if result[i].isdigit() or result[i].startswith('+') and result[i][1:].isdigit():
        result.insert(i, '"')
        result.insert(i + 2, '"')
        i += 2
    i += 1
print(result)
print(' '.join(result))