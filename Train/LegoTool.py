import maya.cmds as mc
import random

class LegoToolWindow(object):

    def __init__(self):
        self.window = "Lego Tool"
        self.title = "Lego Tool"
        self.size = (400, 400)

        if mc.window(self.window, exists=True):
            mc.deleteUI(self.window, window=True)

        self.window = mc.window(self.window, title=self.title, widthHeight=self.size)

        mc.columnLayout(adjustableColumn=True)

        self.uWidth = mc.intSliderGrp(field=True, label='Width', minValue=1, maxValue=15, fieldMinValue=1,
                                      fieldMaxValue=100, value=2)
        self.uLength = mc.intSliderGrp(field=True, label='Length', minValue=1, maxValue=15, fieldMinValue=1,
                                       fieldMaxValue=100, value=4)

        self.uFlat = mc.checkBoxGrp(columnWidth2=[100, 165], numberOfCheckBoxes=1, label='Flat', v1=False)

        self.createBtn = mc.button(label="Create")

        mc.showWindow()


class LegoTool:
    def __init__(self):
        self.numBricks = 0
        self.numCylinders = 0
    
    def deleteAll(self):
        mc.select(all=True)
        mc.delete()

    def createLegoBrick(self, uLength=4, uWidth=2, flat=False, top=True, bottom=True):
        # Brick constants FIXME: Make these global
        unitHeight = 0.17
        unitWidth = 0.8
        thickness = 0.12

        brick = []

        # User defined parameters
        
        userLength = uLength
        userWidth = uWidth
        height = 0.32
        flipped = False
        
        if userLength == 1:
            # flip width and length 
            temp = userLength
            userLength = userWidth
            userWidth = temp
            flipped=True

        # Calculate dimensions
        if not flat:
            height = 3 * height

        width = userWidth * unitWidth
        length = userLength * unitWidth

        # Create base
        base = mc.polyCube(w=width, d=length, h=height)[0]
        mc.polyBevel(o=0.02)
        mc.move(0, height / 2, 0)
    
        if top:
            # Create top studs
            for i in range(userLength):
                for j in range(userWidth):
                    stud = mc.polyCylinder(r=.24, h=unitHeight, sx=12)
                    brick.append(stud[0])
                    mc.move(-width / 2 + unitWidth / 2 + unitWidth * j, height + (unitHeight) / 2,
                            -length / 2 + unitWidth / 2 + unitWidth * i)
        
        if bottom:
            # Bottom boolean
            cutout = mc.polyCube(w=width - 2 * thickness, d=length - 2 * thickness, h=height - thickness)[0]
            mc.move(0, (height / 2) - thickness / 2, 0)
            base = mc.polyCBoolOp(base, cutout, op=2)
            mc.delete(ch=1)
            brick.append(base[0])
    
            # Create underside studs
            for i in range(userLength - 1):
                rad = 0.325
                if userLength == 1 or userWidth == 1:
                    rad = rad / 2
                if userWidth == 1:
                    stud = mc.polyCylinder(r=rad, h=height - thickness, sx=12)
                    brick.append(stud[0])
                    mc.move(0, (height - thickness) / 2, -length / 2 + i * unitWidth + unitWidth)
    
                for j in range(userWidth - 1):
                    stud = mc.polyCylinder(r=rad, h=height - thickness, sx=12)
                    brick.append(stud[0])
                    mc.move(-width / 2 + j * unitWidth + unitWidth, (height - thickness) / 2,
                            -length / 2 + i * unitWidth + unitWidth)
        else:
            brick.append(base)
        
        name = "Brick_" + str(userLength) + "x" + str(userWidth) + "_" + str(self.numBricks)
        if flat:
            name += "_flat"
        mc.group(brick, n=name)
        if flipped:
            mc.rotate(0, 90, 0, r=True)
        self.numBricks += 1
        return name


    def createLegoCylinder(self, flat=False, top=True, bottom=True):
        brick = []
        
        unitHeight = 0.17
        baseHeight = 0.762
        totalHeight = 0.96
        if flat:
            baseHeight = 0.1
            totalHeight = 0.3

        # Create base
        cylinderBase = mc.polyCylinder(h=baseHeight, r=0.38, sx=12, n="base")
        mc.move(0, totalHeight/2 + (totalHeight-baseHeight)/8, 0)
        
        # Bottom thing
        if flat:
            baseHeight *= 2
        
        if bottom:
            cylinderBool = mc.polyCylinder(r=0.3, h=baseHeight, sx=12)
            mc.move(0, baseHeight/2, 0)
            cylinderBase = mc.polyCBoolOp(cylinderBase, cylinderBool, op=2)
            mc.delete(ch=1)
        brick.append(cylinderBase[0])
        
        bottomBase = mc.polyCylinder(r=0.3, h=baseHeight, sx=12)
        mc.move(0, baseHeight/2, 0)
        if bottom: 
            bottomBool = mc.polyCylinder(r=0.24, h=baseHeight, sx=12)
            mc.move(0, baseHeight/2, 0)
            bottomBase = mc.polyCBoolOp(bottomBase, bottomBool, op=2)
            mc.delete(ch=1)
        brick.append(bottomBase[0])
        
        
        if top:
            # Create top stud
            studBase = mc.polyCylinder(r=0.24, h=unitHeight, sx=12)[0]
            mc.move(0, totalHeight, 0)
            if not flat:
                studBool = mc.polyCylinder(r=0.16, h=unitHeight, sx=12)[0]
                mc.move(0, totalHeight, 0)
                studBase = mc.polyCBoolOp(studBase, studBool, op=2)[0]
                mc.delete(ch=1)
            brick.append(studBase)
        
        name = "Cylinder_" + str(self.numCylinders)
        if flat:
            name="Stud_" + str(self.numCylinders)
        mc.group(brick, n=name)
        self.numCylinders += 1
        return name

    
    def moveLego(self, x=0, y=0, z=0, flat=False):
        mc.move(x*0.8, y*0.96, z*0.8) 
    
    
    def createTracks(self, length=5):
        tracks = []
        
        for i in range(length*3 + 1):
            brick = self.createLegoBrick(10, 2, True, True, False)
            mc.move(0.8*4*i - 0.4*11, 0, 0)
            tracks.append(brick)
            
            brick = self.createLegoBrick(1, 2, True, True, False)
            mc.move(0.8*4*i - 0.4*11, 0.32, + 0.4 + 0.8*3)
            tracks.append(brick)
            
            brick = self.createLegoBrick(1, 2, True, True, False)
            mc.move(0.8*4*i - 0.4*11, 0.32, - (0.4 + 0.8*3))
            tracks.append(brick)
            
            # FIXME: Clean this up 
            stud = self.createLegoCylinder(True, bottom=False)
            mc.move(0.8*4*i - 0.4*11 + 0.4, 0.32, + 0.4 + 0.8*1)
            tracks.append(stud)
            
            stud = self.createLegoCylinder(True, bottom=False)
            mc.move(0.8*4*i - 0.4*11 - 0.4, 0.32, + 0.4 + 0.8*1)
            tracks.append(stud)
            
            stud = self.createLegoCylinder(True, bottom=False)
            mc.move(0.8*4*i - 0.4*11 + 0.4, 0.32, - 0.4 - 0.8*1)
            tracks.append(stud)
            
            stud = self.createLegoCylinder(True, bottom=False)
            mc.move(0.8*4*i - 0.4*11 - 0.4, 0.32, - 0.4 - 0.8*1)
            tracks.append(stud)

        for i in range(length):
            brickLength = 12
            brick = self.createLegoBrick(1, brickLength, bottom=False)
            mc.move(0.4 + brickLength*0.8*i, 0.32, -0.4 - 0.8*2)
            tracks.append(brick)
            
            brick = self.createLegoBrick(1, brickLength, bottom=False)
            mc.move(0.4 + brickLength*0.8*i, 0.32,  0.4 + 0.8*2)
            tracks.append(brick)
        
        mc.group(tracks, n="Train Tracks")
    
    
    def createFence(self, length=9):
        fence = []
        slat=None
        
        # Create slats 
        numSlats = length//2
        for i in range(numSlats):
            j = random.uniform(0, 1)
            if j > 0.3 or i == 0 or i == numSlats-1:
                slat = self.createLegoBrick(5, 1, True)
                mc.move(i*0.8*2 - 0.8*(numSlats - 1), 0, 0.8)
                fence.append(slat)
        
        # Create back boards 
        board = self.createLegoBrick(1, length, True)
        mc.move(0, 0.32, 0)
        fence.append(board)
        
        board2 = self.createLegoBrick(1, length, True)
        mc.move(0, 0.32, 0.8*2)
        fence.append(board2)
        
        # Create random studs 
        numStuds = int(random.uniform(length*0.3, length))
        
        for i in range(numStuds):
            stud = self.createLegoCylinder(True)
            j = random.uniform(0,1)
            z=0
            if j > 0.5:
                z=0.8*2
            x = int(random.uniform(0, length))
            mc.move(x*0.8 - 0.8*(numSlats), 0.64, z)
            fence.append(stud)
        
        # Group
        mc.group(fence, n="Fence")
        mc.move(10, 1.6, 17)
        mc.rotate(-90, 20, 0, r=True)





