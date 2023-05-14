import string
import random
#State: hold patch memory density
#Actions: Pick Drop Walk

found = 0
maxval = 0

#input da netlogo
hold = 0
patch = 0
memory = 0
density = 0

curstate=f'{hold}{patch}{memory}{density}'

line = "1100:-1.-1.1/1000:0.0.1/0102:0.0.0/0000:0.0.0/1011:-1.0.1/0101:1.0.-1/1110:-1.0.1/1121:-1.0.0/"
table = line.split("/")

del table[-1]

for i in range(len(table)):
    s = (table[i][0:4])
    
    if curstate == s:
        actions = table[i].split(':')[1]
        actions = actions.split('.')
        
        maxval = max(actions)
        
        pick = actions[0]
        drop = actions[1]
        walk = actions[2]



        

        

if found == 0:
    action = random.randrange(0,3)

    
#print(action)


"table = qtable.split('/')"
"del table[-1]"
"for i in range(len(table)):"
"s = (table[i][0:4])"

"    if curstate == s:"
"        pick = table[i][5]"
"        drop = table[i][7]"
"        walk = table[i][9]"
"        found = 1"

"        l = [pick, drop, walk]"
"        action = l.index(max(l))"

"if found == 0:"
"    action = random.randrange(0,3)"