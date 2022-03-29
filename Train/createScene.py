import maya.cmds as mc
from LegoTool.LegoTool import LegoTool
import random

legoTool = LegoTool()

legoTool.deleteAll()
legoTool.initShaders()

# Base plate
mc.polyPlane(w=200, h=100)

# # Create foliage
for z in range(2):
    side = 1 if z == 0 else -1
    length = 250
    for i in range(length):
        for j in range(30):
            rand = random.uniform(0, 1)
            if rand > 0.94:
                legoTool.createLegoPlant()
                legoTool.moveLego(i - length/2, 0, side*(j + 10))
            if 0.100000000000000000 < rand < 0.102000000000000000:
                randomRot = random.uniform(0, 360)
                small = False
                height = int(random.uniform(5, 15))
                if randomRot > 270:
                    small = True
                    height = int(random.uniform(4, 7))
                legoTool.createLegoCactus(small=small, height=height)
                legoTool.moveLego(i - length/2, 0, side*(j + 10))

                mc.rotate(0, randomRot)

    # # Create fence
    legoTool.createFence(length=251)
    legoTool.moveLego(0, 1.6, side * 40)
    if side == -1:
        mc.rotate(90, 0, 180)
        pass

# userLength = int(input("Enter number of passenger cars"))
userLength = 3

legoTool.createTracks(20)
legoTool.moveLego(0, 0, 0)
mc.move(-80, 0, 0)

createCars = True

mainColors = ["yellow", "darkGreen", "blue"]
accentColors = ["red",  "yellow", "yellow"]
woodColors = ["brown",  "brown", "red"]

if createCars:
    legoTool.createSteamEngine()
    legoTool.moveLego(0, 4, 0)
    legoTool.createCoalCar(makeCoal=True)
    legoTool.moveLego(15, 4 - 2/3, 0)
    for i in range(userLength):
        legoTool.createPassengerCar(mainColorName=mainColors[i],
                                    accentColorName=accentColors[i],
                                    woodColorName=woodColors[i])
        legoTool.moveLego(35 + i * 22, 4 - 2/3, 0)

cars = mc.ls("*Car*")
engine = mc.ls("*Steam_Engine")
for car in engine:
    cars.append(car)

mc.select(cars)
mc.move(-20, 0, 0, r=True)
