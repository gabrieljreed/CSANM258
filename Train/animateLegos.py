import maya.cmds as mc
from LegoTool.LegoTool import LegoTool
import random

legoTool = LegoTool()

legoTool.deleteAll()

tracks = legoTool.createTracks(length=10)

# startTime = mc.playbackOptions(q=True, minTime=True)
# endTime = mc.playbackOptions(q=True, maxTime=True)

startTime = 0

for brick in mc.listRelatives(tracks, c=True):
    targetPos = mc.getAttr(brick+".translateY")
    influence = mc.getAttr(brick+".translateX") + 20 + mc.getAttr(brick+".translateY")
    influence *= 0.5
    mc.setKeyframe(brick, time=startTime, attribute="translateY", value=(targetPos + 4) * 100)
    mc.setKeyframe(brick, time=startTime + influence, attribute="translateY", value=targetPos)


engine = legoTool.createSteamEngine()
legoTool.moveLego(20, 4, 0)

startTime = 10

for brick in mc.listRelatives(engine, c=True):
    targetPos = mc.getAttr(brick + ".translateY")
    influence = mc.getAttr(brick + ".translateX") + 15 + mc.getAttr(brick + ".translateY") + 10
    influence *= 3
    mc.setKeyframe(brick, time=startTime, attribute="translateY", value=(targetPos + 10)*100)
    mc.setKeyframe(brick, time=startTime + influence, attribute="translateY", value=targetPos)


coalCar = legoTool.createCoalCar(makeCoal=False)
legoTool.moveLego(35, 4 - 2/3, 0)

startTime = 40

for brick in mc.listRelatives(coalCar, c=True):
    targetPos = mc.getAttr(brick + ".translateY")
    influence = mc.getAttr(brick + ".translateX") + 15 + mc.getAttr(brick + ".translateY") + 10
    influence *= 3
    mc.setKeyframe(brick, time=startTime, attribute="translateY", value=(targetPos + 10)*100)
    mc.setKeyframe(brick, time=startTime + influence, attribute="translateY", value=targetPos)


for i in range(1):
    passengerCar = legoTool.createPassengerCar()
    legoTool.moveLego(57 + 22 * i, 4 - 2/3, 0)

    startTime = 70 + 30 * i

    for brick in mc.listRelatives(passengerCar, c=True):
        targetPos = mc.getAttr(brick + ".translateY")
        influence = mc.getAttr(brick + ".translateX") + 15 + mc.getAttr(brick + ".translateY") + 10
        influence *= 3
        mc.setKeyframe(brick, time=startTime, attribute="translateY", value=(targetPos + 10)*100)
        mc.setKeyframe(brick, time=startTime + influence, attribute="translateY", value=targetPos)
