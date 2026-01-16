def snowman():
    sphere(pos = vec(-100,10,0), color = color.white, radius = 5)
    sphere(pos = vec(-100,18,0), color = color.white, radius = 4)
    box(pos = vec(-97,11,0), axis = vec(.3,0.35,0), length = 13, color = color.green)
    box(pos = vec(-103,11,0), axis = vec(-.3,.35, 0), length = 13, color = color.green)
    arrow(pos = vec(-100,17,2), axis = vec(0, 0, 1), length = 4, color = color.orange)
    sphere(pos = vec(-101,19,3.2), color = color.orange, radius = 1.3)
    sphere(pos = vec(-99,19,3.2), color = color.orange, radius = 1.3)
    
    

#snowman()
    

for i in range(-100, 100, 200/numPlanks):
    nugs.append(cylinder(pos = vec(i+100/numPlanks, -10/numPlanks, 0), color = color.orange, axis = vec(0,1,0), size = vec(15/numPlanks, 60/numPlanks, 50/numPlanks), texture = textures.rough, emissive = True))
    
    
#L up
#H Sideways
#W In out
def macBig():
    cylinder(pos = vec(-100,5.1,0), axis = vec(0,1,0), height = 5, length = 0.2, width = 5, color = color.orange) #bottom bun
    cylinder(pos = vec(-100,5.3,0), axis = vec(0,1,0), height = 5, length = .2, width = 5, color = color.black) #bottom patty
    cylinder(pos = vec(-100,5.5,0), axis = vec(0,1,0), height = 5, length = .1, width = 5, color = color.yellow) #bottom cheese
    cylinder(pos = vec(-100,5.6,0), axis = vec(0,1,0), height = 5, length = .1, width = 5, color = color.green) #bottom lettuce
    cylinder(pos = vec(-100,5.7,0), axis = vec(0,1,0), height = 5, length = .5, width = 5, color = color.orange) #middle bun
    cylinder(pos = vec(-100,6.2,0), axis = vec(0,1,0), height = 5, length = .2, width = 5, color = color.black) #top patty
    cylinder(pos = vec(-100,6.4,0), axis = vec(0,1,0), height = 5, length = .1, width = 5, color = color.yellow) #top cheese
    cylinder(pos = vec(-100,6.5,0), axis = vec(0,1,0), height = 5, length = .1, width = 5, color = color.green) #top lettuce
    sphere(pos = vec(-100,6.45,0), axis = vec(0,1,0), radius = 2.3, color = color.orange) #top bun
#macBig()
    
def chicken():
    sphere(pos = vec(-100,10,0), color = color.yellow, radius = 4)
    sphere(pos = vec(-97,15,0), color = color.yellow, radius = 3)
    box(pos = vec(-102,8,1), axis = vec(0,1,0), length = 8, color = color.white)
    box(pos = vec(-102,8,-1), axis = vec(0,1,0), length = 8, color = color.white)
    box(pos = vec(-100,10.4,3), axis = vec(0,0.5,-0.5), length = 8.5, color = color.white)
    box(pos = vec(-100,10.4,-3), axis = vec(0,0.5,0.5), length = 8.5, color = color.white)
    sphere(pos = vec(-95.5,16.5,1), color = color.orange, radius = 1.3)
    sphere(pos = vec(-95.5,16.5,-1), color = color.orange, radius = 1.3)
    arrow(pos = vec(-95.2,16,0), length = 3, color = color.orange)
#chicken()
