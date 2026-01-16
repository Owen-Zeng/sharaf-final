Web VPython 3.2

edge1 = box(pos = vec(-100, 0 ,0), color = color.red, length = 10, height = 1, width = 10)
edge2 = box(pos = vec(100, 0, 0), color = color.red, length = 10, height = 1, width = 10)

k = 0
numPlanks = 5
character = ""
setup = False
running = False
characterMass = 200


characterList = ["Snowman", "Man", "Chicken"]



select_spring_force = slider(bind =  select_k, step = 1, min = 200, max = 1000, value = 200)
spring_text = wtext(text = "Spring force(k): " + "200\n")
def select_k(evt):
    global k 
    k = select_spring_force.value
    spring_text.text = "Spring force(k): " + str(select_spring_force.value) + "\n"
    return select_spring_force.value


select_planks = slider(bind = plank_num, min = 5, max = 10, step = 1)
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
    
mykeys = keysdown()
prose = label() 
lastLen = len(prose.text)

def keyInput(evt):
    s = evt.key
    if ( s == 'left' or s is 'right' ):
        prose.text += s
        

scene.bind('keydown', keyInput)

start_button = button(bind = start, text = "Start")
setup_text = wtext(text = "Setup: False\n")

run_button = button(bind = run, text = "Run")
run_text = wtext(text = "Run: False\n")


nugs = []
fries = []

dt = 0.1 
t = 0
g = vec(0, -9.81, 0)
mass = 1500
k = 500

b0 = 2*sqrt(mass*k)
b = b0*0.1

def start(evt):
    global setup
    setup = not setup
    if setup:
        start_button.text = "Stop"
    else:
        start_button.text = "Start"
    setup_text.text = "Setup: " + str(setup) + "\n"
    
    
    for i in range(-100, 100, 200/numPlanks):
        nugs.append(sphere(pos = vec(i+100/numPlanks, 0, 0), color = color.orange, radius = 50/numPlanks, eqPos = vec(i+100/numPlanks,0,0)))
        fries.append(box(pos = vector(i+100/numPlanks, 0, 0), color = color.yellow, length = 200/numPlanks, eqPos = vec(i+100/numPlanks,0,0)))
        
    for nug in nugs:
        nug.velocity = vec(0,0,0)
        nug.mass = 1500
    
    for fry in fries:
        fry.velocity = vec(0,0,0)

    start_button.disabled = True
    select_planks.disabled = True
    
def run(evt):
    global running
    running = not running
    if running:
        run_button.text = "Stop"
    else:
        run_button.text = "Start"
    run_text.text = "Run: " + running + "\n"
        
        
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
    if(setup):
        if running:
            curr = -1
            if (lastLen is not len(prose.text)):
                if prose.text[len(prose.text)-1] is right and curr < numPlanks-1:
                    curr+=1
                if prose.text[len(prose.text)-1] is left and curr > 0:
                    curr-=1
                lastLen = len(prose.text)
            if curr >= 0:
                nugs[i].mass += characterMass
        for i in range(numPlanks):
            mass = nugs[i].mass
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
