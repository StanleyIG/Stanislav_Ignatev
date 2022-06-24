import os
from collections import defaultdict
import django

root_dir = django.__path__[0]
size_dict = {}
res = []
for root, dirs, files in os.walk(root_dir):
    for file in files:
        size = os.stat(os.path.join(root, file)).st_size
        if size > 0 and size <= 100000:
            res.append(size)
size_dict.setdefault(100, len([i for i in res if i > 0 and i <= 100 and i % 10 == 0]))
size_dict.setdefault(1000, len([i for i in res if i > 100 and i <= 1000 and i % 10 == 0]))
size_dict.setdefault(10000, len([i for i in res if i > 1000 and i <= 10000 and i % 10 == 0]))
size_dict.setdefault(100000, len([i for i in res if i > 10000 and i <= 100000 and i % 10 == 0]))
print(size_dict)

