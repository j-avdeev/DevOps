import os

print("Right now I am here - {}".format(os.getcwd()))

content = os.listdir('.')
print("There are {} elements in this directory".format(len(content)))
for element in content:
    print(element)