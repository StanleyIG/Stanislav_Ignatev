import os
from collections import defaultdict
import django

root_dir = django.__path__[0]
size_dict = defaultdict(int)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        size = 10**len(str(os.stat(os.path.join(root, file)).st_size))
        size_dict[size]+=1

for size, files in sorted(size_dict.items()):
    print(f'{size}: {files}')