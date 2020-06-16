from common import read_input
import math,random

def calSlope(a,b):
    x1,y1 = a
    x2,y2 = b
    return (y1-y2)/(x1-x2)

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

def triSquare(a,b,c):
    x1,y1 = a
    x2,y2 = b
    x3,y3 = c
    return abs((x1*y2 - x2*y1) + (x2*y3 - x3*y2) + (x3*y1 - x1*y3)) / 2

def isIntersect(a,b,c,d):
    s = triSquare(a,b,c) + triSquare(a,b,d) - triSquare(a,c,d) - triSquare(b,c,d)
    return True if s == 0 else False

def adjustIntersect(result):
    for i in range(n):
        a, b = tour[result[i]], tour[result[i + 1]]
        for j in range(i + 2, n):
            c, d = tour[result[j]], tour[result[j + 1]]
            if len({a,b,c,d}) == 4 and isIntersect(a, b, c, d):
                result = result[:i + 1] + result[i + 1:j + 1][::-1] + result[j + 1:]
    return result

def sequentReinsert(result,m):
    score = totalDistance(result)

    for i in range(1, n):
        for j in range(i, min(i+m,n)):
            a, b, c = result[:i], result[i:j + 1], result[j + 1:]
            result1 = insertAtoB(b, a + c)
            score1 = totalDistance(result1)
            if score > score1:
                result = result1
                score = score1

    # change start point
    result = result[n // 2:] + result[1:n // 2 + 1]

    for i in range(1, n):
        for j in range(i, min(i+m,n)):
            if i <= n // 2 <= j:
                a, b, c = result[:i], result[i:j + 1], result[j + 1:]
                result1 = insertAtoB(b, a + c)
                score1 = totalDistance(result1)
                if score > score1:
                    result = result1
                    score = score1
    return result, score

for k in range(7):

    tour = read_input('input_'+str(k)+'.csv')
    n = len(tour)
    points = list(range(n))
    result = createConvexHull(tour)
    # result = createRandomInit(3)
    result = insertAtoB(set(points) - set(result), result)
    result = adjustIntersect(result)
    result, score = sequentReinsert(result,10)
    print(result, score)

    # name = 'output'
    # with open(f'{name}_{k}.csv', 'w') as f:
    #     f.write(format_tour(result) + '\n')
