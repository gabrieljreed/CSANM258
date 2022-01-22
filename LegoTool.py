import maya.cmds as mc

def deleteAll():
    mc.select(all=True)
    mc.delete()


def createLego(uLength = 4, uWidth = 2, fl = False):
    # Brick constants 
    unitHeight = 0.17
    unitWidth = 0.8
    thickness = 0.12
    
    brick = []
    
    # User defined parameters 
    flat = fl
    userLength = uLength
    userWidth = uWidth
    height = 0.32
    
    # Calculate dimensions 
    if not flat:
        height = 3 * height
    
    width = userWidth * unitWidth
    length = userLength * unitWidth
    
    # Create base 
    base = mc.polyCube(w=width, d=length, h=height)[0]
    mc.move(0, height/2, 0)
    
    brick = []
    
    # Create top studs 
    for i in range(userLength):
        for j in range(userWidth):
            stud = mc.polyCylinder(r=.24, h=unitHeight, sx=12)
            brick.append(stud[0])
            mc.move(-width/2 + unitWidth/2 + unitWidth*j, height + (unitHeight)/2, -length/2 + unitWidth/2 + unitWidth * i)\
    
    # Bottom boolean 
    bool = mc.polyCube(w=width - 2*thickness, d=length - 2*thickness, h=height-thickness)[0]
    mc.move(0, (height/2) - thickness/2, 0)
    base = mc.polyCBoolOp(base, bool, op=2)
    mc.delete(ch=1)
    brick.append(base[0])
    
    # Create underside studs 
    for i in range(userLength - 1):
        rad = 0.325
        if userLength == 1 or userWidth == 1:
            rad = rad / 2
        if userWidth == 1:
            stud = mc.polyCylinder(r=rad, h=height-thickness, sx=12)
            brick.append(stud[0])
            mc.move(0, (height-thickness)/2, -length/2 + i*unitWidth + unitWidth)
    
        for j in range(userWidth - 1):
            stud = mc.polyCylinder(r=rad, h=height-thickness, sx=12)
            brick.append(stud[0])
            mc.move(-width/2 + j*unitWidth + unitWidth, (height-thickness)/2, -length/2 + i*unitWidth + unitWidth)

    name = "Brick_" + str(userLength) + "x" + str(userWidth) + "_0"
    print(name)
    mc.group(brick, n=name)


# deleteAll()
createLego(2, 3)

