#A* Search
main_file = open("C:\\Users\\LENOVO\\OneDrive\\Desktop\\422\\Input_file.txt")
h_n = {}
f_n = {}
parent_child = {}
path = []
queue = []
pathcost = 0
for line in main_file:
    temp_arr = line.split(' ')
    temp_arr[-1] = temp_arr[-1].strip('\n')
    parent_child[temp_arr[0]] = []
    for i in range(2,len(temp_arr)):
        if (i % 2 == 1):
            temp_arr[i] = int(temp_arr[i])
            parent_child[temp_arr[0]].append(temp_arr[i])
        else:
            if temp_arr[i] != '':
                parent_child[temp_arr[0]].append(temp_arr[i])
    
    h_n[temp_arr[0]] = int(temp_arr[1])


root = input('Provide a starting city --> ')
f_n[root] = h_n[root]
queue.append(root)
current_node = ''
goal_flag = False

while (queue != []) and (goal_flag == False):
    minValue = 100000000000000000000000000000000000000000
    for item in queue:  #Imitating a priority queue
        if f_n[item] < minValue:
            minValue = f_n[item]
            current_node = item
        elif (f_n[item] == minValue) and (item != 'Bucharest'): #to expand other nodes first
            minValue = f_n[item]
            current_node = item
    queue.remove(current_node) #pop
    path.append(current_node)
    val = 0
    if len(path) != 1:
        counter = len(path)-1
        comparator = counter-1

    #--------------------------------------------------------------------------------------
        while (counter != 0) and (comparator != -1):
            if path[counter] in parent_child[path[comparator]]:
                if comparator == 0:
                    for idx in range(0,len(parent_child[path[comparator]])-1):
                        if parent_child[path[comparator]][idx] == path[counter]:
                            val += parent_child[path[comparator]][idx+1]
                            break
                    counter = comparator
                    comparator -= 1
                else:
                    if (path[counter] in parent_child[path[comparator-1]]) and (h_n[path[comparator-1]] < h_n[path[comparator]] ):
                        for idx in range(0,len(parent_child[path[comparator-1]])-1):
                            if parent_child[path[comparator-1]][idx] == path[counter]:
                                val += parent_child[path[comparator-1]][idx+1]
                                break
                        counter = comparator -1
                        comparator -= 2
                    else:
                        for idx in range(0,len(parent_child[path[comparator]])-1):
                            if parent_child[path[comparator]][idx] == path[counter]:
                                val += parent_child[path[comparator]][idx+1]
                                break
                        counter = comparator
                        comparator -= 1

                    
            else:
                comparator -= 1
    for i in range(0,len(parent_child[current_node]),2):
        if parent_child[current_node][i] not in f_n.keys():
            f_n[parent_child[current_node][i]] = val + h_n[parent_child[current_node][i]] + parent_child[current_node][i+1]
            queue.append(parent_child[current_node][i])
        else:
            if (val + h_n[parent_child[current_node][i]] + parent_child[current_node][i+1]) < f_n[parent_child[current_node][i]]:
                f_n[parent_child[current_node][i]] = val + h_n[parent_child[current_node][i]] + parent_child[current_node][i+1]
                queue.append(parent_child[current_node][i])

    if current_node == 'Bucharest':
        goal_flag = True

if goal_flag == True:
    counter = len(path)-1
    comparator = counter-1
    remove = []

#--------------------------------------------------------------------------------------
    while (counter != 0) and (comparator != -1):
        if path[counter] in parent_child[path[comparator]]:
            if comparator == 0:
                counter = comparator
                comparator -= 1
            else:
                if (path[counter] in parent_child[path[comparator-1]]) and (h_n[path[comparator-1]] < h_n[path[comparator]] ):
                    remove.append(path[comparator])
                    counter = comparator -1
                    comparator -= 2
                else:
                    counter = comparator
                    comparator -= 1

                
        else:
            remove.append(path[comparator])
            comparator -= 1

#-----------------------------------------------------------------------------------------------

    for item in remove:
        path.remove(item)

#------------------------------------------------------------------------------------------------

    for i in range(0,len(path)-1):
        for j in range(0,len(parent_child[path[i]]),2):
            if parent_child[path[i]][j] == path[i+1]:
                pathcost += parent_child[path[i]][j+1]

#------------------------------------------------------------------------------------------------

    output = ''
    for idx in range(0,len(path)-1):
        output += path[idx]
        output += ' -> '
    output += path[-1]
    print('Path: '+output)
    print('Total distance: '+str(pathcost)+'km')

else:
    print('NO PATH FOUND')

#----------------------------------------------------------------------------------------------




