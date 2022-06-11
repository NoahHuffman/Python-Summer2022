import random

#Class to mimick a singular die
class Die:
    def __init__(self,value):
        self.value = value     
        
def main():
    totalDoubleSixes = 0
    totalTrials = 0

    #Loop to get the frequency of the particular pair
    while totalTrials < 10000:
        numTrials = 0
        doubleSixes = 0
        totalTrials += 1
        while numTrials < 24:
            numTrials += 1
            die1 = Die(random.randint(1,6))
            die2 = Die(random.randint(1,6))
            if die1.value == 6 and die2.value == 6:
                doubleSixes +=1
                break
        if doubleSixes > 0:
            totalDoubleSixes += 1
        else:
            continue

    probability = (totalDoubleSixes / totalTrials)
    print(probability) 

main()