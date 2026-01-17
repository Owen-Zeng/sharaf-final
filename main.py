Web VPython 3.2

# Our project is the bridge project where we have a bridge made of "nuggets" that are connected to each other with "fries".
# The bridge is supported by two blocks at the edges, and has gravity and spring forces acting on the nuggets in the brdige.
# For our user input, we have a select spring constant slider that moves from 200 to 1000.
# We also have a slider that allows the user to select the number of planks.
# The character is selected from a menu, with either no character, a snowman, a bigmac, or a chicken.
# The user uses the setup button to set up the bridge after selecting number of planks and their character. 
# The run button is used to let the user move the chracter around with the left and right arrow keys.

scene.background = vec(0.537,0.812,0.941)
edge1 = box(pos = vec(-100, 0 ,0), color = color.red, length = 10, height = 1, width = 10, height = 10)
edge2 = box(pos = vec(100, 0, 0), color = color.red, length = 10, height = 1, width = 10, height = 10)

k = 0
numPlanks = 5
character = ""
setup = False
running = False
characterMass = 10000
player = None


characterList = ["Choose a character", "Snowman", "Big Mac", "Chicken"]

select_spring_force = slider(bind =  select_k, step = 1, min = 200, max = 1000, value = 200)
spring_text = wtext(text = "Spring constant(k): " + "200\n")
def select_k(evt):
    global k 
    k = select_spring_force.value
    spring_text.text = "Spring constant(k): " + str(select_spring_force.value) + "\n"
    return select_spring_force.value


select_planks = slider(bind = plank_num, min = 5, max = 10, step = 1)
planks_text = wtext(text = "Number of Planks: " + "4\n")
def plank_num(evt):
    global numPlanks
    numPlanks = select_planks.value
    planks_text.text = "Number of Planks: " + str(select_planks.value - 1) + "\n"
    return select_planks.value

select_char = menu(bind = getChar, choices = characterList)
character_text = wtext(text = "Character:" + "Choose a character\n")
def getChar(evt):
    global character
    if evt.index == 0:
        character = "Choose a character"
    elif evt.index == 1:
        character = "Snowman"
    elif evt.index == 2:
        character = "Big Mac"
    elif evt.index == 3:
        character = "Chicken"
    
    character_text.text = "Character:" + character + "\n"
    return character
    
mykeys = keysdown()

currIndex = -1
#-1 to nugs.length


def keyInput(evt):
    global currIndex
    if running:
        s = evt.key
        if ( s == 'left' and (currIndex > -1)):
            currIndex-=1
        
        if ( s == 'right' and (currIndex < len(nugs))):
             currIndex+=1
        

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
    currIndex = -1
    setup = not setup
    if setup:
        start_button.text = "Stop"
    else:
        start_button.text = "Start"
    setup_text.text = "Setup: " + str(setup) + "\n"

        
    step = 200 / numPlanks
    
    for i in range(1, numPlanks):
        xpos = edge1.pos.x + (i * step)
        nugs.append(cylinder(pos = vec(xpos, -10/numPlanks, 0), 
                    color = color.orange, 
                    axis = vec(0,1,0), 
                    size = 2*vec(15/numPlanks, 60/numPlanks, 50/numPlanks), 
                    texture = textures.rough, 
                    emissive = True))     
        
    for i in range(numPlanks):
        xc = edge1.pos.x + (i * step) + (step / 2)
        
        fries.append(box(pos = vector(xc, 0, 0), 
                    color = color.yellow, 
                    length = step, 
                    height = 3,
                    width = 3,
                    texture = textures.rough))
        
    for nug in nugs:
        nug.velocity = vec(0,0,0)
        nug.mass = 1500
    
    for fry in fries:
        fry.velocity = vec(0,0,0)

    global player
    if (character == 'Big Mac'):
        player = macBig()
    elif (character == 'Chicken'):
        player = chicken()
    elif (character == 'Snowman'):
        player = snowman()
    
    start_button.disabled = True
    select_planks.disabled = True
    select_char.disabled = True
    
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
            for i in range(len(nugs)):
                nugs[i].mass = 1500
                if (i == currIndex):
                    nugs[i].mass += characterMass 
            
            if player != None:
                target_pos = vec(0,0,0)
                if currIndex == -1:
                    target_pos = edge1.pos
                elif currIndex == len(nugs):
                    target_pos = edge2.pos
                else:
                    target_pos = nugs[currIndex].pos
                player.pos = target_pos + vec(0, 10, 0) 
                pass 
            pass 

        for i in range(len(nugs)):
            mass = nugs[i].mass
            if i == 0:
                leftAcc = springAcc(nugs[i], edge1.pos)
                rightAcc = springAcc(nugs[i], nugs[i+1].pos)
            elif (i == len(nugs) - 1):
                leftAcc = springAcc(nugs[i], nugs[i-1].pos)
                rightAcc = springAcc(nugs[i], edge2.pos)
            else:
                leftAcc = springAcc(nugs[i], nugs[i-1].pos)
                rightAcc = springAcc(nugs[i], nugs[i+1].pos)
                
            totalAcc = RK2(nugacc, nugs[i].velocity, t, dt) + leftAcc + rightAcc
            nugs[i].velocity += totalAcc
            nugs[i].pos += RK2(posi, nugs[i].velocity, t, dt)
        for i in range(len(fries)):
            if i == 0:
                left = edge1.pos
            else:
                left = nugs[i-1].pos
                
            if i == len(fries) - 1:
                right = edge2.pos
            else:
                right = nugs[i].pos
                
            center = (left + right) / 2
            axis = right - left
            fries[i].pos = center
            fries[i].axis = axis
            fries[i].length = mag(axis)
        
        
        t += dt 
