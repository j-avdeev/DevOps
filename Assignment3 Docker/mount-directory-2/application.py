import os
import sys

target_dir = sys.argv[1]

print("Observe directory - {}".format(target_dir))

content = os.listdir(target_dir)
print("There are {} elements in this directory".format (len(content)))
for element in content:
    print(element)