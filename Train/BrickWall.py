import maya.cmds as mc
import random

mc.select(all=True)
mc.delete()

names = []
for j in range(4):
    for i in range(10):
        cube = mc.polyCube()
        names.append(cube[0])
        mc.scale(2, 1, 1)
        mc.polyBevel(o=0.05)
        z = random.uniform(0, 0.1)
        mc.move(2*i + j%2, j, z)
        mc.rotate(0, z*50 * ((z*100)%2-1), 0)

    cube = mc.polyCube()
    names.append(cube[0])
    mc.polyBevel(o=0.05)
    z = random.uniform(0, 0.1)
    mc.move(0, 0, z)
    mc.rotate(0, z * 50 * ((z * 100) % 2 - 1), 0)
    if j % 2:
        mc.move(-0.5, j, 0)
    else:
        mc.move(19.5, j, 0)


wall = mc.group(names)
mc.move(-10, 0, 0)
