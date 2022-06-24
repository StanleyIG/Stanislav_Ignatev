import os

dir_ = {'my_project':
            [{'settings': [],
            'mainapp': [],
            'adminapp': [],
            'authapp': []}]}

for key, value in dir_.items():
        for i in value:
            for k in i.keys():
                os.makedirs(os.path.join(key,k), exist_ok=True)
