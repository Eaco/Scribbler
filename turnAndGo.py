def turnAndGo():
        turnLeft(-0.79, 1)
        temp = returnMostCommonObstacle(10, 130)
        if (temp <= 1000):         #this checks if the most common is zero and drives forward if nothing is in front of it
            forward(1,1.75)
            turnLeft(0.79, 1)
       # elif(temp > 1000):
        #    turnRight(1.58, 1)
         #   forward
        
