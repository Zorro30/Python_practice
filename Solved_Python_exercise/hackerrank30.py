def differentTeams(skills):

    count = {'p':0,'c':0,'m':0,'b':0,'z':0}
    for i in skills:
        if i == 'p':
            count['p']+=1
        if i=='c':
            count['c']+=1
        if i=='m':
            count['m']+=1
        if i=='b':
            count['b']+=1
        if i=='z':
            count['z']+=1
    res = min(count.keys(), key=(lambda k: count[k]))
    print(count[res])

differentTeams("pcmpcmbbbzz")