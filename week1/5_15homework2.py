## the program for game- I can haz wordz [make 16 alphabets be words 'highest score']

from collections import defaultdict

valueForLetter = [1, 1, 2, 1, 1, 2, 1, 2, 1, 3, 3, 2, 2, 1, 1, 2, 3, 1, 1, 1, 1, 2, 2, 3, 2, 3]


def queryToHash(x):
    sample = [0] * 26
    i = 0
    while i < len(x):
        sample[ord(x[i]) - ord('A')] += 1
        i += 2 if x[i] == 'Q' else 1
    while sample[-1] == 0: sample.pop()
    return sample
    # the sample is a list


def hashToValue(x):
    res = 0
    for i in range(len(x)):
        res += int(x[i]) * valueForLetter[i]
    return res


def dfs(node, test):
    global maxRes
    if maxRes[0] < node.val:
        maxRes = [node.val, hashToWord[node.hash]]
    for freq, child in node.children.items():
        if len(child.hash) > len(test): break
        if freq <= test[len(child.hash) - 1]:
            dfs(child, test)


class TreeNode(object):
    def __init__(self):
        self.hash = ''
        self.val = 0
        self.children = defaultdict(TreeNode)



# put origin words in list
originDict = []
with open('dictionary.txt', 'r') as f:
    for line in f:
        originDict.append(line.strip('\n').upper())

# create dictionary for hash to word
hashToWord = {}
for x in originDict:
    hashToWord[''.join(map(str, queryToHash(x)))] = x
    # use map to make list be string

# create tree
root = TreeNode()
for key in hashToWord:
    node = root
    for i in range(len(key)):
        hash = node.hash
        node = node.children[int(key[i])]
        node.hash = hash + key[i]
    node.val = hashToValue(node.hash)

# input and dfs
for i in range(10):
    maxRes = [0, '']
    test = input("Input:")
    dfs(root, queryToHash(test))
    print(maxRes)
