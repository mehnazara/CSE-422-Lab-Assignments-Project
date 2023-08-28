def maximiser(state,a,b,leaf,parent_child):
    global counter 
    v = -10000000000000000000000000000000000
    if state[:4:] == 'leaf':
        counter += 1
        return leaf[state]
    for child in parent_child[state]:
        

        v1 = minimiser(child,a,b,leaf,parent_child)
        if v1 > v:
            v = v1
        if (v1 >= b):
            #print('Pruned Max')
            return v
        























        if v1 > a:
            a = v1
    return v 


def minimiser(state,a,b,leaf,parent_child):
    global counter 
    v = 10000000000000000000000000000000000
    if state[:4:] == 'leaf':
        counter += 1
        return leaf[state]
    for child in parent_child[state]:
        v1 = maximiser(child,a,b,leaf,parent_child)
        if v1 < v:
            v = v1
        if (v1 <= a):
            #print('Pruned Min')
            return v
        if v1 < b:
            b = v1
    return v 
#----------------------------------------------------------------------------------------------    

import random as r

id = input("Provide an id ------>")

attack_hp_range = input('Range-------> ').split(' ')
attack_hp_range = [int(x) for x in attack_hp_range]

hp_of_defender = int(id[-1:-3:-1])

depth = int(id[0]) * 2
branch = int(id[2])

leaf_node_length = branch ** depth 
leaf_nodes = []
for j in range(leaf_node_length):
    leaf_nodes.append(r.randint(attack_hp_range[0],attack_hp_range[1]))

leaf = {}
parent_child = {}    
depth_level = {}

print(f'Depth and Branch ratio is ----> {depth}:{branch}')
print('Terminal States(Leaf Nodes) are ',end='')
for i in range(len(leaf_nodes)):
    if i == (len(leaf_nodes)-1):
        print(leaf_nodes[i], end='.')
    else:
        print(leaf_nodes[i], end=',')
print()

parent_child['og_attacker'] = []
depth_level['og_attacker'] = depth
depth -= 1
attacker_count = 1
completed = []

for defender_count in range(branch):
    parent_child['og_attacker'].append(('defender'+str(defender_count+1)))
    parent_child[('defender'+str(defender_count+1))] = []
    depth_level[('defender'+str(defender_count+1))] = depth

completed.append('og_attacker')
defender_count = branch + 1
indicator = 0
temp = {}
 

 #print(parent_child)

while indicator < len(leaf_nodes):
    for key in parent_child.keys():
        if key not in completed:
            for i in range(branch):
                if key[:8:] == 'defender':
                    if depth_level[key] == 1:
                        parent_child[key].append(('leaf'+str(indicator)))
                        leaf[('leaf'+str(indicator))] = leaf_nodes[indicator]
                        indicator += 1
                    else:
                        parent_child[key].append(('attacker'+str(attacker_count)))
                        temp[('attacker'+str(attacker_count))] = []
                        depth_level[('attacker'+str(attacker_count))] = depth_level[key] - 1
                        attacker_count += 1
                else:
                    if depth_level[key] == 1:
                        parent_child[key].append(('leaf'+str(indicator)))
                        leaf[('leaf'+str(indicator))] = leaf_nodes[indicator]
                        indicator += 1
                    else:
                        parent_child[key].append(('defender'+str(defender_count)))
                        temp[('defender'+str(defender_count))] = []
                        depth_level[('defender'+str(defender_count))] = depth_level[key] - 1
                        defender_count += 1
            completed.append(key)

    for key in temp.keys():
        parent_child[key] = temp[key]
    temp = {}

counter = 0
attack = maximiser('og_attacker',-100000000000000000000000,1000000000000000000000000,leaf,parent_child)

print('Left life(HP) of the defender after maximum damage caused by the attacker is ---->',hp_of_defender-attack)
print('After Alpha-Beta Pruning Leaf Node Comparisons ---->',counter)
