legoTool = LegoTool()
legoTool.deleteAll()
# legoTool.createTracks(length=1)

# Train car 
# Baseplate 
legoTool.createLegoBrick(10, 20, bottom=False, flat=True)
legoTool.moveLego(0, 2/3, 0)

# Walls 
legoTool.createLegoBrick(1, 16, bottom=False, top=False)
legoTool.moveLego(0, 1, 4.5)
legoTool.createLegoBrick(1, 16, bottom=False, top=False)
legoTool.moveLego(0, 1, -4.5)

legoTool.createLegoBrick(3, 1, bottom=False, top=False)
legoTool.moveLego(7.5, 1, 2.5)
legoTool.createLegoBrick(3, 1, bottom=False, top=False)
legoTool.moveLego(7.5, 1, -2.5)
legoTool.createLegoBrick(3, 1, bottom=False, top=False)
legoTool.moveLego(-7.5, 1, -2.5)
legoTool.createLegoBrick(3, 1, bottom=False, top=False)
legoTool.moveLego(-7.5, 1, 2.5)

legoTool.createLegoBrick(4, 1, bottom=False, top=False)
legoTool.moveLego(7.5, 2, 3)
legoTool.createLegoBrick(4, 1, bottom=False, top=False)
legoTool.moveLego(7.5, 2, -3)
legoTool.createLegoBrick(4, 1, bottom=False, top=False)
legoTool.moveLego(-7.5, 2, 3)
legoTool.createLegoBrick(4, 1, bottom=False, top=False)
legoTool.moveLego(-7.5, 2, -3)

