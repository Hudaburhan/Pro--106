def greet(name):
    print("Hey! "+name+" how are you")

def countWordsFromFile():
    filename = input("Enter File name ")
    wordCount=0
    file= open(filename,'r')
    for line in file:
        words= line.split()
        wordCount= wordCount+len(words)
        # print(words)     
    print(wordCount)  

countWordsFromFile()
greet("Huda")