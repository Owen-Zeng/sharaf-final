Web VPython 3.2

edge1 = box(pos = vec(-100, 0 ,0), color = color.red, length = 10, height = 10, width = 10)
edge2 = box(pos = vec(100, 0, 0), color = color.red, length = 10, height = 10, width = 10)

numPlanks = float(input("Enter Number of Planks"))

#constants
dt = 0.1 
t = 1 
g = vec(0, -9.81, 0)
mass = 10
k = 200
b = 1

nugs = []
fries = []


for i in range(-100, 100, 200/numPlanks):
    nugs.append(sphere(pos = vec(i+100/numPlanks, 0, 0), color = color.orange, radius = 50/numPlanks))
    fries.append(box(pos = vector(i+100/numPlanks, 0, 0), color = color.yellow, length = 200/numPlanks), eqPos = vec(i+100/numPlanks,0,0))
    
for nug in nugs:
    nug.velocity = vec(0,0,0)

for fry in fries:
    fry.velocity = vec(0,0,0)
    
def fryacc(v, t):
    print(fry.pos)
    print(fry.eqPos)
    print(vec(-325234,0,0) - vec(0,0,0))
    print(fry.pos - fry.eqPos)
    
    return ((mass*g - b*v)/mass) + (-k * (fry.pos - fry.eqPos)/mass)

def nugacc(v, t):
    return ((mass*g - b*v)/mass)
    
def pos(v, t):
    return v * dt

def RK2(f, X, t, dt):
    k1 = f(X, t) * dt
    k2 = f(X + k1/2, t + dt/2) * dt
    return k2
    
while 1:
    rate(1/dt)
    for nug in nugs:
        nug.velocity += RK2(nugacc, nug.velocity, t, dt)
        nug.pos += RK2(pos, nug.velocity, t, dt)
    for fry in fries:
        fry.velocity += RK2(fryacc, fry.velocity, t, dt)
        fry.pos += RK2(pos, fry.velocity, t, dt)
    
    t += dt
