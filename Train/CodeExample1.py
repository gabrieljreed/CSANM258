import maya.cmds as mc

mc.select(all=True)
mc.delete()

# Declaring variables
num1 = 2
num2 = 5
num3 = 10
# Adding them together and printing them out (total = 17)
total = num1 + num2 + num3
print("First total")
print(total)
# Declaring and printing more variables (total first time will be same, then will be 25)
num2 = 8
stringToPrint = "Next total"
print(stringToPrint)
print(total)
total = total + num2
print("Now total = " + str(total))

# Declaring list and accessing elements in it
numList = [2, 4, 6, 8]
print(numList[0])
print(numList[3])
product = numList[0] * numList[1]
anotherStringToPrint = "The current product is " + str(product)
print(anotherStringToPrint)
product = product * numList[2]
product = product * numList[3]
print("Product = " + str(product))

# Declaring paycheck variables, adding them together
paycheck1 = 280.79
paycheck2 = 590
bankAmount = paycheck1 + paycheck2  # this is how many dollars is in your bank account!
paycheck1 = 0
paycheck2 = 0
print("There are " + str(bankAmount) + " dollars in your bank account")
# Even though you zero them out, your $money$ is already secured

# MY CODE TO ASK USER FOR MORE MONAYYY
newPaycheck = input("How much money would you like to deposit?")
bankAmount = bankAmount + float(newPaycheck)
print("\nYour new balance is {}".format(bankAmount))

######################
somelist = [3, 5, 3.2, 98, "bob", 45]  # Declare list
somelist.append(35)  # Append bob to list
print(somelist)  # Print list

#####################
myspheres = []
for vari in range(10):
    # print(vari)
    baseSphere = mc.polySphere(sx=20.4, r=1, sy=20, ax=[0, 1, 0], cuv=2, ch=1)  # Creates sphere
    myspheres.append(baseSphere[0])  # Adds sphere to myspheres
    print(baseSphere)  # Prints info about the sphere
    mc.move(vari, 0, 0, r=True)  # Moves the sphere a relative amount based on the increasing iterator "vari"
print(myspheres)  # Prints all info about the spheres

#####################################
import maya.cmds as mc
import random

cylHeight = int(input())  # Input to get height of the cylinders
myListOfRotValues = range(0, 360, 20)  # Uses the range function to get a list of ranges separated by 20 degrees
print(myListOfRotValues)  # Prints list
spokeObjectNames = []  # Declare empty list
for curCyl in myListOfRotValues:  # For loop going through list of rot values
    curSpoke = mc.polyCylinder(r=0.1, h=cylHeight)  # Creates new cylinder
    spokeObjectNames.append(curSpoke[0])  # Append name to spokeObjectNames
    mc.move(0, cylHeight / 2.0 + 1, 0)  # Move cylinder so bottom is on origin
    mc.move(0, 0, 0, curSpoke[0] + ".scalePivot", curSpoke[0] + ".rotatePivot")
    randRot = random.uniform(0, 360)  # Random value 0..360
    mc.rotate(randRot, 0, 0)  # Performs rotation

print(spokeObjectNames)  # Prints object names
mc.group(spokeObjectNames)  # Groups all objects
