Web VPython 3.2
scene.background = color.green
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

def snowman():
    sphere(pos = vec(-100,10,0), color = color.white, radius = 5)
    sphere(pos = vec(-100,18,0), color = color.white, radius = 4)
    box(pos = vec(-97,11,0), axis = vec(.3,0.35,0), length = 13, color = vec(0.531,0.318,.161))
    box(pos = vec(-103,11,0), axis = vec(-.3,.35, 0), length = 13, color = vec(0.531,0.318,.161))
    arrow(pos = vec(-100,17,2), axis = vec(0, 0, 1), length = 4, color = color.orange)
    
    sphere(pos = vec(-101,19,2.7), color = color.black, radius = 1.3) #eye
    sphere(pos = vec(-99,19,2.7), color = color.black, radius = 1.3) #eye
    
    sphere(pos = vec(-100,9,4.5), color = color.black, radius = 0.8) #body
    sphere(pos = vec(-100,10.5,4.6), color = color.black, radius = 0.8) #body 
    sphere(pos = vec(-100,12,3.9), color = color.black, radius = 0.8) #body
    
    sphere(pos = vec(-102,17,2.7), color = color.black, radius = .7) #mouth
    sphere(pos = vec(-101,16,2.7), color = color.black, radius = .7) #mouth
    sphere(pos = vec(-100,15.5,2.7), color = color.black, radius = 0.7) #mouth
    sphere(pos = vec(-99,16,2.7), color = color.black, radius = 0.7) #mouth 
    sphere(pos = vec(-98,17,2.7), color = color.black, radius = 0.7) #mouth
    
    box(pos = vec(-100,22,0), color = color.black, height = 1, length = 8, width = 8)
    cylinder(pos = vec(-100,23.5,0), color = color.black, length = 6, height = 7, width = 7, axis = vec(0,1,0))
    cylinder(pos = vec(-100,22.5,0), color = color.red, length = 2, height = 7, width = 7, axis = vec(0,1,0))
    
    

#snowman()
    

for i in range(-100, 100, 200/numPlanks):
    nugs.append(cylinder(pos = vec(i+100/numPlanks, -10/numPlanks, 0), color = color.orange, axis = vec(0,1,0), size = vec(15/numPlanks, 60/numPlanks, 50/numPlanks), texture = textures.rough, emissive = True))
    
#Length y
#Height x
#Width z
def macBig():
    cylinder(pos = vec(-100,5.1,0), axis = vec(0,1,0), height = 5, length = 0.2, width = 5, color = color.orange) #bottom bun
    cylinder(pos = vec(-100,5.3,0), axis = vec(0,1,0), height = 5, length = .2, width = 5, color = vec(0.531,0.318,.161)) #bottom patty
    cylinder(pos = vec(-100,5.5,0), axis = vec(0,1,0), height = 5, length = .1, width = 5, color = color.yellow) #bottom cheese
    cylinder(pos = vec(-100,5.6,0), axis = vec(0,1,0), height = 5, length = .1, width = 5, color = color.green) #bottom lettuce
    cylinder(pos = vec(-100,5.7,0), axis = vec(0,1,0), height = 5, length = .5, width = 5, color = color.orange) #middle bun
    cylinder(pos = vec(-100,6.2,0), axis = vec(0,1,0), height = 5, length = .2, width = 5, color = vec(0.531,0.318,.161)) #top patty
    cylinder(pos = vec(-100,6.4,0), axis = vec(0,1,0), height = 5, length = .1, width = 5, color = color.yellow) #top cheese
    cylinder(pos = vec(-100,6.5,0), axis = vec(0,1,0), height = 5, length = .1, width = 5, color = color.green) #top lettuce
    sphere(pos = vec(-100,6.7,0), size = vec(5,1.5,5), color = color.orange,) #top bun
#macBig()
    
def chicken():
    sphere(pos = vec(-100,10,0), color = color.yellow, radius = 4)
    sphere(pos = vec(-97,15,0), color = color.yellow, radius = 3)
    box(pos = vec(-102,8,1), axis = vec(0,1,0), length = 8, color = color.yellow)
    box(pos = vec(-102,8,-1), axis = vec(0,1,0), length = 8, color = color.yellow)
    box(pos = vec(-100,10.4,3), axis = vec(0,0.5,-0.5), length = 8.5, color = color.yellow)
    box(pos = vec(-100,10.4,-3), axis = vec(0,0.5,0.5), length = 8.5, color = color.yellow)
    sphere(pos = vec(-95.5,16.5,1), color = color.red, radius = 1.3)
    sphere(pos = vec(-95.5,16.5,-1), color = color.red, radius = 1.3)
    arrow(pos = vec(-95.2,16,0), length = 3, color = color.yellow)
#chicken()
    
