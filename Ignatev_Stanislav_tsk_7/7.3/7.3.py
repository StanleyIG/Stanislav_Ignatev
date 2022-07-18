import os
import pathlib
import shutil

root = 'my_project'
folders = ['settings', 'mainapp', 'authapp', 'templates']
files = ['templates', 'mainapp', 'authapp']
files2 = ['templates', 'authapp']
for folder in folders:
    os.makedirs(os.path.join(root, folder), exist_ok=True)
    os.makedirs(os.path.join(root, *folders[1:2], *files[0:2]), exist_ok=True)
    os.makedirs(os.path.join(root, *folders[2:3], *files2[0:2]), exist_ok=True)
    #for file in files[1:]:
        #os.makedirs(os.path.join(root, *folders[3:], file), exist_ok=True)


def get_file(add_file, path):
    for i in add_file:
        filepath = os.path.join(path, i)
        with open(filepath, 'w') as f:
            f.write(i)

# add_file = ['__init__.py', 'models.py', 'views.py']
# get_file(add_file,'C:/Users/Админ/PycharmProjects/pythonProject2/lesson_7/my_project/templates/authapp')
import os
import shutil

path = 'my_project'

for root, dirs, files in os.walk(path):
    for name in dirs:
        if name.lower().startswith('templates'):
            shutil.copytree(os.path.join(root, name), os.path.join(path, name), dirs_exist_ok=True)




