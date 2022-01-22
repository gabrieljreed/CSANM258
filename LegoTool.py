import maya.cmds as mc

mc.select(all=True)
mc.delete()

# Brick constants 
unitHeight = 0.17
unitWidth = 0.8
thickness = 0.12

# User defined parameters 
flat = True
userLength = 4
userWidth = 2
height = 0.32

# Calculate dimensions 
if not flat:
    height = 3 * height

width = userWidth * unitWidth
length = userLength * unitWidth

# Create base 
base = mc.polyCube(w=width, d=length, h=height)[0]
mc.move(0, height/2, 0)

# Create studs 
for i in range(userLength):
    for j in range(userWidth):
        mc.polyCylinder(r=.24, h=unitHeight, sx=12)
        mc.move(-width/2 + unitWidth/2 + unitWidth*j, height + (unitHeight)/2, -length/2 + unitWidth/2 + unitWidth * i)

# Bottom boolean 
bool = mc.polyCube(w=width - 2*thickness, d=length - 2*thickness, h=height-thickness)[0]
mc.move(0, (height/2) - thickness/2, 0)
mc.polyCBoolOp(base, bool, op=2)
mc.delete(ch=1)
