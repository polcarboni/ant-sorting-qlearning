import string
import random
#State: hold patch memory density
#Actions: Pick Drop Walk

found = 0


#input da netlogo
hold = 1
patch = 0
memory = 0
density = 1

curstate=f'{hold}{patch}{memory}{density}'

line = "0102:1.0.0/0000:0.0.0/1001:3.0.1/"
table = line.split("/")

del table[-1]

for i in range(len(table)):
    s = (table[i][0:4])
    
    if curstate == s:

        pick = table[i][5]
        drop = table[i][7]
        walk = table[i][9]
        found = 1
        
        l = [pick, drop, walk]
        action = l.index(max(l))

if found == 0:
    action = random.randrange(0,3)
    pass

    
print(action)


