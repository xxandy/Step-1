# k for key, v for value.
class Node(object):
    def __init__(self, k, v):
        self.val = [k, v]
        self.left = None
        self.right = None

# end <> .. <> .. <> start
def get(k ,v, start, end):
    if cache_size >= 1:
        if not cache:
            # initialization the double linked list.
            node = Node(k, v)
            cache[k] = node
            start = node
            end = node
        else:
            # if the target_URL is already in cache and it is not the 'start'.
            # [target_URL is not the latest url in double linked list]. 
            if k in cache and k != start.val[0]:
                nodeToAdd, end = deleteNode(k, end)
                cache[k] = nodeToAdd
                start = addNewStart(nodeToAdd, start)
            # if the target_URL not in cache.
            elif k not in cache:
                cache[k] = Node(k, v)
                start = addNewStart(cache[k], start)
                if len(cache) > cache_size:
                    end = deleteNode(end.val[0], end)[1]
    return start, end

# ALEXNOTE: I really like that you chose to add deleteNote as a separate function!
#           Quick question: is this meant to be called from outside this class?
#           If not, how could you avoid it?

# k != start.val[0]
def deleteNode(k, end):
    # if k is the 'end'node, the oldest one.
    if k == end.val[0]:
        newEnd = end.right
        newEnd.left = None
        end.right = None
        end = newEnd
    else:
        l,r = cache[k].left, cache[k].right
        l.right = r
        r.left = l.right
    # delete the key-'k' from the chache and get new end.
    return cache.pop(k), end

def addNewStart(newstart, start):
    newstart.left = start
    start.right = newstart
    return newstart




cache = {}
# cache's max size.
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
