
#prompt user for keywords file
def keywordsfile () :
    keywordsFileName = input(print("Please enter the name of the file with the keywords: "))
    try:
        openKeywordsFileName = open(keywordsFileName, "r")
    except IOError:
        print("File not found.")
        quit() #quit?
    for i in range (0, len(openKeywordsFileName) - 1):
        keyAndValList[i] = readLine(openKeywordsFileName).split(",")
        i = i + 1
    for k in range (0, len(keyAndValList)) - 1:
        keywordList[k] = str(keyAndValList[k])
        keyValList[k] = int(keyAndValList[k+1])

    keysJoined = []
    keysJoined.append(keywordList)
    
    return keywordList
    return keyValList

def fileExists() :
    #prompt user for file  name
    tweetsFileName = input(print("Please enter the name of the file with the tweets: "))
    #exception handling
    try:
        openTweetsFile = open(tweetsFileName, "r")
    except IOError:
        print("File not found.")
        quit() #CHECK
    return openTweetsFile

def splitTweets() :
    for line in openTweetsFile :








#defining variables
keywordsFileName = ""
openKeywordsFileName = ""
keyAndValList = []
keywordList = []
keyValList = []
openTweetsFile = ""
justTweets = []
tweetsWords = []




#main?
keywordsFile()


