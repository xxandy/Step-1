originDict = []
with open('dictionary.txt','r') as f:
    for line in f:
        originDict.append(line.strip('\n').upper())

valueForLetter = [1,1,2,1,1,2,1,2,1,3,3,2,2,1,1,2,3,1,1,1,1,2,2,3,2,3]


def toHash(x):
    sample = [0] * 26
    i = 0
    while i < len(x):
        if x[i] == 'Q':
            sample[ord(x[i]) - ord('A')] += 1
            i += 2
        else:
            sample[ord(x[i]) - ord('A')] += 1
            i += 1
    return ''.join(list(map(str, sample)))


hashToWord = {}

for x in originDict:
    hashToWord[toHash(x)] = x


def judge(test,inDict):
    for i in range(26):
        if inDict[i] > test[i]:
            return False
    return True


def hashToValue(x):
    res = 0
    for i in range(26):
        res += int(x[i]) * valueForLetter[i]
    return res


givenLetter = str(input('Please give 16 letters:'))
nowMax = [0,'']

test = toHash(givenLetter)

for word in hashToWord:
    if judge(test,word):
        if hashToValue(word) > nowMax[0]:
            nowMax = [hashToValue(word),hashToWord[word]]

print(nowMax)
