##--- Real-Time Situation Analysis Sim ---##
##----Missile Launcher (Hit o Miss)----##

import random
import time

def RTsim(x):
    start = time.monotonic() #timer to count the time of whole function
    cityLimitsNS = range(10,21) #the latitude range of the city (10 integers long)
    cityLimitsEW = range(10,21) #the longitude range of the city
    num, numHits = 0, 0 
    while num < x : #function will run a 'x' number of times
        print('__________________________________________________________________') #aesthically pleasing
        print()
        launchTimeBegins = time.monotonic() #timer to count the time of each calculation, itself 
        num += 1 
        NS = random.randint(-50,50) #postive will be north, negative south ### this randomness is to simulate RT situations, since I'll will not be measuring outside situations as of now
        EW = random.randint(-50,50) #postive will be east, negative west
        ## Below is to print the cardinal direction of missile landing
        if NS >= 0 and EW >= 0:
            print( str(NS) + "N " + str(EW) + "E")
        elif NS >= 0 and EW < 0:
            print( str(NS) + "N " + str(abs(EW)) + "W")
        elif NS < 0 and EW >= 0:
            print( str(abs(NS)) + "S " + str(EW) + "E")
        else:
            print( str(abs(NS)) + "S " + str(abs(EW)) + "W")

        ## Below is to state if missile hit or missed
        if NS in cityLimitsNS and EW in cityLimitsEW:
            print("HIT")
            numHits += 1
        else:
            print("MISS")
        
        launchTimeEnds = time.monotonic()
        print ("Check " + str(num) + ": " + str(launchTimeEnds - launchTimeBegins) + " Function Time")

    end = time.monotonic()
    print( str(end - start) + " Whole Time")
    print("Number of Hits: " + str(numHits))


RTsim(100)
