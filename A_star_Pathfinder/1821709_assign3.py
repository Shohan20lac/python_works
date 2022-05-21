import copy

pathcost = 0


def goright():
    global pathcost,robotX
    pathcost += 1
    robotX += 1
    
def goleft():
    global pathcost,robotX
    pathcost += 1
    robotX -= 1

def goup():
    global pathcost,robotY
    pathcost += 1
    robotY -= 1    

def godown():
    global pathcost,robotY
    pathcost += 1
    robotY += 1
    
def goupleft():
    global pathcost, robotX, robotY
    pathcost += 1
    robotY -= 1
    robotX -= 1
    
def goupright():
    global pathcost, robotX, robotY
    pathcost += 1
    robotY -= 1
    robotX += 1
    
def godownright():
    global pathcost, robotX, robotY
    pathcost += 1
    robotY += 1
    robotX += 1
    
def godownleft():
    global pathcost, robotX, robotY
    pathcost += 1
    robotY += 1
    robotX -= 1   

def extendFrontier(current): 
    global frontier  
    
    frontier.append(current)
  
def getNeighbors():
    global neighbors
    
    #get right neighbor
    if robotX < xsize :
        if ( board[robotY][robotX+1] =='b' or board[robotY][robotX+1] =='e'):
            print('right cell blocked or explored. Cannot append')    
        else:
            neighbors.append((robotY, robotX+1))
            print('right neighbor found:' ,robotY,robotX+1)
            board[robotY][robotX+1] = 'e'
        
        
    #get left neighbor
    if robotX > xsize :
        if (board[robotY][robotX-1] =='b' or board[robotY][robotX-1] =='e' ):
            print('left cell blocked or explored. Cannot append')    
        else:
            neighbors.append((robotY, robotX-1))
            print('left neighbor found:' ,robotY,robotX-1)
            board[robotY][robotX-1] = 'e'
        
    #get down neighbor
    if robotY < ysize :
        if (board[robotY+1][robotX] =='b' or board[robotY+1][robotX] =='e'):
            print('down cell blocked or explored. Cannot append')    
        else:
            neighbors.append((robotY+1, robotX))
            print('down neighbor found:' ,robotY+1, robotX)
            board[robotY+1][robotX] = 'e'
        
    #get up neighbor
    if robotY > ysize :
        if (board[robotY-1][robotX] =='b' or board[robotY-1][robotX] =='e'):
            print('up cell blocked or explored. Cannot append')    
        else:
            neighbors.append((robotY-1, robotX))
            print('up neighbor found:' ,robotY-1,robotX)
            board[robotY-1][robotX] = 'e'
    
    
    #get up left neighbor
    if robotY> ysize and robotX>xsize:
        if (board[robotY-1][robotX-1] =='b' or board[robotY-1][robotX-1] =='e' ):
            print('left cell blocked or explored. Cannot append')    
        else:
            neighbors.append( (robotY-1,robotX-1) )
            print('up left neighbor FOUND')
            board[robotY-1][robotX-1] = 'e'
        
    #get up right neighbor
    if robotY> ysize and robotX<xsize:
        if (board[robotY-1][robotX+1] =='b' or board[robotY-1][robotX+1] =='e'):
            print('up right cell blocked or explored. Cannot append')    
        else:
            neighbors.append( (robotY-1,robotX+1) )
            print('up right neighbor FOUND')
            board[robotY-1][robotX+1] = 'e'
        
    #get down left neighbor
    if robotY < ysize and robotX>xsize:
        if (board[robotY+1][robotX-1] =='b' or board[robotY+1][robotX-1] =='e'):
            print('down left cell blocked or explored. Cannot append')    
        else:
            neighbors.append( (robotY+1,robotX-1) )
            print('down left neighbor FOUND')
            board[robotY+1][robotX-1] = 'e'
        
    #get down right neighbor
    if robotY < ysize and robotX<xsize:
        if (board[robotY+1][robotX-1] =='b' or board[robotY+1][robotX-1] =='e'):
            print('down left cell blocked or explored. Cannot append')    
        else:
            neighbors.append( (robotY+1,robotX+1) )
            print('down right neighbor FOUND')
            board[robotY+1][robotX+1] = 'e'
    
    print('\n')

def getNeighborCost(i,j):
    global robotX, robotY
    
    #diagonal neighbor
    if (i!=robotY and j!=robotX):
        return 3
    
    #vertical neighbor
    if (i!=robotY and j==robotX):
        return 2
        
    #horizontal neighbor
    if (i==robotY and j!=robotX):
        return 1

