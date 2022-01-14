mc.select(all=True)
mc.delete()

success = False
while not success:
    success = True
    userInput = input("What kind of shape would you like to create?")
    if userInput == "sphere":
        mc.polySphere()
    elif userInput == "box":
        mc.polyCube()
    elif userInput == "cone":
        mc.polyCone()
    else:
        print("Incorrect input! Please try again!")
        success = False
