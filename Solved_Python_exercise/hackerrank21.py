def entityExpansion(l, entities):
    # count = 0
    # non_count = 0
    # der = False
    # for i in entities:
    #     if ';' in i:
    #         count += (i.count(';'))+1
    #         der = True
    #     else:
    #         non_count +=1
    # if der:        
    #     if (count+1+non_count) < l:
    #         print( "1 {}".format(count+non_count))
    #     else:
    #         print( "0 {}".format(count+non_count))
    # else:
    #     if (count+1+non_count) < l:
    #         print( "1 {}".format(non_count))
    #     else:
    #         print( "0 {}".format(non_count))
    count = 0
    non_count = 0
    der = False
    den = False
    for i in entities:
        if i.split(' ')[1] == 'a0':
            den = True
        if ';' in i:
            count += (i.count(';'))+1
            der = True
        else:
            non_count +=1
    if der: 
        if den:       
            if (count+1+non_count) < l:
                print( "1 {}".format(count+1+non_count))
            else:
                print( "0 {}".format(count+1+non_count))
        else:
            if (count+1+non_count) < l:
                print( "1 {}".format(count+non_count))
            else:
                print( "0 {}".format(count+non_count))
    else:
        if (count+1+non_count) < l:
            print( "1 {}".format(non_count))
        else:
            print( "0 {}".format(non_count))
    


if __name__ == '__main__':
    l = int(input().strip())

    entities_count = int(input().strip())

    entities = []

    for _ in range(entities_count):
        entities_item = input()
        entities.append(entities_item)

    (entityExpansion(l, entities))



