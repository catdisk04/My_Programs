#!/usr/bin/python3
import random, math, csv, matplotlib.pyplot as plt

R = 100 #radius of circle
L = 250 #domain side length
N = 100 #num_steps
S = 10 #step length
A = 3 #number of ants


figure, axes = plt.subplots()
circ = plt.Circle(( 0 , 0 ), R , fill=False )
axes.add_artist(circ)
colors=['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

axes.set_aspect( 1 )
plt.xlim([-L/2, L/2])
plt.ylim([-L/2, L/2])
plt.title('Drunken ants')

operators=[
[S, 0], 
[-S, 0], 
[0, S], 
[0, -S ]
]

def add_arr(arr1, arr2):
    if not len(arr1) == len(arr2):
        return 0
    res = []
    for i in range(len(arr1)):
    	res.append(arr1[i]+arr2[i])
    return res


# print(x, y)
def get_path(color):
    global plt
    
    #init pos
    theta= int(random.random()*360)
    x = R * math.cos(math.radians(theta))
    y = R * math.sin(math.radians(theta))
    res = [[round(x, 3), round(y, 3)]] #rounding for aesthetics and size of csv file
    
    plt.scatter(res[0][0], res[0][1], color=color)
    
    for i in range(N-1):
        p = add_arr(res[i], random.choice(operators)) #p is the new point in the path
        crossed = False
        
        for j in range(2): #looping over the x and y axis
            if p[j] > L/2:
                plt.plot([res[i][0], p[0]], [res[i][1], p[1]], color = color) #for continiuity of plots
                p[j] -= L
                plt.plot([p[0], p[0]-1], [p[1], p[1]-1]) #for continiuity of plots
                crossed = True

            elif p[j] < -L/2:
                plt.plot([res[i][0], p[0]], [res[i][1], p[1]], color = color) #for continiuity of plots
                p[j] += L
                plt.plot([p[0], p[0]+1], [p[1], p[1]+1]) #for continiuity of plots
                crossed = True
        
        if not crossed:
            # print(res[i], p)
            plt.plot([res[i][0], p[0]], [res[i][1], p[1]], color = color)
            # plt.plot([res[i][0], res[i-1][0]], [res[i][1], res[i-1][1]], color = 'r')
        else:
            # print(p)
            pass
            
        res.append(p)

    return res
        
l=[get_path(colors[i%len(colors)]) for i in range(A)]
file_names=[f"path{i}.csv" for i in range(1, A+1)]
for i in range(len(l)):
    with open(file_names[i], 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        for line in l[i]:
            writer.writerow(line)





