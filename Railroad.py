import maya.cmds as mc

mc.select(all=True)
mc.delete()

# Track 
trackL = mc.polyCube(name="trackL", w=30, h=1, d=0.3)
trackR = mc.polyCube(name="trackR", w=30, h=1, d=0.3)

mc.move(0,0.5,-1.8, "trackL", relative=True)
mc.move(0,0.5,1.8, "trackR", relative=True)

mc.polyCube(w=30, h=0.2, d=0.2)
mc.move(0,0.1,2)

mc.polyCube(w=30, h=0.2, d=0.2)
mc.move(0,0.1,-2)

mc.polyCube(w=30, h=0.2, d=0.2)
mc.move(0,0.9,2)

mc.polyCube(w=30, h=0.2, d=0.2)
mc.move(0,0.9,-2)


# Slats 
for i in range(10):
    mc.polyCube(w=1, h=0.1, d=6)
    mc.move(i*3 - 15, 0, 0)


# Little thingies 
for i in range(10):
    mc.polyCube(w=1, h=0.1, d=0.6)
    mc.move(i*3 - 15, 0.1, -2.4)
    
for i in range(10):
    mc.polyCube(w=1, h=0.1, d=0.6)
    mc.move(i*3 - 15, 0.1, 2.4)


# Thingy Bolts
for i in range(10):
    mc.polySphere(r=0.1)
    mc.move(i*3 - 15.2, 0.1, -2.4)
    
for i in range(10):
    mc.polySphere(r=0.1)
    mc.move(i*3 - 14.8, 0.1, -2.4)

for i in range(10):
    mc.polySphere(r=0.1)
    mc.move(i*3 - 15.2, 0.1, 2.4)
    
for i in range(10):
    mc.polySphere(r=0.1)
    mc.move(i*3 - 14.8, 0.1, 2.4)


# Track bolts 





    
