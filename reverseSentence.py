# program which takes a sentence (a string with spaces) and reverses each word, while
# keeping the ordering of the words the same

userInput = input("Enter a sentence..")

currWord = "" # hold current word
reversedWords = [] #contains a list of the reversed words collected

for l in range(0, len(userInput)):
    # space means new word, so add current word to list then delete it
    if userInput[l] == " ":
        reversedWords.append(currWord)
        currWord = ""
    # case for last character in string
    elif l == len(userInput)-1:
        currWord = userInput[l] + currWord
        reversedWords.append(currWord)
    # case for consecutive characters to be added onto existing current word
    else:
        currWord = userInput[l] + currWord

#print from reversed list
for word in reversedWords:
    print(word, end=" ")