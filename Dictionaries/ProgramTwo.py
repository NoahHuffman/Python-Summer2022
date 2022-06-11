def main():


    file = input("Enter the name of the file (case sensitive): ")
    infile = open(file,"r")
    list = []
    freqDict = {}

    #reading each line    
    for line in infile:   
        #reading each word        
        for word in line.split():   
            #scrubbing content          
            word = word.replace(".","").replace(",","").replace(".","").replace(":","").replace("'","").lower()
            list.append(word.rstrip())
        list.sort()
 #       print(list)

    for i in list:
        if i in freqDict:
            freqDict[i] += 1
        else:
            freqDict[i] = 1

#    print(freqDict)

    for key, value in freqDict.items():
        print(str(key).rstrip() + ":", "(" +str(value)+")")


        

main()