def getObstacleArray(maxIt = 100, power = 135, returnArray = 'center'):
    setIRPower(power)
    counter = 0
    arrayOfLeftValue = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfCenterValue = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    arrayOfRightValue = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    while counter < maxIt:
        temp = getObstacle()
        print str(temp[0]) + " "*(5-len(str(temp[0]))) + str(temp[1]) + " "*(5-len(str(temp[1]))) + str(temp[2])
        arrayOfLeftValue[temp[0]/100] += 1
        arrayOfCenterValue[temp[1]/100] += 1
        arrayOfRightValue[temp[2]/100] += 1
        counter += 1
    if returnArray == 'center':
        return arrayOfCenterValue
    elif returnArray == 'left':
        return arrayOfLeftValue
    elif returnArray == 'right':
        return arrayOfRightValue
    elif returnArray == 'all':
        return [arrayOfLeftValue, arrayOfCenterValue, arrayOfRightValue]

def printObstacle(maxIt = 100, power = 135, printArray = 'center'):
    arrayOfValues = getObstacleArray(maxIt, power, printArray) #NOTE DO NOT PASS IN ALL
    print "/n/n"
    counter = 0
    while counter < len(arrayOfValues):
        print str(counter*100) + "-" + str((counter + 1)*100 - 1) + ": " + str(arrayOfValue[counter])
        counter += 1

def returnMostCommonObstacle(maxIt = 100, power = 135, printArray = 'all'):
    arrayOfValues = getObstacleArray(maxIt, power, printArray)

    if printArray == 'left':             #Converts the one dimensional array to a 
        arrayOfValues = [arrayOfValues] #3 dimensional array with the original
        arrayOfValues.append([0])       #array at the new array[1]
        arrayOfValues.append([0])

    counter = 0
    highestValueLeftIndex = 0
    while counter < len(arrayOfValues[0]):
        if arrayOfValues[0][counter] > arrayOfValues[0][highestValueLeftIndex]:
            highestValueLeftIndex = counter
        counter += 1

    highestValueLeftIndex *=100
        
    if printArray == 'left':
        return highestValueLeftIndex

    if printArray == 'center':          #Converts the one dimensional array to a 
        arrayOfValues = [arrayOfValues] #3 dimensional array with the original
        arrayOfValues.append([0])       #array at the new array[1]
        arrayOfValues.append([0])
        arrayOfValues[1] = arrayOfValues[0]
        arrayOfValues[0] = [0]

    counter = 0
    highestValueCenterIndex = 0
    while counter < len(arrayOfValues[1]):
        if arrayOfValues[1][counter] > arrayOfValues[1][highestValueCenterIndex]:
            highestValueCenterIndex = counter
        counter += 1

    highestValueCenterIndex *=100

    if printArray == 'center':
        return highestValueCenterIndex

    if printArray == 'right':           #Converts the one dimensional array to a 
        arrayOfValues = [arrayOfValues] #3 dimensional array with the original
        arrayOfValues.append([0])       #array at the new array[2]
        arrayOfValues.append([0])
        arrayOfValues[2] = arrayOfValues[0]
        arrayOfValues[0] = [0]

    counter = 0
    highestValueRightIndex = 0
    while counter < len(arrayOfValues[2]):
        if arrayOfValues[2][counter] > arrayOfValues[2][highestValueRightIndex]:
            highestValueRightIndex = counter
        counter += 1

    highestValueRightIndex *=100

    if printArray == 'right':
        return highestValueRightIndex

    return highestValueLeftIndex + highestValueCenterIndex + highestValueRightIndex

    

def printIR(maxIt = 100):
    counter = 0
    while counter < maxIt:
        temp = getIR()
        print temp
        counter += 1

#printObstacle(20)
#returnObstacle(20)
#printIR(1000)
