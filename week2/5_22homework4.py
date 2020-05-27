class Node(object):
    def __init__(self, k, v):
        self.val = [k, v]
        self.left = None
        self.right = None

# end <> .. <> .. <> start
def get(k ,v, start, end):
    if cache_size >= 1:
        if not cache:
            node = Node(k, v)
            cache[k] = node
            start = node
            end = node
        else:
            if k in cache and k != start.val[0]:
                nodeToAdd, end = deleteNode(k, end)
                cache[k] = nodeToAdd
                start = addNewStart(nodeToAdd, start)
            elif k not in cache:
                cache[k] = Node(k, v)
                start = addNewStart(cache[k], start)
                if len(cache) > cache_size:
                    end = deleteNode(end.val[0], end)[1]
    return start, end

# k != start[0]
def deleteNode(k, end):
    if k == end.val[0]:
        newEnd = end.right
        newEnd.left = None
        end.right = None
        end = newEnd
    else:
        l,r = cache[k].left, cache[k].right
        l.right = r
        r.left = l.right
    return cache.pop(k), end

def addNewStart(newstart, start):
    newstart.left = start
    start.right = newstart
    return newstart




cache = {}
cache_size = 3
start, end = None, None
start, end = get('a', 'A', start, end)
start, end = get('b', 'B', start, end)
start, end = get('c', 'C', start, end)
print(cache.keys(),start.val)
start, end = get('d', 'D', start, end)
print(cache.keys(),start.val)
start, end = get('e', 'E', start, end)
print(cache.keys(),start.val)
start, end = get('d', 'D', start, end)
print(cache.keys(),start.val)
start, end = get('d', 'D', start, end)
print(cache.keys(),start.val)