legoTool.createLegoBrick(1, 14, bottom=False, top=False)
legoTool.moveLego(0, 2, 4.5)
legoTool.createLegoBrick(1, 14, bottom=False, top=False)
legoTool.moveLego(0, 2, -4.5)

# Sides 
for i in range(2):
    side = 1
    if i == 0:
        side = -1
    legoTool.createLegoBrick(1, 12)
    legoTool.moveLego(0, 1, 3.5 * side)
    legoTool.createLegoBrick(1, 12)
    legoTool.moveLego(0, 2, 3.5 * side)


for j in range(2):
    side = 1
    if j == 0:
        side = -1

    legoTool.createLegoBrick(1, 12, top=False, bottom=False)
    legoTool.moveLego(0, 5, 3.5 * side)
    
    for i in range(2):
        legoTool.createLegoBrick(1, 2, top=False, bottom=False)
        legoTool.moveLego(2, i+3, 3.5 * side)
        
        legoTool.createLegoBrick(1, 2, top=False, bottom=False)
        legoTool.moveLego(-2, i+3, 3.5 * side)

# Front and back 
for i in range(2):
    side = 1
    if i == 0:
        side = -1
    legoTool.createLegoBrick(8, 1, top=False)
    legoTool.moveLego(6.5 * side, 5, 0)

for j in range(4):
    long = 1
    if j % 2 == 0:
        long = -1
    wide = 1
    if j < 2:
        wide = -1

    for i in range(4):
        if i < 2:
            legoTool.createLegoBrick(3, 1, top=True, bottom=False)
            legoTool.moveLego(6.5 * long, i+1, 2.5 * wide)
        else:
            legoTool.createLegoBrick(1, 2, top=False, bottom=False)
            legoTool.moveLego(6 * long, i+1, 3.5 * wide)
            legoTool.createLegoBrick(1, 1, top=False, bottom=False)
            legoTool.moveLego(6.5 * long, i+1, 1.5 * wide)

# Roof 
legoTool.createLegoBrick(10, 18, flat=True)
legoTool.moveLego(0, 6, 0)

legoTool.createLegoBrick(2, 10)
legoTool.moveLego(0, 6 + 1/3, 0)

legoTool.createLegoBrick(1, 16, flat=True, top=False, bottom=False)
legoTool.moveLego(0, 6 + 1/3, 4.5)
legoTool.createLegoBrick(1, 16, flat=True, top=False, bottom=False)
legoTool.moveLego(0, 6 + 1/3, -4.5)
legoTool.createLegoBrick(10, 1, flat=True, top=False, bottom=False)
legoTool.moveLego(8.5, 6+1/3, 0)
legoTool.createLegoBrick(10, 1, flat=True, top=False, bottom=False)
legoTool.moveLego(-8.5, 6+1/3, 0)

for i in range(5):
    legoTool.createLegoCylinder(flat=True, bottom=False)
    legoTool.moveLego(2*i-4, 7 + 1/3, 0)
