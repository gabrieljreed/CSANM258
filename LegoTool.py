import maya.cmds as mc


class LegoTool:
    def deleteAll(self):
        mc.select(all=True)
        mc.delete()

    def createLegoBrick(self, uLength=4, uWidth=2, fl=False):
        # Brick constants FIXME: Make these global
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
        mc.move(0, height / 2, 0)

        # Create top studs
        for i in range(userLength):
            for j in range(userWidth):
                stud = mc.polyCylinder(r=.24, h=unitHeight, sx=12)
                brick.append(stud[0])
                mc.move(-width / 2 + unitWidth / 2 + unitWidth * j, height + (unitHeight) / 2,
                        -length / 2 + unitWidth / 2 + unitWidth * i)
        # Bottom boolean
        cutout = mc.polyCube(w=width - 2 * thickness, d=length - 2 * thickness, h=height - thickness)[0]
        mc.move(0, (height / 2) - thickness / 2, 0)
        base = mc.polyCBoolOp(base, cutout, op=2)
        mc.delete(ch=1)
        brick.append(base[0])

        # Create underside studs
        # FIXME: This only works in one direction
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

        name = "Brick_" + str(userLength) + "x" + str(userWidth) + "_0"
        if flat:
            name += "_flat"
        print(name)
        mc.group(brick, n=name)


    def createLegoCylinder(self, flat=False):
        unitHeight = 0.17

        height = 0.32
        if not flat:
            height = 3 * height
        baseHeight = 0.762
        totalHeight = 0.96

        # Create base
        mc.polyCylinder(h=baseHeight, r=0.38)
        mc.move(0, totalHeight/2, 0)

        # Create top stud
        mc.polyCylinder(r=0.24, h=unitHeight)
        mc.move(0, totalHeight + (unitHeight) / 2, 0)

        # Bottom thing
        mc.polyCylinder(r=0.28, h=baseHeight)
        mc.move(0, baseHeight/2, 0)


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


legoTool = LegoTool()

legoTool.deleteAll()
legoTool.createLegoBrick(2, 2)
mc.move(-2, 0, -2)
legoTool.createLegoCylinder()
