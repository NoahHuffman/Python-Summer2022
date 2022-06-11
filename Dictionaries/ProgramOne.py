def main():
    infile = open("LargeCitiesDict.txt")
    LargeStateDict={}
    state = input("Enter a state: ")
    
    #Creating dictionary
    for line in infile:
        #Code Scrubbing
        line = line.replace("(","").replace(")","").replace("\n","").replace("'","").replace("[","").replace("]","").split(",")
        #Setting Keys and Values for dictionary
        LargeStateDict.update({line[0]: line[1:]})

    
    if state in LargeStateDict.keys():
        if len(LargeStateDict.get(state)) > 1:
            print("Large cities in",state.rstrip()+":",", ".join(LargeStateDict.get(state)))
        elif len(LargeStateDict.get(state)) == 1:
            print("Large city in",state.rstrip()+":",", ".join(LargeStateDict.get(state)))
        elif not LargeStateDict.get(state):
            print("No large cities, mate!")
    else:
        print("Invalid Input")

    infile.close()
main()