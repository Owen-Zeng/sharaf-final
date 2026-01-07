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

nugs = []
fries = []

for i in range(-100, 100, 200/numPlanks):
    nugs.append(sphere(pos = vec(i+100/numPlanks, 0, 0), color = color.orange, radius = 50/numPlanks))
    fries.append(box(pos = vector(i+100/numPlanks, 0, 0), color = color.yellow, length = 200/numPlanks))

    
equilPos.y = 0


def acc(v, t):
    return ((mass*g - b*v)/mass) + (-k * (ball.pos.y - equilPos)/mass)
    
def pos(v, t):
    return v * dt

def RK2(f, X, t, dt):
    k1 = f(X, t) * dt
    k2 = f(X + k1/2, t + dt/2) * dt
    return k2
    
while 1:
    rate(1/dt)
    for nug in nugs:
        nug.velocity += RK2(acc, nug.velocity, t, dt)
        nug.pos += RK2(pos, nug.velocity, t, dt)
    for fry in fries:
        fry.velocity += RK2(acc, fry.velocity, t, dt)
        fry.pos += RK2(pos, fry.velocity, t, dt)
    
    t += dt
