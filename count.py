string1 = input("enter string1    ")
charactercount = 0
wordcount = 1
for i in string1:
    charactercount = charactercount + 1
    if (i == ' '):
        wordcount = wordcount + 1
print("charactercount")
print(charactercount)
print("wordcount")
print(wordcount)

