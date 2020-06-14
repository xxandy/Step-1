from common import print_tour, read_input, format_tour
import math

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

for k in range(7):

    tour = read_input('input_'+str(k)+'.csv')
    n = len(tour)
    points = list(range(n))

    leftMost = [0,9999]
    rightMost = [0,0]
    for i in range(n):
        if tour[i][0] < leftMost[1]:
            leftMost = [i,tour[i][0]]
        if tour[i][0] > rightMost[1]:
            rightMost = [i,tour[i][0]]
    upRoute = [leftMost[0]]
    downRoute = [rightMost[0]]
    convexRoute = findConvex(upRoute,rightMost) + findConvex(downRoute,leftMost)[1:]
    unvisited = set(points) - set(convexRoute)
    nextInsert = [0,0]
    while unvisited:
        minDistance = float('inf')
        for i in range(len(convexRoute)-1):
            a,b = convexRoute[i],convexRoute[i+1]
            for x in unvisited:
                if minDistance > distance(tour[a],tour[x]) + distance(tour[x],tour[b]) - distance(tour[a],tour[b]):
                    minDistance =  distance(tour[a],tour[x]) + distance(tour[x],tour[b]) - distance(tour[a],tour[b])
                    nextInsert = [i+1,x]
        unvisited.remove(nextInsert[1])
        convexRoute.insert(nextInsert[0],nextInsert[1])

    print(convexRoute)

    name = 'output'
    with open(f'{name}_{k}.csv', 'w') as f:
        f.write(format_tour(convexRoute) + '\n')




