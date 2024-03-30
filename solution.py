import math
from turtle import pos
directionsCoords = {
    "north": (-1,0),
    "south": (1,0),
    "west": (0,-1),
    "east": (0,1)
}

def solvepart1():
    data = fileRead("input.txt")
    grid = []
    for row in data:
        vals = list(row.strip())
        vals = [ int(val) for val in vals ]
        grid.append(vals)

    print( dijkstraModifiedNoLines(grid, 1, 3) )

def solvepart2():
    data = fileRead("input.txt")
    grid = []
    for row in data:
        vals = list(row.strip())
        vals = [ int(val) for val in vals ]
        grid.append(vals)

    print( dijkstraModifiedNoLines(grid, 4, 10) )
    
#use dijkstras algorithm to find the shortest path between 0,0 and the opposite corner while only going straight between X and Y spaces
def dijkstraModifiedNoLines(grid, minSpaces, maxSpaces):

    #set up lists and dictionaries
    visitedNodes = []
    dists = {}
    edgeNodes = [(0,(0,0),(-1,-1))] #distance, (x,y), prevdirection

    #loop until every node has been visited
    while len(edgeNodes) > 0:

        #find next node to visit
        currentNode = ()
        newDist = math.inf
        for node in edgeNodes:
            if node[0] < newDist:
                currentNode = node
                newDist = node[0]
        edgeNodes.remove(currentNode)
        dist, coords, prevdirection = currentNode

        #check if end has been reached
        if coords[0] == len(grid)-1 and coords[1] == len(grid[0])-1:
            return dist

        #check if node is already visited
        if (coords,prevdirection) in visitedNodes:
            continue
        visitedNodes.append((coords,prevdirection))

        #get list of valid directions
        allNeighbors = list(directionsCoords.values())
        possibleNeighbors = []
        for offset in allNeighbors:
            invertedPrev = tuple([ val * -1 for val in prevdirection])
            if offset != prevdirection and offset != invertedPrev:
                possibleNeighbors.append(offset)

        #calculate distance for each neighbor up to maxspaces away
        for direction in possibleNeighbors:
            addedDist = 0
            for travellength in range(1,maxSpaces+1):
                newCoords = tuple([ coords[i] + (direction[i] * travellength) for i in [0,1] ])
                if newCoords[0] >= 0 and newCoords[0] < len(grid) and newCoords[1] >= 0 and newCoords[1] < len(grid[1]):
                    addedDist = addedDist + grid[newCoords[0]][newCoords[1]]
                    if travellength >= minSpaces:
                        newDist = dist + addedDist
                        if newDist < dists.get((newCoords,direction), math.inf):
                            dists[(newCoords,direction)] = newDist
                            edgeNodes.append((newDist, newCoords, direction))



#adds two coordinates together
def posAdd(pos1, pos2):
    return tuple([ sum(coords) for coords in zip(pos1, pos2) ])
    
def fileRead(name):
    data = []
    f = open(name, "r")
    for line in f:
        data.append(line);
    return data

solvepart2()