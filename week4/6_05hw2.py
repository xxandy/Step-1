from collections import defaultdict
import random

# note the relationships between pages.
def noteRelations():
    relation = defaultdict(list)
    reverse = defaultdict(list)
    with open('wikilinks.txt', 'r') as f:
        for line in f:
            id, follower = line.split()
            relation[id].append(follower)
            reverse[follower].append(id)
    return relation, reverse


# BFS - search if can startName to target
def BFS(startName):
    view = set()
    startId = str(idToName.index(startName))
    search = [startId]
    for id in search:
        view.add(id)
    while search:
        nextSearch = []
        for id in search:
            if idToName[id] == target:
                return True
            else:
                for x in relationDict[id]:
                    if x not in view:
                        nextSearch.append(x)
                        view.add(id)

        search = nextSearch
    return False

# Search for the shortest path and memo the path
def memoPathBfs(startName):
    pathMemo = dict()
    startId = nameToId[startName]
    pathMemo[startId] = [startId]
    search = [startId]
    layer = 1
    while search:
        nextSearch = []
        n = 1
        for id in search:
            if idToName[id] == target:
                print()
                return pathMemo[id]
            for x in relationDict[id]:
                if x not in pathMemo:
                    pathMemo[x] = pathMemo[id] + [x]
                    nextSearch.append(x)
            # print the search status and real time fresh
            print('\rSearching for layer '+ str(layer) + ', Total = '+ str(n) +'/'+ str(len(search)),end= '')
            n += 1
        print()
        search = nextSearch
        layer += 1
    return []

# calculate page's rank.
def calScore(idToScore):
    newIdToScore = defaultdict(float)
    for id in idToScore:
        if relationDict[id]:
            s = idToScore[id] / len(relationDict[id])
            for tar in relationDict[id]:
                newIdToScore[tar] += s
    return newIdToScore


# Main
idToName = defaultdict(str)
nameToId = defaultdict(str)
with open('wikipages.txt', encoding="utf-8") as f:
    i = 0
    for line in f:
        idToName[str(i)] = line.split()[1]
        nameToId[line.split()[1]] = str(i)
        i += 1


relationDict, reverseDict = noteRelations()

# Search lonely
lonely = []
for x in idToName:
    if x not in reverseDict:
        lonely.append(idToName[x])
print(len(lonely))
# 417638


# we use memoPathBfs instead of BFS here, because
nameList = list(nameToId.keys())
while 1:
    startName = input('Please input the start:')
    # You can also use random '-r' to help you pick a random target.
    if startName == '-r':
        startName = random.choice(nameList)
        print(startName)
    target = input('Please input the end:')
    if target == '-r':
        target = random.choice(nameList)
        print(target)
    res = memoPathBfs(startName)
    if res:
        path = []
        for ID in res:
            path.append(idToName[ID])
        print('The path is:',path)
    else:
        print('No available path')
# Sample Result
# Please input the start:-r
# 馬泉営駅
# Please input the end:-r
# ネオカルチノスタチン
# Searching for layer 1, Total = 1/1
# Searching for layer 2, Total = 23/23
# Searching for layer 3, Total = 3093/3093
# Searching for layer 4, Total = 134742/134742
# Searching for layer 5, Total = 618514/618514
# Searching for layer 6, Total = 49695/262155
# The path is: ['馬泉営駅', 'ピン音', '国際標準化機構', '銅', 'アルキン', 'ネオカルチノスタチン']

# NoPath Sample
# Please input the start:-r
# セオドロス2世
# Please input the end:-r
# 東京モノレール800形電車

# Score
idToScore = defaultdict(float)
for id in idToName:
    idToScore[id] = 100.0
for i in range(20):
    idToScore = calScore(idToScore)
    idToScoreTop10 = sorted(idToScore.items(),key = lambda x : x[1], reverse=1)[:10]
    resultTop10 = []
    for x in idToScoreTop10:
        resultTop10.append([idToName[x[0]],x[1]])
    print(resultTop10)

# High Score
# ['英語', 467098.45314200403],
# ['日本', 381932.5750729001],
# ['アメリカ合衆国', 258178.13908338943],
# ['イギリス', 150336.32181161],
# ['ウィクショナリー', 129600.4228944038],
# ['フランス', 125509.03031184111],
# ['東京都', 123569.22640472912],
# ['ドイツ', 109510.28834320651],
# ['地理座標系', 94968.36594554028],
# ['日本語', 90667.91262832283]
