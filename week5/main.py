from common import read_input
import math,random

def calSlope(a,b):
    x1,y1 = a
    x2,y2 = b
    return (y1-y2)/(x1-x2)

# search the up part and down part
def findConvex(Route,end):
    maxSlope = float('inf')
    unvisited = set(points)
    unvisited.remove(Route[-1])
    while Route[-1] != end[0]:
        nowSlope = -float('inf')
        nextPoint = -1
        j = Route[-1]
        for i in unvisited:
            slope = calSlope(tour[i], tour[j])
            if nowSlope < slope < maxSlope:
                nowSlope = slope
                nextPoint = i
        maxSlope = nowSlope
        unvisited.remove(nextPoint)
        Route.append(nextPoint)
    return Route

def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def totalDistance(result):
    res = 0
    for i in range(len(result)-1):
        res += distance(tour[result[i]],tour[result[i+1]])
    return res

# create the convexhull
def createConvexHull(tour):
    leftMost = [0, 9999]
    rightMost = [0, 0]
    for i in range(len(tour)):
        if tour[i][0] < leftMost[1]:
            leftMost = [i, tour[i][0]]
        if tour[i][0] > rightMost[1]:
            rightMost = [i, tour[i][0]]
    upRoute = [leftMost[0]]
    downRoute = [rightMost[0]]
    convexRoute = findConvex(upRoute, rightMost) + findConvex(downRoute, leftMost)[1:]
    return convexRoute

def createRandomInit(m):
    return random.sample(points, m)

# insert A to line segment
def insertAtoB(A,B):
    A = set(A)
    while A:
        nextInsert = [0,0]
        minDistance = float('inf')
        for x in A:
            for i in range(len(B)-1):
                if minDistance > distance(tour[B[i]],tour[x]) + distance(tour[x],tour[B[i+1]]) - distance(tour[B[i]],tour[B[i+1]]):
                    minDistance = distance(tour[B[i]],tour[x]) + distance(tour[x],tour[B[i+1]]) - distance(tour[B[i]],tour[B[i+1]])
                    nextInsert = [i+1,x]
        A.remove(nextInsert[1])
        B.insert(nextInsert[0],nextInsert[1])
    return B

# search the intersection('s x) of 2 lines(4 point)
def isIntersect(a,b,c,d):
    x1,y1 = a
    x2,y2 = b
    x3,y3 = c
    x4,y4 = d
    x = (y3*x4*x2 - y4*x3*x2 - y3*x4*x1 + y4*x3*x1 - y1*x2*x4 + y2*x1*x4 + y1*x2*x3 - y2*x1*x3) / (x4*y2 - x4*y1 - x3*y2 + x3*y1 - x2*y4 + x2*y3 + x1*y4 - x1*y3)
    return True if min(x1,x2) < x < max(x1,x2) and min(x3,x4) < x < max(x3,x4) else False


# If intersect, change the route
def adjustIntersect(result):
    for i in range(n):
        a, b = tour[result[i]], tour[result[i + 1]]
        for j in range(i + 2, n):
            c, d = tour[result[j]], tour[result[j + 1]]
            if len({a,b,c,d}) == 4 and isIntersect(a, b, c, d):
                result = result[:i + 1] + result[i + 1:j + 1][::-1] + result[j + 1:]
    return result

# Pick 1 to m points, search  if they have better route
# one by one
def sequentReinsert(result,m):
    score = totalDistance(result)

    for i in range(1, n):
        for j in range(i, min(i+m,n)):
            # b: list for points to be inserted
            # a+c: the list to insert points in b.
            a, b, c = result[:i], result[i:j + 1], result[j + 1:]
            result1 = insertAtoB(b, a + c)
            score1 = totalDistance(result1)
            # if score1(new score(distance)) is smaller
            if score > score1:
                result = result1
                score = score1

    # change start point
    # because we didn't test the ID for index-0
    # we cut the list in half and put the index[0] in the middle.
    result = result[n // 2:] + result[1:n // 2 + 1]

    for i in range(1, n):
        for j in range(i, min(i+m,n)):
            # only run when we test index-0
            if i <= n // 2 <= j:
                a, b, c = result[:i], result[i:j + 1], result[j + 1:]
                result1 = insertAtoB(b, a + c)
                score1 = totalDistance(result1)
                if score > score1:
                    result = result1
                    score = score1
    return result

# Pick 1 to m points [2 parts], search  if they have better route
# one by one
def twoSequentReinsert(result,m):
    score = totalDistance(result)
    for i in range(1, n):
        for j in range(i + 1, min(i + m, n)):
            for x in range(j, n):
                for y in range(x + 1, min(x + m, n)):
                    a, b, c, d, e = result[:i], result[i:j], result[j:x], result[x:y],result[y:]
                    result1 = insertAtoB(b+d,a+c+e)
                    score1 = totalDistance(result1)
                    if score > score1:
                        result = result1
                        score = score1
    return result

for k in range(7):

    tour = read_input('input_'+str(k)+'.csv')
    n = len(tour)
    points = list(range(n))
    inital = createConvexHull(tour)
    # inital = createRandomInit(3)
    result = insertAtoB(set(points) - set(inital), inital)
    print('After Insertion      =',totalDistance(result), result)
    result = adjustIntersect(result)
    print('After Swap           =',totalDistance(result), result)
    result = sequentReinsert(result,10)
    print('After Re-insertion 1 =',totalDistance(result),result)
    result = twoSequentReinsert(result, 5)
    print('After Re-insertion 2 =',totalDistance(result),result)

    # name = 'output'
    # with open(f'{name}_{k}.csv', 'w') as f:
    #     f.write(format_tour(result) + '\n')
