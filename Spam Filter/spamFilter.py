import numpy as np
import pandas as pd
from collections import defaultdict
import string

df = pd.read_csv("spam ham data set.csv",encoding='latin-1')
df.dropna(axis=1, inplace=True)
trainSet = df[:3900]
testSet = df[3900:]
testSet.reset_index(inplace=True,drop=True)

spamCount = 0
hamCount = 0
totalCount =  0
spamDict = defaultdict(int)
hamDict = defaultdict(int)
for index,row in trainSet.iterrows():
    totalCount+=1
    wordList = str(row['v2']).split()
    wordList = [(word.translate(str.maketrans('', '', string.punctuation))).lower() for word in wordList]
    wordList = [word for word in wordList if word != '']
    if str(row['v1'])=='spam':
        spamCount+=1
        addInDict = spamDict
    else:
        hamCount+=1
        addInDict = hamDict
    for word in wordList:
        addInDict[word] = addInDict[word]+1

pSpam = spamCount/totalCount
pHam = hamCount/totalCount
alpha = 1
k = 2
pWordSpamDict = {}
pWordHamDict = {}
for key in spamDict:
    pWordSpamDict[key] = (spamDict[key] + alpha)/(spamCount + (alpha*k))
for key in hamDict:
    pWordHamDict[key] = (hamDict[key] + alpha)/(hamCount + (alpha*k))

def spamProb(wordList):
    wordSpamProb = []
    for word in wordList:
        if word in pWordSpamDict:
            wordSpamProb.append(pWordSpamDict[word])
        else:
            p = (0 + alpha)/(spamCount + (alpha*k))
            wordSpamProb.append(p)
    prob = pSpam
    for item in wordSpamProb:
        prob*=item
    return prob

def hamProb(wordList):
    wordHamProb = []
    for word in wordList:
        if word in pWordHamDict:
            wordHamProb.append(pWordHamDict[word])
        else:
            p = (0 + alpha)/(hamCount + (alpha*k))
            wordHamProb.append(p)
    prob = pHam
    for item in wordHamProb:
        prob*=item
    return prob

actual = np.zeros(len(testSet.index), dtype=int)
predicted = np.zeros(len(testSet.index), dtype=int)
for index, row in testSet.iterrows():
    if str(row['v1'])=='spam':
        actual[index] = 1
    else:
        actual[index] = 0
    
    mail = str(row['v2'])
    wordList = str(mail).split()
    wordList = [(word.translate(str.maketrans('', '', string.punctuation))).lower() for word in wordList]
    wordList = [word for word in wordList if word != '']
    
    pSpamMail = spamProb(wordList)
    pHamMail = hamProb(wordList)
    
    if pSpamMail > pHamMail:
        predicted[index] = 1
    else:
        predicted[index] = 0
        
print('Total Test Mails : ' + str(len(testSet.index)))
print('Classified correctly : ' + str(np.sum(actual == predicted)))
print('Accuracy : ' + str(((np.sum(actual == predicted))/(len(testSet.index)))*100))