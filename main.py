Web VPython 3.2


buttonText = wtext(text = "\n Toggle Animation: ")
animationStatus = wtext(text = "Off ")
animationToggle = button(bind = toggleAnimation, text = "Toggle")


wt = wtext(text = "\nSelect Iterations: ")
selectIterations = slider(bind= iterationsSlider, min = 5, max =10, step = 1, disabled = True)
Iwt = wtext(text = "1")


wt = wtext(text = "\nEdge Exclusion: ")
edge = slider(bind = edgeSlider, min = 0, max = 45, step = 5)
Ewt = wtext(text = edge.value + "%")

swt = wtext(text = "\nStarting Seed Value: ")
seedSlider = slider(bind=seedSliderFunc, min=0.05, max=0.95, step=0.01, value=0.1)
seedWt = wtext(text="0.1")

Swt = wtext(text = "\nStart Simulation   ")
start = button(bind = toggleSim, text = "Start")

def handMenu(evt):
    return selectHand.value

def iterationsSlider(evt):
    Iwt.text = selectIteraions.value
    return selectIterations.value

def edgeSlider(evt):
    return edge.value

def seedSliderFunc(evt):
    seedWt.text = str(round(seedSlider.value, 2))

def toggleAnimation(evt):
    global animationStatus
    global animation

    animation = not animation

    if(animation):
        animationStatus.text = "On "
    else:
        animationStatus.text = "Off "
        
def toggleSim(evt):
    w = 10

edge1 = box(pos = (-100, 0 ,0))
edge2 = box(pos = (100, 0, 0))

ball = sphere(pos = initPos, mass = 4, make_trail = True, radius = 0.5)


gx = graph(title='vx vs Time', ytitle='velocity x', xtitle='Time')
gy = graph(title='vy vs Time', ytitle='velocity y', xtitle='Time')

cx = gcurve(graph = gx, color = color.blue)
cy = gcurve(graph = gy, color = color.purple)

dt = 0.1 
t = 1 
g = vec(0, -9.81, 0)

b = float(input("Enter b"))
v0 = 40
theta = 35


initVel = vec(v0 * cos(radians(theta)), v0 * sin(radians(theta)), 0)
ball.velocity = initVel

def acc(v, t):
    return (ball.mass*g - b*v)/ball.mass
    
    
def pos(v, t):
    return v * dt

def RK2(f, X, t, dt):
    k1 = f(X, t) * dt
    k2 = f(X + k1/2, t + dt/2) * dt
    return k2
    
while ball.pos.y >= 0:
    rate(1/dt)
    
    ball.velocity += RK2(acc, ball.velocity, t, dt)
    ball.pos += RK2(pos, ball.velocity, t, dt)
    
    t += dt
    
    
    cx.plot(t, ball.velocity.x)
    cy.plot(t, ball.velocity.y)
