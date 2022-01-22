import maya.cmds as mc

mc.select(all=True)
mc.delete()

# Brick constants 
studHeight = 0.17
studWidth = 0.8
thickness = 0.12

# User defined parameters 
flat = True
userLength = 4
userWidth = 2
height = None


if flat:
    height = .32
else:
    height = .96

width = userWidth * studWidth
length = userLength * studWidth

base = mc.polyCube(w=width, d=length, h=height)[0]
mc.move(0, height/2, 0)
print("length: ", length)
print("width: ", width)

for i in range(userLength):
    for j in range(userWidth):
        mc.polyCylinder(r=.24, h=studHeight, sx=12)
        mc.move(-width/2 + studWidth/2 + studWidth*j, height + (studHeight)/2, -length/2 + studWidth/2 + studWidth * i)


bool = mc.polyCube(w=width - 2*thickness, d=length - 2*thickness, h=height-thickness)[0]
mc.move(0, (height/2) - thickness/2, 0)
mc.polyCBoolOp(base, bool, op=2)
mc.delete(ch=1)
