import maya.cmds as mc 

winName = "Test"

def createWindow():
    if mc.window(winName, exists=True):
        mc.deleteUI(winName)
    mc.window(winName)
    mc.showWindow(winName)
    cmds.setParent("..")
    
    cmds.button(label="Close", command=('cmds.deleteUI(\"' + window + '\", window=True)') )

createWindow()
