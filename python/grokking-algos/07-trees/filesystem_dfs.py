from os import listdir
from os.path import isfile, join
from collections import deque

def printnames(start_dir):
    print(f"Searching inside: {start_dir}")  
    search_queue = deque()
    search_queue.append(start_dir)
    while search_queue:
        current_dir = search_queue.popleft()
        for file in sorted(listdir(current_dir)):
            fullpath = join(current_dir, file)
            if isfile(fullpath):
                print(f"Now searching inside: {current_dir}")
                print(file)
            else:
                search_queue.append(fullpath)


print(printnames('..'))
