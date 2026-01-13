Web VPython 3.2

edge1 = box(pos = vec(-100, 0 ,0), color = color.red, length = 10, height = 10, width = 10)
edge2 = box(pos = vec(100, 0, 0), color = color.red, length = 10, height = 10, width = 10)

numPlanks = float(input("Enter Number of Planks"))

#constants
dt = 0.1 
t = 1 
g = vec(0, -9.81, 0)
mass = 1000
k = 200
b = 1

nugs = []
fries = []


for i in range(-100, 100, 200/numPlanks):
    nugs.append(sphere(pos = vec(i+100/numPlanks, 0, 0), color = color.orange, radius = 50/numPlanks, eqPos = vec(i+100/numPlanks,0,0)))
    fries.append(box(pos = vector(i+100/numPlanks, 0, 0), color = color.yellow, length = 200/numPlanks, eqPos = vec(i+100/numPlanks,0,0)))
    
for nug in nugs:
    nug.velocity = vec(0,0,0)

for fry in fries:
    fry.velocity = vec(0,0,0)
    
def springAcc(nug, X):
    return (-k * (nug.pos - X))/mass

def nugacc(v, t):
    return ((mass*g - b*v)/mass)
    
def posi(v, t):
    return v * dt

def RK2(f, X, t, dt):
    k1 = f(X, t) * dt
    k2 = f(X + k1/2, t + dt/2) * dt
    return k2
    #n - n-1, distance from right and left, use distance to delta x, after moving every nugs, then the fries move,
while 1:
    rate(50)
    for i in range(numPlanks):
        if (i == 0):
            leftAcc = springAcc(nugs[i], edge1.pos)
            rightAcc = springAcc(nugs[i], nugs[i+1].pos)
        elif (i == numPlanks - 1):
            leftAcc = springAcc(nugs[i], nugs[i-1].pos)
            rightAcc = springAcc(nugs[i], edge2.pos)
        else:
            leftAcc = springAcc(nugs[i], nugs[i-1].pos)
            rightAcc = springAcc(nugs[i], nugs[i+1].pos)
        totalAcc = RK2(nugacc, nugs[i].velocity, t, dt) + leftAcc + rightAcc
        nugs[i].velocity += totalAcc
        nugs[i].pos += RK2(posi, nugs[i].velocity, t, dt)
    #for fry in fries:
    
    t += dt 
