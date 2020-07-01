from common import read_input
import math,random
from collections import defaultdict

def calSlope(a,b):
    x1,y1 = a
    x2,y2 = b
    return (y1-y2)/(x1-x2)

# search the up part and down part
# both up part and down part could use this function
# because they both start at the most big slope and become smaller (slope) one by one
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
    # [0]:ID [1]: x-coordinate
    leftMost = [0, 9999]
    rightMost = [0, 0]
    # search the most-left point and most-right point in tour.
    for i in range(len(tour)):
        if tour[i][0] < leftMost[1]:
            leftMost = [i, tour[i][0]]
        if tour[i][0] > rightMost[1]:
            rightMost = [i, tour[i][0]]
    upRoute = [leftMost[0]]
    downRoute = [rightMost[0]]
    convexRoute = findConvex(upRoute, rightMost) + findConvex(downRoute, leftMost)[1:]
    return convexRoute

def createInitial(k):
    k = 7
    tour = read_input('input_' + str(k) + '.csv')
    n = len(tour)
    points = list(range(n))
    inital = createConvexHull(tour)
    result = insertAtoB(set(points) - set(inital), inital)
    print(totalDistance(result), result)


# insert A to line segment
def insertAtoB(A, B, doPrint = False):
    segmentToDistance = defaultdict(list)
    unvisited = A
    result = B
    for i in range(len(result) - 1):
        a, b = result[i], result[i + 1]
        for x in unvisited:
            segmentToDistance[(a, b)].append(
                [distance(tour[a], tour[x]) + distance(tour[x], tour[b]) - distance(tour[a], tour[b]), x])
    for key in segmentToDistance:
        segmentToDistance[key].sort(reverse=True)

    while unvisited:
        minDistance = float('inf')
        minSegment = (0, 0)
        nextInsert = [0, 0]  # [id,num]
        for i in range(len(result) - 1):
            a, b = result[i], result[i + 1]
            while segmentToDistance[(a, b)][-1][1] not in unvisited:
                segmentToDistance[(a, b)].pop()
            if minDistance > segmentToDistance[(a, b)][-1][0]:
                minDistance = segmentToDistance[(a, b)][-1][0]
                minSegment = (a, b)
                nextInsert = [i + 1, segmentToDistance[(a, b)][-1][1]]
        unvisited.remove(nextInsert[1])
        result.insert(nextInsert[0], nextInsert[1])
        newSegment = [(minSegment[0], nextInsert[1]), (nextInsert[1], minSegment[1])]
        for key in newSegment:
            a, b = key
            for x in unvisited:
                segmentToDistance[(a, b)].append(
                    [distance(tour[a], tour[x]) + distance(tour[x], tour[b]) - distance(tour[a], tour[b]), x])
        for key in newSegment:
            segmentToDistance[key].sort(reverse=True)
        if doPrint:
            print('Initialization :',len(unvisited),'/',n)
    return result

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
        print('Adjustment :', i+1, '/', n)
    return result


def optimize(result, mode, randomNum, looptime):
    for i in range(looptime):
        if mode == 1:
            unvisited = set(random.sample(result[1:-1], randomNum))
        elif mode == 2:
            start = random.randint(1,n-1)
            end = random.randint(start+1,min(n,start+randomNum))
            unvisited = set(result[start:end])
        elif mode == 3:
            unvisited = set()
            ratio = random.randint(20, randomNum)
            center = random.randint(1, n - 1)
            for i in range(1, n - 1):
                if distance(tour[result[i]], tour[result[center]]) <= ratio:
                    unvisited.add(result[i])
        newResult = []
        for x in result:
            if x not in unvisited:
                newResult.append(x)
        newResult = insertAtoB(unvisited, newResult)
        score = totalDistance(result)
        newScore = totalDistance(newResult)
        if newScore < score:
            score = newScore
            result = newResult
        print('Optimization :', i+1 , '/', looptime,'Best Score =',score, result)
    return result


# k = 6 or k = 7
k = 7
tour = read_input('input_'+str(k)+'.csv')
n = len(tour)
points = list(range(n))
inital = createConvexHull(tour)
result = insertAtoB(set(points) - set(inital), inital, True)
print('Best Score =',totalDistance(result), result)

# *     mode    * You can use either 1 or 2 or 3 or random
# *  randomNum  * randomNum determine the re-insert scale, will cost time if too big
# *  loopTime   * the time for running optimize function
result = optimize(result, mode=random.randint(1,3), randomNum=50, looptime=10000)

result = adjustIntersect(result)
print('Best Score =',totalDistance(result), result)

# name = 'output'
# with open(f'{name}_{k}.csv', 'w') as f:
#     f.write(format_tour(result) + '\n')