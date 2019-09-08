import sys
import os
import time

message_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 
                           'message.txt')
f = open(message_path, 'r', encoding='utf-8')
init_message = f.read()
message = init_message.split('*')

print(message[0])
time.sleep(2)
print(message[1])
time.sleep(1)
print(message[2])
time.sleep(1.5)
print(message[3])
time.sleep(0.5)
print(message[4])
time.sleep(2)
print(message[5])
time.sleep(1)
print(message[6])
time.sleep(1)
print(message[7])
time.sleep(1)

f.close()