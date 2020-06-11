
# note the relationships between IDs.
def noteRelations(dictionary):
    # ALEXNOTE:  it makes more sense to pass the filename as a parameter to this function, to make it
    #             more generic.
    with open('namelinks.txt', 'r') as f:
        for line in f:
            if line.split()[0] in dictionary:
                dictionary[line.split()[0]].append(line.split()[1])
            else:
                dictionary[line.split()[0]] = [line.split()[1]]
            # ALEXNOTE: the dicionary only has ids.   A dictionary linking the elements directly to each other
            #            would be more efficient.


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
            # notice that we need index-(int) to find name in nicknameList
            if idToName[int(id)] == target:
                return True
            else:
                for x in followRelative[id]:
                    if x not in view:
                        nextSearch.append(x)
                        view.add(id)

        search = nextSearch
    return False

# Search for the shortest path and memo the path
def memoPathBfs(startName):
    pathMemo = dict()
    startId = str(idToName.index(startName))
    pathMemo[startId] = [startId]
    search = [startId]
    while search:
        nextSearch = []
        for id in search:
            if idToName[int(id)] == target:
                return pathMemo[id]
            for x in followRelative[id]:
                if x not in pathMemo:
                    pathMemo[x] = pathMemo[id] + [x]
                    nextSearch.append(x)
        search = nextSearch
    return []


idToName = []
with open('nicknames.txt', 'r') as e:
    for line in e:
        idToName.append(line.split()[1])

followRelative = dict()
# ALEXNOTE: since the parameter is purely for output, it may make more sense to make an  return value rather than a parameter.
#           Parameter sort of implies  either IN  or IN/OUT data transfer
noteRelations(followRelative)

startName = 'adrian'
target = 'jacqueline'
print(BFS(startName))
print(memoPathBfs(startName))
# shortest - 最小何人たどればたどり着ける
print(len(memoPathBfs(startName)))
