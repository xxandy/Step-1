originDict = []
with open('dictionary.txt', 'r') as f:
    for line in f:
        originDict.append(line.strip('\n').upper())

TestCase = ['CDRA', 'ABAY', 'DOTG', 'CCOW', 'UDNBREA', '']
targetDict = {}

for x in originDict:
    sample = [0] * 26
    for y in x:
        sample[ord(y) - ord('A')] += 1
    k = ''.join(list(map(str, sample)))
    if k not in targetDict:
        targetDict[k] = [x]
    else:
        targetDict[k].append(x)


def judge(test, tar):
    global res
    for i in range(26):
        if test[i] < tar[i]:
            return
    res += targetDict[tar]


for x in TestCase:
    res = []
    sample = [0] * 26
    for y in x:
        sample[ord(y) - ord('A')] += 1
    k = ''.join(list(map(str, sample)))
    for tar in targetDict:
        judge(k, tar)

    print(res)