i = 0
j = 1

        
def get_max_F_neighbor():
    global neighbors, fmax, maxindex
    print('searching for max F neighbor of node', current )
    if len(neighbors)==1:
        print('Only one neighbor. Returning 0:')
        return 0  

    fmax = 0
    tempindex = 0   
    
    for (i,j) in neighbors:
        print('checking neighbor #', tempindex, ':', neighbors[tempindex] ,'. Is it max F?')     
        
        this_neighbor_cost = getNeighborCost (i,j)
        print('cost value: ' , this_neighbor_cost)
        print('manhattan value: ', manhattan[i][j])
        
        this_neighbor_fvalue = this_neighbor_cost + manhattan[i][j]
        print('F value: ', this_neighbor_fvalue)
        
    
        if ( this_neighbor_fvalue >= fmax ):
            print( neighbors[tempindex], 'may be a max F node. Checking rest of list:')
            fmax = copy.copy(this_neighbor_fvalue)
            maxindex = copy.copy(tempindex)
            tempindex += 1
    
    
    print('RESULT: neighbor number',maxindex, neighbors[maxindex], 'is the max F neighbor.')
    return maxindex

def getminindex():
    global neighbors, fmin, minindex
    tempindex = 0
    
    for (i,j) in neighbors:
        this_neighbor_cost = getNeighborCost (i,j)
        this_neighbor_fvalue = this_neighbor_cost + manhattan[i][j]
    
        if ( this_neighbor_fvalue < fmin ):
            fmin = this_neighbor_fvalue
            minindex = tempindex
            tempindex - 1
    return minindex

def expandCurrent( max_F_neighbor ):
    global current
    current.append(max_F_neighbor)    
    
def updatePathCost (  ):
    global pathcost
    
    # case1: path has less than/ =1 nodes
    if len(takenpath)<=1:
        return 0
    
    for i in range (1, len(takenpath)):
        #detect diag movement, add3
        if (
            takenpath[i][1]-takenpath[i-1][1] != 0 
            and
            takenpath[i][0] - takenpath[i-1][0] != 0 
            ):
            print('diagonally moved. Added ', 3)
        pathcost += 3
       
        #detect horizontal movement, add1
        if takenpath[i][1] - takenpath[i-1][1] != 0 :
            print('horizontally moved. Added' , 1)
        pathcost += 1
        
        #detect vetical movement, add2
        if takenpath[i][0] - takenpath[i-1][0] != 0 :
            print('vertically moved. Added' , 2)
        pathcost += 2        
        
# key 
key = {
       'a': 'cell is open for exploration',
       'e': 'cell is explored',
       'b': 'cell is blocked',
       'g': 'cell is goal'
}

#setting up board
board = []
board.append(['a', 'a', 'a', 'b'])
board.append(['a', 'b', 'a', 'a'])
board.append(['a', 'a', 'b', 'g'])
board.append(['a', 'a', 'a', 'a'])

#setting up manhattan distances list
manhattan = []
manhattan.append([0,0,0,0])
manhattan.append([0,0,0,0])
manhattan.append([0,0,0,0])
manhattan.append([0,0,0,0])

#listing all the path costs


#let, goal location is known (for manhattan distance calculation).
goaly = 2
goalx = 3
tempx = 0
tempy = 0

for i in range(0,4):
    tempy = i
    for j in range(0,4):
        tempx = j
        currmanhatt = abs(goalx-tempx) + abs(goaly-tempy) 
        manhattan[i][j] = currmanhatt










#base case setups

max_F_neighbor=0
min_F_neighbor=0

xsize = 3
ysize = 3
newY = (0,0)
newX = (0,0)
robotX = 0
robotY = 0
takenpath = [] #list of list of integers (AKA list of coordinates AKA a path)
takenpath.append( (robotX, robotY ) )

fmin = 1000

maxindex = 0
minindex = 0


frontier = []
frontier.append ((robotX, robotY))  #add start node to frontier

neighbors = []
getNeighbors()  #of start node

tempman = 0
print('start nodes neighbors initialized:' , neighbors)

print(frontier[len(frontier)-1])

#find best neighbor of current node
while (len(frontier))!=0:
    
    if (board[robotY][robotX] =='g'):
        print('goal state reached')
        break
    
    temp1 = (copy.copy((  frontier.pop()  )))
    current = []
    current.append ((temp1))

    while (len(neighbors))!=0:
        
        
        maxindex = copy.copy( get_max_F_neighbor() )
        max_F_neighbor = neighbors[maxindex]
        
        print('neighbors remaining:', neighbors)
        print( 'max neighbor found: ', max_F_neighbor )
        
        if (len(neighbors)==1):  #only one best node left to move to
            print('best F node found: ', max_F_neighbor )
            newY = list(max_F_neighbor)[0]
            newX = list(max_F_neighbor)[1]
            
            robotY= newY
            robotX= newX
            takenpath.append( (robotY, robotX ) )
            print(' MOVED robot to :', robotY, robotX)
            updatePathCost()
            
        
        current.append( copy.copy( max_F_neighbor) )
        print('max F neighbor' , max_F_neighbor, 'added to current.')
        print('current now: ', current)
        
        
        
        frontier.append ( copy.copy(current) )
        print('added current path:', current, 'to frontier.')
        
        current.pop()
        neighbors.pop(maxindex)
        
        print('exploring different neighbor...\n')        
    
    getNeighbors()


print('FINAL PATHCOST: ' , pathcost )
print('Taken path:' , takenpath )

