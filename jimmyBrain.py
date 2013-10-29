from myro import *
def fun():
    count = 0
    initialize("COM3")
    while (count < 1):
        temp = returnMostCommonObstacle(10, 130)
        print 'TEMP: ' + str(temp)
        while (temp < 300):
            forward(1, 1)
            temp = returnMostCommonObstacle(10, 130)
            print 'TEMP: ' + str(temp)

        while (temp < 1000):
            forward(1, 0.5)
            temp = returnMostCommonObstacle(10, 130)
            print 'TEMP: ' + str(temp)

        turnAndGo()

        
