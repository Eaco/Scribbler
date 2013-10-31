from myro import *
def fun():
    count = 0
    direction = 1
    whereAmIX = 0
    whereAmIY = 0
    initialize("COM3")
    while (count < 1):
        temp = returnMostCommonObstacle(10, 130)
        print 'TEMP: ' + str(temp)
        while (temp < 300):
            while (whereAmIX > 0):         #if jimmy is not on it's original x
                forward(1,2);
                whereAmIY += 2
                turnLeft(.79, 1)        #he turns to the left
                temp = returnMostCommonObstacle(10, 130)    #checks if there is somthing in front of him
                while (temp > 1000):
                    turnRight(.79, 1)   #if there is something in front of him turns back to right
                    forward(1,1)        #goes forward
                    turnLeft(.79, 1)    #turns left again
                    temp = returnMostCommonObstacle() #checks the obstacle again
                while (whereAmIX != 0 and temp < 1000):
                    forward(1,1)
                    whereAmIX -= 1
                    temp = returnMostCommonObstacle(10, 130)
                print 'done yo'
                turnRight(.79, 1)
                    
                
            whereAmIY += 1
            forward(1, 1)
            temp = returnMostCommonObstacle(10, 130)
            print 'TEMP: ' + str(temp)
            print 'position in y' + str(whereAmIY)

        while (temp < 1000):
            whereAmIY += 0.5
            forward(1, 0.5)
            temp = returnMostCommonObstacle(10, 130)
            print 'TEMP: ' + str(temp)
            print 'position ' + str(whereAmIY) + str(whereAmIX)

        while (temp > 1000):
            turnAndGo()
            whereAmIX += 2
            temp = returnMostCommonObstacle(10, 130)

        
        
