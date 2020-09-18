# Import
from textblob import TextBlob  # ForAnalyzingGrammarInData
import sys
import tweepy  # ForAuthentication
import matplotlib.pyplot as plt  # ForPlottingPieChart


def percentage(part, whole):
    return 100 * float(part) / float(whole)


# PasscodesForAuthentication
consumerKey = "cr0k2zYgkAr77RtGOcRK2kUOe"
consumerSecret = "0aTEXzAdJxKY3ynDisMRdjhvFFr3Sz6YGURcHoXLVSNJYJib7m"
accessToken = "1158303446769868800-j9xvSvwUF45kEhJ4pLl2VCLV0neLUw"
accessTokenSecret = "KLe5dd153149H9nP6XFDXS0T9oGZl4WGMd8Qm4PCPaWEX"
auth = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

# UsingTextBlobForAuthentication
searchTerm = input("Enter hashtag to search:")
tweets = api.search(searchTerm)

print("Total tweets extracted :- " + str(len(tweets)))
numberofSeachTerms = int(input("How many tweets to analyze?"))

# GetData
positive = 0.00
negative = 0.00
mixed = 0.00
polarity = 0.00

# DefineSegregation
for i in range(0, numberofSeachTerms):
    print(tweets[i].text)  # PrintingRecievedData
    analysis = TextBlob(tweets[i].text)  # DeclareLoopConditions
    polarity += analysis.sentiment.polarity
    if analysis.sentiment.polarity == 0.00:
        mixed += 1
    elif analysis.sentiment.polarity < 0.00:
        negative += 1
    elif analysis.sentiment.polarity > 0.00:
        positive += 1

# CallingPercentageFunction
positive = percentage(positive, numberofSeachTerms)
negative = percentage(negative, numberofSeachTerms)
mixed = percentage(mixed, numberofSeachTerms)
polarity = percentage(polarity, numberofSeachTerms)

# ConvertingToFloatVals
positive = format(positive, ".2f")
negative = format(negative, ".2f")
mixed = format(mixed, ".2f")

if polarity == 0:
    reaction = "Mixed Views"
elif polarity < 0.00:
    reaction = "Negatively"
elif polarity > 0.00:
    reaction = "Positively"

print("People are reacting " + reaction + " on " + searchTerm)

# LoopInTextBlob
labels = [
    "Positive[" + str(positive) + "%]",
    "Mixed Views[" + str(mixed) + "%]",
    "Negative[" + str(negative) + "%]",
]
sizes = [positive, mixed, negative]
colors = ["pink", "lightgreen", "lightblue"]
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title("People are reacting " + reaction + " on " + searchTerm)
plt.axis("equal")
plt.tight_layout()
plt.show()
# PlottingThePieChart
