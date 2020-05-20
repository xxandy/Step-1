## make anagram be word

## ALEXREVIEW - I would like to have the algorithm explained during our chat

originDict = []
with open('dictionary.txt', 'r') as f:
    for line in f:
        originDict.append(line.strip('\n').upper())

TestCase = ['CDRA', 'ABAY', 'DOTG', 'CCOW', 'UDNBREA', '', 'apple']
targetDict = {}

for x in originDict:
    ## ALEXREVIEW - next 3 lines repeat later in the program.  Could it be a reusable function?
    sample = [0] * 26
    for y in x:
        sample[ord(y) - ord('A')] += 1
    k = ''.join(list(map(str, sample)))
    if k not in targetDict:
        targetDict[k] = [x]
    else:
        targetDict[k].append(x)


def judge(test, tar):
    ## ALEXREVIEW: it would be better not to use globals, and instead collaborate with the caller
    ##              by returning a value, and letting the caller assemble res.
    ##              It is especially not recommended to declare a global within an inner function.
    global res
    for i in range(26):
        if test[i] < tar[i]:
            return
    res += targetDict[tar]


for x in TestCase:
    x = x.upper()
    res = []
    sample = [0] * 26
    for y in x:
        sample[ord(y) - ord('A')] += 1
    k = ''.join(list(map(str, sample)))
    for tar in targetDict:
        judge(k, tar)

    print(res)
