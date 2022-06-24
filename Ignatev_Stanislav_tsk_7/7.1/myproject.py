import os

def my_project(*kwargs):
    root = 'my_project'
    folders = [*kwargs]
    for folder in folders:
            os.makedirs(os.path.join(root, folder), exist_ok=True)

if __name__ == '__main__':
    print(my_project(''))
