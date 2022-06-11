file = open("nums.txt","r")

#Function to test whether or not a number is :) or :(
def testHappiness(num):
    list = []
    while num != 1:
        num = sum(int(i)**2 for i in str(num)) 
        if num in list:
            return False
        list.append(num)
    return True



#Calling the function and outputting the results :)
for w in file:
        w = int(w)
        testHappiness(w)
        if testHappiness(w) is True:
            print(str(w).strip(),"is happy.")
        else:
            print(str(w).strip(),"is not happy.")

file.close()

