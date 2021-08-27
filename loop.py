count =7
while(count>0):
    print(count)
    count=count-1
    
sentence = input("What's your favorite food: ")
wordCount=1
characterCount=0
for i in sentence:
    characterCount=characterCount+1
    if(i==' '):
        wordCount=wordCount+1

print("number of Characters are: ")
print(characterCount)
print("number of Words are: ")
print(wordCount)