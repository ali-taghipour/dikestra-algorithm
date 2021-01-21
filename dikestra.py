vertexs = []
directions = []
cost = ""
v = ""
v_selected = []
next = input("If you want to go to next step please enter next in which step:\n")
if next == "next":
    while True:
        vName = input("Please enter vertex name or enter next:\n")
        if vName == "next":
            break
        vertexs.append(vName)
    if len(vertexs) < 2:
        print("You must enter two vertexts!!!")
        exit()
    for i in vertexs:
        for j in vertexs:
            if i != j and ((j,i,-1) not in directions):
                directions.append((i,j,-1))
    print("Please enter directions costs between two vertexs and if there isn't direct path enter -1")
    for i in directions:
        if directions.index(i) <= len(directions) - 1:
            cost = ""
        while type(cost) != type(1):
            cost = input("Please enter direction cost between {0} and {1}:\n".format(i[0],i[1]))
            try:
                cost = int(cost)
                directions[directions.index(i)] = (i[0],i[1],cost)
            except:
                print("Enter number!!!")

    while v not in vertexs:
        v = input("Please enter the vertex you want to see the nearest directions up to it:\n")
    v_selected.append(v)

    v_directions = []
    for i in directions:
        if v in i[0] or v in i[1]:
            v_directions.append(i)

    v2 = v
    vs = ""
    total = 0
    while len(directions) > 0:
        minimum = -1
        for i in directions:
            if (v2 in i[0] or v2 in i[1]) and len(v_selected) > 1:
                for j in i:
                    if j != v2 and type(j) != type(1):
                        for k in v_directions:
                            if i[2] != -1:
                                if (j == k[0] or j == k[1]) and (i[2] + total < k[2] or k[2] == -1):
                                    a = (v2,)
                                    print(i[2])
                                    if(len(v_directions[v_directions.index(k)]) > 3):
                                        a = v_directions[v_directions.index(k)][3:] + a
                                    v_directions[v_directions.index(k)] = (k[0],k[1],total + i[2]) + a
            
            if (v2 in i[0] or v2 in i[1]) and i[2] != -1:
                if minimum == -1:
                    minimum = i[2]
                    for j in i:
                        if j != v2 and type(j) != type(1):
                            vs = j
                elif i[2] < minimum:
                    minimum = i[2]    
                    for j in i:
                        if j != v2 and type(j) != type(1):
                            vs = j  
        if(minimum != -1):
            dirs = []
            for k in directions:
                if (k[0] == v2 or k[1] == v2) == False:
                    dirs.append(k)
            directions = []
            directions = dirs[:]
            v2 = vs
            v_selected.append(vs)
            total = total + minimum
        else:
            break
        
for i in v_directions:
    if(len(i) > 3):
        print("Direction cost between {0} and {1} is {2}".format(i[0],i[1],i[2]),end=" ")
        if len(i) < 5:
            print("and the vertex between them is {0}".format(i[3]))
        else:
            print("and the vertexs between them are",end=" ")
            for j in i:
                if i.index(j) > 2:
                    print(j,end=" ")
            print("respectively")
    else:
        print("Direction cost between {0} and {1} is {2}".format(i[0],i[1],i[2]))