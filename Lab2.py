import random as r

def crossover(parent1,parent2):
    temp = parent1[len(parent1)//2::]
    child1 = parent1[:len(parent1)//2:] + parent2[len(parent2)//2::]
    child2 = parent2[:len(parent2)//2:] + temp
    return child1,child2

def mutation(child1,child2):
    position1 = r.randint(0,len(child1)-1)
    position2 = r.randint(0,len(child2)-1)
    temp1 = ''
    temp2 = ''
    for i in range(len(child1)):
        if i != position1:
            temp1 += child1[i]
        else:
            if child1[i] == '1':
                temp1 += '0'
            else:
                temp1 += '1'
    child1 = temp1
    for i in range(len(child2)):
        if i != position2:
            temp2 += child2[i]
        else:
            if child2[i] == '1':
                temp2 += '0'
            else:
                temp2 += '1'
    child2 = temp2
    
    return child1,child2

def fitness(per1,main_dict):
    sum = 100000000000000000000000000000000
    temp = 0
    for i in range(len(per1)):
        if per1[i] == '1':
            if main_dict[i][0] == 'l':
                temp -= main_dict[i][1]
            else:
                temp += main_dict[i][1]
    if temp < sum:
        sum = temp
    if sum == 0:
        return True
    else:
        return False
    

noOfTransaction = int(input("Provide number of transactions--> "))
main_dict = {}
for i in range(noOfTransaction):
    main_dict[i] = input("Transaction--> ").split(" ")
    main_dict[i][1] = int(main_dict[i][1])




population = []
while len(population) != 30:
    temp = ''
    for i in range(noOfTransaction):
        temp += str(r.randint(0,1))
    if (temp != ("0"*noOfTransaction)) and (temp not in population):
        population.append(temp)



counter = 0
goal = False
goalState = '' 
while (counter != 100) and (goal == False):
    
    parent1 = r.randint(0,len(population)-1)
    
    while True:
        parent2 = r.randint(0,len(population)-1)
        if parent2 != parent1:
            break 

    
    parent1 = population[parent1]
    parent2 = population[parent2]

    goal = fitness(parent1,main_dict)
    if goal == True:
        goalState = parent1
        break
    goal = fitness(parent2,main_dict)
    if goal == True:
        goalState = parent2 
        break
    child1,child2 = crossover(parent1,parent2)
    child1,child2 = mutation(child1,child2)
    population.remove(parent1)
    population.remove(parent2)
    if (child1 != ("0"*noOfTransaction)) and (child1 not in population):
        population.append(child1)
    if (child2 != ("0"*noOfTransaction)) and (child2 not in population):
        population.append(child2)
    counter += 1
    

if goal == True:
    print(goalState)
else:
    print(-1)










