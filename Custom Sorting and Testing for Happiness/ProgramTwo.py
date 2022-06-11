
file = open("sentences.txt","r")
list = []

#Creating list with each line of content
for w in file:
    list.append(w.strip())        

#Sorting the list in terms of length
list.sort(key=len)

#Printing new sorted list one line at a time :)
for string in list:
    print(string)

file.close()