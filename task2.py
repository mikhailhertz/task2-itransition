import sha3
import os

path = os.path.join(os.getcwd(), 'task2')
s = []
for filename in os.listdir(path):
   with open(os.path.join(path, filename), 'rb') as f:
       s.append(sha3.sha3_256(f.read()).hexdigest())
s = sorted(s)
print(s)
string = ''.join(s)
string += "mikhailhertz@gmail.com"
print(sha3.sha3_256(str.encode(string)).hexdigest())
