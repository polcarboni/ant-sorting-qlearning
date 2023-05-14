x = line.split("\n") 

q = threelines.split("\n")
del q[0]
del q[-2:]

print(q)
qtable = ""

for i in range(len(q)):

    hold = (q[i][0])
    patch = int(q[i][2:4])
    memory = int(q[i][5:7])
    density = int(q[i][8:10])

    print(hold, patch, memory, density)

    score = q[i].replace(">","/").split("/")

    pick = int(float(score[1].strip()))
    drop = int(float(score[2].strip()))
    walk = int(float(score[3].strip()))

    print(pick, drop, walk)

    stateactions = f'{hold}{patch}{memory}{density}:{pick}.{drop}.{walk}/'

    qtable += stateactions









"import string"
"q = x.split(""\n"")"
"del q[0]"
"del q[-2:]"
"qtable = ''"
"for i in range(len(q)):"
"    hold = (q[i][0])"
"    patch = int(q[i][2:4])"
"    memory = int(q[i][5:7])"
"    density = int(q[i][8:10])"
"    score = q[i].replace("">"""",""""/"").split(""/"")"

"    pick = int(float(score[1].strip()))"
"    drop = int(float(score[2].strip()))"
"    walk = int(float(score[3].strip()))"

"    stateactions = f'{hold}{patch}{memory}{density}:{pick}.{drop}.{walk}/'"

"    qtable += stateactions"
")"
" show py:runresult 'qtable'"