def snowman():
    parts = []
    parts.append(sphere(pos = vec(-100,10,0), color = color.white, radius = 5))
    parts.append(sphere(pos = vec(-100,18,0), color = color.white, radius = 4))
    parts.append(box(pos = vec(-97,11,0), axis = vec(.3,0.35,0), length = 13, color = vec(0.531,0.318,.161)))
    parts.append(box(pos = vec(-103,11,0), axis = vec(-.3,.35, 0), length = 13, color = vec(0.531,0.318,.161)))
    parts.append(arrow(pos = vec(-100,17,2), axis = vec(0, 0, 1), length = 4, color = color.orange))
    
    parts.append(sphere(pos = vec(-101,19,2.7), color = color.black, radius = 1.3)) #eye
    parts.append(sphere(pos = vec(-99,19,2.7), color = color.black, radius = 1.3)) #eye
    
    parts.append(sphere(pos = vec(-100,9,4.5), color = color.black, radius = 0.8)) #body
    parts.append(sphere(pos = vec(-100,10.5,4.6), color = color.black, radius = 0.8)) #body 
    parts.append(sphere(pos = vec(-100,12,3.9), color = color.black, radius = 0.8)) #body
    
    parts.append(sphere(pos = vec(-102,17,2.7), color = color.black, radius = .7)) #mouth
    parts.append(sphere(pos = vec(-101,16,2.7), color = color.black, radius = .7)) #mouth
    parts.append(sphere(pos = vec(-100,15.5,2.7), color = color.black, radius = 0.7)) #mouth
    parts.append(sphere(pos = vec(-99,16,2.7), color = color.black, radius = 0.7)) #mouth 
    parts.append(sphere(pos = vec(-98,17,2.7), color = color.black, radius = 0.7)) #mouth
    
    parts.append(box(pos = vec(-100,22,0), color = color.black, height = 1, length = 8, width = 8))
    parts.append(cylinder(pos = vec(-100,23.5,0), color = color.black, length = 6, height = 7, width = 7, axis = vec(0,1,0)))
    parts.append(cylinder(pos = vec(-100,22.5,0), color = color.red, length = 2, height = 7, width = 7, axis = vec(0,1,0)))
    
    return compound(parts)

#snowman()
    
#Length y
#Height x
#Width z
def macBig():
    parts = []
    parts.append(cylinder(pos = vec(-100,5.1,0), axis = vec(0,1,0), height = 13, length = 0.6, width = 13, color = color.orange)) #bottom bun
    parts.append(cylinder(pos = vec(-100,5.7,0), axis = vec(0,1,0), height = 13, length = .6, width = 13, color = vec(0.531,0.318,.161))) #bottom patty
    parts.append(box(pos = vec(-100,6.3,0), axis = vec(0,1,0), height = 13, length = .3, width = 13, color = color.yellow)) #bottom cheese
    parts.append(cylinder(pos = vec(-100,6.6,0), axis = vec(0,1,0), height = 13, length = .3, width = 13, color = color.green)) #bottom lettuce
    parts.append(cylinder(pos = vec(-100,6.9,0), axis = vec(0,1,0), height = 13, length = 1.5, width = 13, color = color.orange)) #middle bun
    parts.append(cylinder(pos = vec(-100,8.4,0), axis = vec(0,1,0), height = 13, length = .6, width = 13, color = vec(0.531,0.318,.161))) #top patty
    parts.append(box(pos = vec(-100,9.0,0), axis = vec(0,1,0), height = 13, length = .3, width = 13, color = color.yellow)) #top cheese
    parts.append(cylinder(pos = vec(-100,9.3,0), axis = vec(0,1,0), height = 13, length = .3, width = 13, color = color.green)) #top lettuce
    parts.append(sphere(pos = vec(-100,9.9,0), size = vec(12,4,12), color = color.orange)) #top bun
    return compound(parts)
#macBig()
    
def chicken():
    parts = []
    parts.append(sphere(pos = vec(-100,10,0), color = color.yellow, radius = 4))
    parts.append(sphere(pos = vec(-97,15,0), color = color.yellow, radius = 3))
    parts.append(box(pos = vec(-102,8,1), axis = vec(0,1,0), length = 8, color = color.yellow))
    parts.append(box(pos = vec(-102,8,-1), axis = vec(0,1,0), length = 8, color = color.yellow))
    parts.append(box(pos = vec(-100,10.4,3), axis = vec(0,0.5,-0.5), length = 8.5, color = color.yellow))
    parts.append(box(pos = vec(-100,10.4,-3), axis = vec(0,0.5,0.5), length = 8.5, color = color.yellow))
    parts.append(sphere(pos = vec(-95.5,16.5,1), color = color.red, radius = 1.3))
    parts.append(sphere(pos = vec(-95.5,16.5,-1), color = color.red, radius = 1.3))
    parts.append(arrow(pos = vec(-95.2,16,0), length = 3, color = color.yellow))
    return compound(parts)
#chicken()
    
