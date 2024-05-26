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

result = [-1 for x in range(m+n)]
hd_thesis_num = [0 for x in range(k)]
hd_teacher_num = [0 for x in range(k)]
hd_thesis = [[] for x in range(k)]
hd_teacher = [[] for x in range(k)]

def caculate_thesis(hd, thesis):
    res = 0
    for th in hd_thesis[hd]:
        res+=s[thesis][th]
    for teacher in hd_teacher[hd]:
        res+=g[thesis][teacher-n]
    return res


def check_thesis(hd, thesis):
    if result[t[thesis]-1+n]==hd:
        return False
    return True

def check_teacher(hd, teacher):
    count = 0
    for x in hd_teacher[hd]:
        count += len(teacher_thesis[x-n])
    count += len(teacher_thesis[teacher-n])
    if b*(k-1) >= count:
        return True
    else:
        return False
    
var = [x for x in range(n, m+n)]
var += [x for x in range(n)]

for x in var:
    tmp = -1
    if(x<n):
        for hd in range(k):
            if hd_thesis_num[hd]<b and check_thesis(hd, x)==True:
                if tmp==-1 or hd_thesis_num[hd]<hd_thesis_num[tmp] :
                    tmp = hd
        # if hd_thesis_num[tmp]>=a:
        #     for hd in range(k):
        #         if check(hd, x)==True and caculate_thesis(hd, x) > caculate_thesis(tmp, x):
        #             tmp = hd
    else:
        for hd in range(k):
            if hd_teacher_num[hd]<d:
                if (tmp==-1 or hd_teacher_num[hd]<hd_teacher_num[tmp]) and check_teacher(hd, x)==True :
                    tmp = hd
    result[x]=tmp
    if(x<n):
        hd_thesis[tmp].append(x)
        hd_thesis_num[tmp]+=1
    else:
        hd_teacher[tmp].append(x)
        hd_teacher_num[tmp]+=1

print(n)
thesis = result[0:n]
for i in range(n):
    print(thesis[i]+1, end=" ")
print()
print(m)
teacher = result[n:m+n]
for i in range(m):
    print(teacher[i]+1, end=" ")

