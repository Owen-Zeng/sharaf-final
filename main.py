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
    