from random import randint
import copy
import numpy

N = 8
popSize = 4
queen =[
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
        ]
pop = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ]
pop2 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ]
conf = [0, 0, 0, 0]

def generatePopulation():
        for i in range(0,popSize):
            for j in range(0,N):
                pop[i][j] = randint(0,7)

def fitnessFunc():
    conf = [0]*4
    for i in range(0,4):
        for j in range(0,8):
            for k in range(j+1,8):
                if pop[i][j] == pop[i][k]:
                    conf[i] = conf[i] + 1

    for i in range(0,4):
        for j in range(1, 8):
            for k in range(j-1, -1, -1):
                ans1 = pop[i][j] - j
                ans2 = pop[i][k] - k

                if ans1 == ans2:
                    conf[i] = conf[i] + 1

                ans1 = pop[i][j] + j
                ans2 = pop[i][k] + k
                if ans1 == ans2:
                    conf[i] = conf[i] + 1
    return conf

def selection():
    a = numpy.argsort(conf)
    for i in range(0,3):
        pop2[i] = copy.copy(pop[a[i]])

def crossover():
    #crossover on ending 4 genes
    ee = pop2
    b = copy.copy(pop[1])
    for j in range(0,8):
        if j>=4:
            a = pop2[0][j]
            pop[0][j] = copy.copy(pop2[1][j])
            pop[1][j] = copy.copy(a)
        else:
            pop[0][j] = copy.copy(pop2[0][j])
            pop[1][j] = copy.copy(pop2[1][j])

    for j in range(0,8):
        if j>=4:
            a = pop2[0][j]
            pop[3][j] = copy.copy(b[j])
            pop[2][j] = copy.copy(pop[2][j])
        else:
            pop[2][j] = copy.copy(b[j])
            pop[3][j] = copy.copy(pop2[2][j])

def mutation():
    for i in range(0,4):
        x = randint(0,7)
        y = randint(0,7)
        pop[i][x]= y

    for i in range(0,4):
        arr = [0]*8
        for j in range(0,8):
            k = pop[i][j]
            if arr[k] == 0:
                arr[k] = 1
            else:
                pop[i][j] = -1

        for j in range(0,8):
            if arr[j] != 0:
                continue
            else:
                for k in range(0,8):
                    if pop[i][k] == -1:
                        pop[i][k] = j
                        break
def putting(i):
    for j in range(0,8):
        k = pop[i][j]
        queen[k][j] = 1

for i in range(0,100000):
    generatePopulation()
    print("Iteration: " + str(i))
    print(pop)
    conf = fitnessFunc()
    print(conf)
    flag = 0
    for i in range(0,4):
        if conf[i] == 0:
            flag=1
            x=i
            break
    if flag==1:
        putting(x)
        print("\n\nQueens:")
        for i in range(0,8):
            print(queen[i])
        exit()

    selection()
    crossover()
    mutation()