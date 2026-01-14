Web VPython 3.2

edge1 = box(pos = vec(-100, 0 ,0), color = color.red, length = 10, height = 1, width = 10)
edge2 = box(pos = vec(100, 0, 0), color = color.red, length = 10, height = 1, width = 10)

spring_force = 0
numPlanks = 0
character = ""
running = False

characterList = ["Snowman", "Man", "Chicken"]


select_spring_force = slider(bind =  select_k)
spring_text = wtext(text = "Spring force(k): " + "0.05\n")
def select_k(evt):
    global spring_force
    spring_force = select_spring_force.value
    spring_text.text = "Spring force(k): " + str(select_spring_force.value) + "\n"
    return select_spring_force.value


select_planks = slider(bind = plank_num, min = 5, max = 10)
planks_text = wtext(text = "Number of Planks: " + "5\n")
def plank_num(evt):
    global numPlanks
    numPlanks = select_planks.value
    planks_text.text = "Number of Planks: " + str(select_planks.value) + "\n"
    return select_planks.value

select_char = menu(bind = getChar, choices = characterList)
character_text = wtext(text = "Character:" + "Snowman\n")
def getChar(evt):
    if evt.index == 0:
        character = "Snowman"
    elif evt.index == 1:
        character = "Man"
    elif evt.index == 2:
        character = "Chicken"

    character_text.text = "Character:" + character + "\n"
    return character

start_button = button(bind = start, text = "Start")
running_text = wtext(text = "Running: False\n")
def start(evt):
    global running
    running = not running
    if running:
        start_button.text = "Stop"
    else:
        start_button.text = "Start"
    running_text.text = "Running: " + str(running) + "\n"

numPlanks = int(input("Enter Number of Planks"))

#constants
dt = 0.1 
t = 1 
g = vec(0, -9.81, 0)
mass = 1500
k = 200

b0 = 2*sqrt(mass*k)
b = b0*0.1

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
    return ((-k * (nug.pos - X)) - b*nug.velocity)/mass

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
    rate(500)
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
    for i in range(len(fries)):
        if (i == 0):
            left = edge1.pos
        else:
            left = nugs[i].pos
        if (i == len(fries) - 1):
            right = edge2.pos
        else:
            right = nugs[i+1].pos
            
        center = (left + right) / 2
        axis = right - left
        fries[i].pos = center
        fries[i].axis = axis
        fries[i].length = mag(axis)
    
    t += dt 
