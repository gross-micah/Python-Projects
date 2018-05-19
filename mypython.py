# necessary headers
import string
import random
import os

#get directory
path_to_script = os.path.dirname(os.path.abspath(__file__))

#build first file
file_name = os.path.join(path_to_script, "hw1.txt")
f = open(file_name, 'w+')
t = ""
for i in range(0, 10):
    t += random.choice(string.ascii_lowercase)
t += '\n'
f.write(t)
f.close()
#build second file
file_name = os.path.join(path_to_script, "hw2.txt")
g = open(file_name, 'w+')
t = ""
for i in range(0, 10):
    t += random.choice(string.ascii_lowercase)
t += '\n'
g.write(t)
g.close()
#build third file
file_name = os.path.join(path_to_script, "hw3.txt")
h = open(file_name, 'w+')
t = ""
for i in range(0, 10):
    t += random.choice(string.ascii_lowercase)
t += '\n'
h.write(t)
h.close()
#display the 3 files
with open("hw1.txt", 'r') as f:
    print(f.read())
f.close()
with open("hw2.txt", 'r') as f:
    print(f.read())
f.close()
with open("hw3.txt", 'r') as f:
    print(f.read())
f.close()

num1 = random.randrange(1, 43)
num2 = random.randrange(1, 43)
print(num1)
print(num2)
print(num1 * num2)
