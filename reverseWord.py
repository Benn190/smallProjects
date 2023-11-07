#program which takes a string from the command line input and reverses its characters

userWord = input("Enter a string..")

reversedWord = ""
for l in range(0, len(userWord)):
    reversedWord = userWord[l] + reversedWord
print(reversedWord)