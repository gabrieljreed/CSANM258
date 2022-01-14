import maya.cmds as mc
import random

mc.select(all=True)
mc.delete()

# Track
mc.polyCube(w=30, h=1, d=0.3)
mc.move(0, 0.5, -1.8)
mc.polyCube(w=30, h=1, d=0.3)
mc.move(0, 0.5, 1.8)

for i in range(4):
    mc.polyCube(w=30, h=0.2, d=0.2)
    pos = i % 2
    side = 1 - (i >= 2) * 2
    mc.move(0, 0.1 + 0.8 * pos, 2 * side)  # There has to be a better way to write this

# Slats
for i in range(10):
    slat = []
    # Slats
    scale = 6 + random.uniform(-0.1, 0.5)
    cube = mc.polyCube(w=1, h=0.1, d=scale)
    mc.polyBevel(o=0.02)
    mc.move(i * 3 - 15, 0, 0)
    slat.append(cube[0])

    # Bolt plates
    for j in range(2):
        side = 1 - j * 2  # Determines what side of the track the plate should appear on
        cube = mc.polyCube(w=0.9, h=0.1, d=0.6)
        mc.polyBevel(o=0.02)
        mc.move(i * 3 - 15, 0.1, 2.4 * side)
        slat.append(cube[0])

    # Bolts
    for j in range(4):
        sphere = mc.polySphere(r=0.1)
        pos = 1 - (j % 2) * 2  # Determines the up or down position of the bolt
        side = 1 - (j >= 2) * 2
        mc.move(i * 3 - (15 + 0.2 * pos), 0.1, 2.4 * side)
        slat.append(sphere[0])

    # Random rotation
    mc.group(slat)
    rot = random.uniform(0, 0.2)
    mc.rotate(0, rot * 50 * ((rot * 100) % 2 - 1), 0)
