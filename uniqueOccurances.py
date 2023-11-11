# program to count the frequency of each unique element in a list

# empty list which will store the elements from command line input
numList = []

# number of elements in list
n = int(input("Enter number of elements: "))

# collect each element
for i in range(0, n):
    item = int(input("Enter an integer: "))
    numList.append(item)

# dictionary to store occurances of each list item
frequencyDict = {}

# loop through list. Increment value in dictory if already in dictionary
for item in numList:
    if item in frequencyDict:
        frequencyDict[item] = frequencyDict.get(item, 0) + 1
    else:
        frequencyDict[item] = 1
        
print(frequencyDict)