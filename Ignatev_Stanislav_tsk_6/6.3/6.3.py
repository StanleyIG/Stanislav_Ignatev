import json

FILENAME = 'my_list.json'

with open('users.csv', 'r', encoding='utf-8') as file_1:
    with open('hobby.csv', 'r', encoding='utf-8') as file_2:
        users = []
        hobby = []
        users.extend(file_1)
        hobby.extend(file_2)
res = {}
it = iter(hobby)
for i in range(len(users)):
    try:
        res[users[i]] = next(it)
    except StopIteration:
        res[users[i]] = None
jsonStr = json.dumps(res)
with open('my_dict.json', 'w', encoding='utf-8') as file_3:
        file_3.write(jsonStr)
with open('my_dict.json', 'r', encoding='utf-8') as f:
    a = f.read()
    b = json.loads(a)
    print(b)



