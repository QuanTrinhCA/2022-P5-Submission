import math

inputs = input().split()

angleofsun = 90 + ((220.8 - 90) / 7) * (int(inputs[0]) - 8)

numberofstep = round(float(inputs[2]) * 1000)

angle = angleofsun + int(inputs[1])

while angle > 360:
    angle -= 360

if 0 < (angle) < 90:
    east = round(math.sin(math.radians(angle)) * numberofstep)
    north = round(math.cos(math.radians(angle)) * numberofstep)
    print("East " + str(east) + " North " + str(north))
elif angle == 90:
    print("East " + str(numberofstep) + " North 0")
elif 90 < (angle) < 180:
    tempangle = angle - 90
    south = round(math.sin(math.radians(tempangle)) * numberofstep)
    east = round(math.cos(math.radians(tempangle)) * numberofstep)
    print("East " + str(east) + " South " + str(south))
    if south == 0:
        print("East " + str(east) + " South 0")
    if east == 0:
        print("East 0 North " + str(south))
elif angle == 180:
    print("East 0" + " South " + str(numberofstep))
elif 180 < (angle) < 270:
    tempangle = angle - 180
    west = round(math.sin(math.radians(tempangle)) * numberofstep)
    south = round(math.cos(math.radians(tempangle)) * numberofstep)
    if south == 0:
        print("West " + str(west) + " South 0")
    if west == 0:
        print("West 0 South " + str(south))
    print("West " + str(west) + " South " + str(south))
elif angle == 270:
    print("West " + str(numberofstep) + " North 0")
elif 270 < (angle) < 360:
    tempangle = angle - 270
    north = round(math.sin(math.radians(tempangle)) * numberofstep)
    west = round(math.cos(math.radians(tempangle)) * numberofstep)
    if north == 0:
        print("West " + str(west) + " North 0")
    if west == 0:
        print("West 0 North " + str(north))
elif angle == 0:
    print("East 0" + " North " + str(numberofstep))