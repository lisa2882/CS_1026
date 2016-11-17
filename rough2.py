#is .strip(whatever) a thing??? or do you have to do lstrip and rstrip

#defining all variables
keywordsFileName = "" #name of the keywords file name inputted by user
keywordsFile = "" #keywords file
tweetsFileName = "" #name of the tweets file name inputted by the user
tweetsFile = "" #tweets file
lat = "" #latitude value of the tweet
long = "" #longitude value of the tweet
tweets = "" #the actual text from the tweets
pacTweCount = 0 #Number of tweets from the Pacific timezone
pacHappiness = 0 #Pacific timezone's happiness values
pacAvgHappiness = 0 #pacific timezone's average happiness
mouTweCount = 0 #Number of tweets from the mountain timezone
mouHappiness = 0 #mountain timezone's happiness values
mouAvgHappiness = 0 #mountain timezone's average happiness
cenTweCount = 0 #number of tweets from the central timezone
cenHappiness = 0 #central timezone's happiness values
cenAvgHappiness = 0 #central timezone's average happiness
easTweCount = 0 #number of tweets from the eastern timezone
easHappiness = 0 #eastern timezone's happiness values
easAvgHappiness = 0 #eastern timezone's average happiness


#defining all lists
wordsAndValsList = [] #list containing the keywords and values (each a separate index)
keywordsList = [] #list containing all the keywords (has the same index as keywordsVal list)
keywordValList = [] #list containing all of the keyword's values (has the same index as keywords list)
coordList = [] #list containing all of the coordinates (needs to have same indexes)
tweetsList = [] #list containing all of the tweets (needs to have same indexes)
happinessList = [] #list containing all of the happiness scores of each tweet (needs to have same indexes)
latList = [] #list containing the latitude values for tweets (needs to have same indexes)
lonList = [] #list containing the longitude values for tweets (needs to have same indexes)]
partHappinessList = [] #used in a for loop
finalHappinessList = []

#defining all constants for timezones
P_13579_LAT = 49.189787
P_246810_LAT = 24.660845
P_12_LON = -67.444574
P_34_LON = -87.518395
P_56_LON = -101.998892
P_78_LON = -115.236428
P_910_LON = -125.242264

#calculating the happiness score of each tweet
def happinessCalculate():
    for i in range (0, len(tweetsList)-1): #for all the tweets individually
        singleTweet = tweetsList[i]
        words = singleTweet.split()
        keyCount = 0 #counts the number of key words in the tweet
        avgHappiness = 0 #calculates the average happiness score for each tweet
        for element in words: #for each individual word
            if element in keywordsList: #for each word in a tweet
                keyCount = keyCount + 1 #number of keywords found in each tweet counter
                tweetsHappiness = tweetsHappiness + int(keywordValList[keywordsList.index()]) #each tweets sentiment value
                partHappinessList.append(tweetsHappiness)
        if keyCount == 0:
            avgHappiness = 0
        else:
            avgHappiness = sum(partHappinessList) / keyCount
        happinessList.append(avgHappiness)
    return happinessList

def happinessScore(happiness,numTweets):
    #happiness score - is it divided by the total number of tweets or the number of tweets from that timezone
    return round(happiness/numTweets, 2)

#main()

#Obtaining the keywords file and checking to make sure that it exists
try:
    keywordsFileName = input(print("Enter the name of the file containing the keywords: "))
    keywordsFile = open(keywordsFileName, "r", encoding="utf-8")
except IOError:
    print("Error: file does not exist.")
    quit()

#inserting the keywords and their values into lists
for line in keywordsFile:
    line.rstrip()
    keywordsSplit = line.split(",")
    keywordsSplit[1] = int(keywordsSplit[1])
    keywordsList.append(keywordsSplit[0])
    keywordValList.append(keywordsSplit[1])

#obtaining the tweets file and checking to make sure that it exists
try:
    tweetsFileName = input(print("Enter the name of the file containing the tweets: "))
    tweetsFile = open(tweetsFileName, "r", encoding="utf-8")
except IOError:
    print("Error: file does not exist.")
    quit()

#getting the tweets and lat and long
for line in tweetsFile:
    line.rstrip()
    splitAll = line.split("]") #splitAll = a whole line from the tweets file
    #getting the coordinates from the tweets
    coord = splitAll[0]
    coord.strip(" [ ]") #stripping the square brackets and space
    coordList.append(coord)
    #getting the actual text from the tweets
    noncord = splitAll[1]
    noncord = noncord.lstrip()
    noncord = noncord.rstrip()
    noncord.split(" ", 3)
    tweets = noncord[3]
    tweets.lstrip(".!#\",")
    tweets.rstrip(".!#\",")
    tweetsList.append(tweets)

finalHappinessList = happinessCalculate()
#maybe the first for loop below as a function?
#getting the coordinates and zones
for coordinate in coordList: #splitting each coordinate into latitude and longitude
    coordinate.lstrip()
    coordinate.strip("[ ]")
    latLon = coordinate.split(",")
    latList.append(float(latLon[0]).lstrip("["))
    lonList.append(float(latLon[1].rstrip("]")))
for i in range (0, len(coordList)-1): #for each coordinate pair
    if (latList[i] > P_13579_LAT or latList[i] < P_246810_LAT or lonList[i] > P_12_LON or lonList[i] < P_910_LON or
        finalHappinessList[i] == 0): #not in a zone or no keywords
        #need to remove that tweet and everything else that depends on that index
        tweetsList.pop(i)
        coordList.pop(i)
        finalHappinessList.pop(i)
        latList.pop(i)
        lonList.pop(i)
    elif lonList[i] >= P_910_LON and lonList[i] <= P_78_LON: #Pacific
        pacTweCount = pacTweCount + 1
        pacHappiness = pacHappiness + finalHappinessList[i]
    elif lonList[i] > P_78_LON and lonList[i] <= P_56_LON: #Mountain
        mouTweCount = mouTweCount + 1
        mouHappiness = mouHappiness + finalHappinessList[i]
    elif lonList[i] > P_56_LON and lonList[i] <= P_34_LON: #Central
        cenTweCount = cenTweCount + 1
        cenHappiness = cenHappiness + finalHappinessList[i]
    elif lonList[i] > P_34_LON and lonList[i] <= P_12_LON: #Eastern
        easTweCount = easTweCount + 1
        easHappiness = easHappiness + finalHappinessList[i]

finalPacificHappinessScore = happinessScore(pacHappiness, pacTweCount)
finalMountainHappinessScore = happinessScore(mouHappiness, mouTweCount)
finalCentralHappinessScore = happinessScore(cenHappiness, cenTweCount)
finalEasternHappinessScore = happinessScore(easHappiness, easTweCount)

print("The happiness score for the following timezones are: ")
print("Pacific Time Zone: " + finalPacificHappinessScore + " with " + pacTweCount + " tweets.")
print("Mountain Time Zone: " + finalMountainHappinessScore + " with " + mouTweCount + " tweets.")
print("Central Time Zone: " + finalCentralHappinessScore + " with " + cenTweCount + " tweets.")
print("Eastern Time Zone: " + finalEasternHappinessScore + " with " + easTweCount + " tweets.")

