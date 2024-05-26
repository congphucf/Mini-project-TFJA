import random
import copy

str = input().split()
n=int(str[0])
m=int(str[1])
k=int(str[2])

str = input().split()
a = int(str[0])
b = int(str[1])
c = int(str[2])
d = int(str[3])
e = int(str[4])
f = int(str[5])

s = []
for i in range(n):
    row = list(map(int, input().split()))
    s.append(row)

g = []
for i in range(n):
    row = list(map(int, input().split()))
    g.append(row)

t = list(map(int, input().split()))

teacher_thesis = [[] for x in range(m)]
for thesis, teacher in enumerate(t):
    teacher_thesis[teacher-1].append(thesis)

def check_thesis(hd, thesis, individual):
    if individual[t[thesis]-1+n]==hd:
        return False
    return True

def check_teacher(hd, teacher, hd_teacher):
    count = 0
    for x in hd_teacher[hd]:
        count += len(teacher_thesis[x-n])
    count += len(teacher_thesis[teacher-n])
    if b*(k-1) >= count:
        return True
    else:
        return False


def initalize(size, num_of_pop):
    population = []
    for index in range(num_of_pop):
        individual = [0 for x in range(size)]
        hd_thesis_num = [0 for x in range(k)]
        hd_teacher_num = [0 for x in range(k)]
        hd_thesis = [[] for x in range(k)]
        hd_teacher = [[] for x in range(k)]

        if index == 0:
            var = [x for x in range(n, m+n)]
            var += [x for x in range(n)]
        else:
            x1 =  [x for x in range(n, m+n)]
            random.shuffle(x1)
            x2 = [x for x in range(n)]
            random.shuffle(x2)
            var = x1 + x2
        
        for x in var:
            tmp = 0
            if(x<n):
                for hd in range(k):
                    if hd_thesis_num[hd]<b and check_thesis(hd, x, individual)==True:
                        if hd_thesis_num[hd]<hd_thesis_num[tmp] :
                            tmp = hd
            else:
                for hd in range(k):
                    if hd_teacher_num[hd]<d:
                        if hd_teacher_num[hd]<hd_teacher_num[tmp] and check_teacher(hd, x, hd_teacher)==True :
                            tmp = hd
    
            individual[x]=tmp
            if(x<n):
                hd_thesis[tmp].append(x)
                hd_thesis_num[tmp]+=1
            else:
                hd_teacher[tmp].append(x)
                hd_teacher_num[tmp]+=1

        population.append(individual)
    return population

def fitness(chronosome):
    thesis = chronosome[0:n]
    teacher = chronosome[n:n+m]

    hd_thesis = [[] for x in range(k)]
    hd_teacher = [[] for x in range(k)]

    for x in range(len(thesis)):
        hd_thesis[thesis[x]].append(x)
    for x in range(len(teacher)):
        hd_teacher[teacher[x]].append(x)

    scorce = 0
    for values in hd_thesis:
        if len(values)<a :
            scorce-=1000000*(a-len(values))
        elif len(values)>b :
            scorce-=1000000*(len(values)-b)

    for values in hd_teacher:
        if len(values)<c :
            scorce-=1000000*(c-len(values))
        elif len(values)>d :
            scorce-=1000000*(len(values)-d)

    for values in hd_thesis:
        tmp = 0
        for x in values:
            for y in values:
                tmp+=s[x][y]
        if tmp<e:
            scorce-=1000000*(e-tmp)

        scorce+=tmp/2
    
    for x in range(k):
        tmp=0
        for i in hd_thesis[x]:
            for j in hd_teacher[x]:
                tmp+=g[i][j]
                if t[i]-1==j:
                    scorce-=10000000
        if tmp<f:
            scorce-=1000000*(f-tmp)

        scorce+=tmp
    return scorce

def cross_over(chronosome1, chronosome2):
    son1 = copy.copy(chronosome1)
    son2 = copy.copy(chronosome2)
    
    rmp = random.uniform(0,1)
    if rmp > 0.5:
        p = random.randint(0,len(son1))
        for x in range(p, len(son1)):
            son1[x], son2[x]=son2[x], son1[x]
    else:
        for x in range(len(son1)):
            p = random.uniform(0,1)
            if p > 0.5:
                son1[x], son2[x]=son2[x], son1[x]
    
    return son1, son2

def mutate(chronosome):
    son = copy.copy(chronosome)

    x = random.randint(0,len(son)-1)
    son[x] = random.randint(0,k-1)
    return son

def genetic_algorithm():
    population = initalize(n+m, 100)
    for x in range(200):
        offspring = []
        for y in range(100):
            rmp = random.uniform(0,1)
            if(rmp>0.2):
                k1 = y
                k2 = random.randint(0, len(population)-1)
                son1, son2 = cross_over(copy.copy(population[k1]), copy.copy(population[k2]))
                offspring.append(son1)
                offspring.append(son2)
            else:
                k1 = y
                son = mutate(copy.copy(population[k1]))

                offspring.append(son)
        population += offspring
        population = sorted(population, key=lambda x: -fitness(x))[0:100]
    
    return population[0]

res = genetic_algorithm()
print(n)
thesis = res[0:n]
for i in range(n):
    print(thesis[i]+1, end=" ")
print()
print(m)
teacher = res[n:m+n]
for i in range(m):
    print(teacher[i]+1, end=" ")

