actions = []

l = [1, 0, 1, 0, 1]

maxval = max(l)

for i in range(len(l)):
    if l[i]==maxval:
        actions.append(i)

