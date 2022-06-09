def main():

    infile = open("Justices.txt")
    outfile = open("JusticesbyPres.txt","w")
    sortedPresList = []
    presList = []
    contentList = []
    freqDict = {}

    #Creating list of file contents
    for line in infile:
        contentList.append(line.split(","))
    
    #Creating a seperate list for the presidents 
    for line in contentList:        
        presidents = line[2]
        presList.append(presidents)

    #Sorting the list of presidents based on their last name
    for el in presList:
        #Splitting the full names so we can access the last name
        el = str(el).split()
        sortedPresList.append(el)
    sortedPresList = sorted(sortedPresList, key=lambda x:x[-1])        

    #Creating frequency dictionary based off how many times each president's name is repeated in the list
    for president in sortedPresList:
        #Re-joining the previously split strings
        president = " ".join(president)
        if president in freqDict:
            freqDict[president] += 1
        else:
            freqDict[president] = 1
    
    #Formatting the output
    for element in freqDict.items():
        element = str(element).replace(",",":").replace("'","").replace("(","").replace(")","")
        #Writing output to new file
        outfile.write(element+"\n")

    infile.close()
    outfile.close()
main()