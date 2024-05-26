from ortools.linear_solver import pywraplp

model = pywraplp.Solver.CreateSolver("SAT")


string = input().split()
N=int(string[0])
M=int(string[1])
K=int(string[2])

string = input().split()
a = int(string[0])
b = int(string[1])
c = int(string[2])
d = int(string[3])
e = int(string[4])
f = int(string[5])

s = []
for i in range(N):
    row = list(map(int, input().split()))
    s.append(row)

g = []
for i in range(N):
    row = list(map(int, input().split()))
    g.append(row)

t = list(map(int, input().split()))

infinity = model.infinity()
x = []
for i in range(N):
    row = []
    for j in range(K):
        row.append(model.IntVar(0, 1, "x[" + str(i) + "," + str(j) + "]"))
    x.append(row)

y = []
for i in range(M):
    row = []
    for j in range(K):
        row.append(model.IntVar(0, 1, "y[" + str(i) + "," + str(j) + "]"))
    y.append(row)

z = []
for k in range(K):
    layer = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(model.IntVar(0, 1, "z[" +str(k) +"," + str(i) + "," + str(j) + "]"))
        layer.append(row)
    z.append(layer)

u = []
for k in range(K):
    layer = []
    for i in range(N):
        row = []
        for j in range(M):
            row.append(model.IntVar(0, 1, "u[" +str(k) +"," + str(i) + "," + str(j) + "]"))
        layer.append(row)
    u.append(layer)

for i in range(N):
    model.Add(sum(x[i][j] for j in range(K))==1)

for i in range(M):
    model.Add(sum(y[i][j] for j in range(K))==1)

for k in range(K):
    model.Add(sum(x[i][k] for i in range(N)) >=a)
    model.Add(sum(x[i][k] for i in range(N)) <=b)

    model.Add(sum(y[i][k] for i in range(M)) >=c)
    model.Add(sum(y[i][k] for i in range(M)) <=d)

    model.Add(sum(sum((z[k][i][j])*s[i][j] for i in range(N)) for j in range(N)) >= 2*e)
    model.Add(sum(sum((u[k][i][j])*g[i][j] for i in range(N)) for j in range(M)) >= f)

for  k in range(K):
    for i in range(N):
        for j in range(N):
            model.Add(z[k][i][j]<=x[i][k])
            model.Add(z[k][i][j]<=x[j][k])
            model.Add(x[i][k]+x[j][k]<=1+z[k][i][j])

for  k in range(K):
    for i in range(N):
        for j in range(M):
            model.Add(u[k][i][j]<=x[i][k])
            model.Add(u[k][i][j]<=y[j][k])
            model.Add(x[i][k]+y[j][k]<=1+u[k][i][j])

for i, j in enumerate(t):
    for k in range(K):
        model.Add(x[i][k]+y[j-1][k]<=1) 


model.Maximize(sum(sum(sum(0.5*(z[k][i][j])*s[i][j] for i in range(N)) for j in range (N)) + sum(sum((u[k][i][j])*g[i][j] for i in range(N)) for j in range(M)) for k in range(K)))

status = model.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print(N)
    for i in range(N):
        for k in range(K):
            if x[i][k].solution_value()==1:
                print(k+1, end=" ")
    print()
    print(M)
    for i in range(M):
        for k in range(K):
            if y[i][k].solution_value()==1:
                print(k+1, end=" ")
    print()
    print("Giá trị mục tiêu tối ưu:", model.Objective().Value())
