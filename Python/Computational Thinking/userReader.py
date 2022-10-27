import os

f = open('50k-users.txt', 'r')
users = []
for line in f:
    users.append(line)

for user in users:
    if user[2] == 'x':
        if user[15] == 'S':
            if user[3].isnumeric():
                if int(user[3]) >= 2 and int(user[3]) <=6:
                    if 'Z' in user:
                        print(user)