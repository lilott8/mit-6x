import math
import random

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)

# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.room = []
        self.width = width
        self.height = height
        self.sizeOfRoom = width * height
        #1 = clean
        #0 = dirty
        self.room = [[0 for x in range(0,height)] for y in range(0,width)]
                
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        #print "This is returning a 1 || 0 not a True/False"
        x = int(math.floor(pos.getX()))
        y = int(math.floor(pos.getY()))
        self.room[x][y] = 1

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        #print "This is returning a 1 || 0 not a True/False"
        if m >= self.width or m < 0:
            return False
        if n >= self.height or n < 0:
            return False
        if self.room[int(m)][int(n)] == 1:
            return True
        else:
            return False
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.sizeOfRoom

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        numCleanTiles = 0
        #print self.room
        for x in range(0, self.width):
            for y in range(0, self.height):
                numCleanTiles += self.room[x][y]
        return numCleanTiles

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        #random.seed(0)
        return Position(random.randrange(0,self.width,1), random.randrange(0,self.height,1))
        

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        if pos.getX() < 0 or pos.getX() >= self.width:
            return False
        if pos.getY() < 0 or pos.getY() >= self.height:
            return False
        return True


room = RectangularRoom(4,6)
"""
print "Getting random positions: "
for x in range(0,100):
    print room.getRandomPosition()
print "+++++++++++++++++++++++++++++"
"""
print "Cleaning the room: "
pos = Position(.6,1.3)
#print room.cleanTileAtPosition(pos)
"""
for x in range(0,5):
    for y in range(0,5):
        print room.isTileCleaned(x,y)
        print room.getNumCleanedTiles()
   """
   
#print room.isTileCleaned(0, 1)
#print room.isTileCleaned(0, 2)
#print room.isTileCleaned(0, 3)
print "Cleaning at " + str(pos.getX()) + ", " + str(pos.getY())
room.cleanTileAtPosition(pos)
print room.isTileCleaned(0,1)
#print room.isTileCleaned(0, 5)
"""
print "___________________________________________"
print "Check to see if a tile is clean:"
print room.isTileCleaned(m=3,n=5)
print "********************************************"
print "Getting room positions: "
print room.isPositionInRoom(Position(-0.10, 0.00))
print room.isPositionInRoom(Position(0.00, -0.10))
print room.isPositionInRoom(Position(18.13, 7.36))
print room.isPositionInRoom(Position(2.00, 0.00))
print "================================"
print "Cleaning tiles repeatedly"
for x in range(0,5):
    for y in range(0,5):
        room.cleanTileAtPosition(Position(x,y))
        print room.isTileCleaned(x,y)
        print room.getNumCleanedTiles()
"""