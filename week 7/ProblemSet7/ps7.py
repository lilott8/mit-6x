# 6.00x Problem Set 7: Simulating robots

import math
import random

import ps7_visualize
import pylab

# For Python 2.7:
from ps7_verify_movement27 import testRobotMovement

# If you get a "Bad magic number" ImportError, comment out what's above and
# uncomment this line (for Python 2.6):
# from ps7_verify_movement26 import testRobotMovement


# === Provided class Position
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
        return Position(random.random()*(self.width), random.random()*(self.height))
        

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


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.direction = random.randrange(360)
        self.position = self.room.getRandomPosition()
        #print self.position
        self.room.cleanTileAtPosition(self.position)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!
        


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        pos = self.position.getNewPosition(self.direction, self.speed)
        if self.room.isPositionInRoom(pos): #if it's in the room, go there
            self.setRobotDirection(random.randrange(360))
            self.position = pos
            self.room.cleanTileAtPosition(pos)
        else:#if not we need a new direction
            self.setRobotDirection(random.randrange(360))
# Uncomment this line to see your implementation of StandardRobot in action!
#testRobotMovement(StandardRobot, RectangularRoom)



# === Problem 3
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    #print "Must clean " + str(min_coverage) + " of the room"
    #anim = ps7_visualize.RobotVisualization(num_robots, width, height)
    cleanRoom = float(width*height)*min_coverage
    steps = []
    for i in range(num_trials):
        room = RectangularRoom(width, height)
        robots = []
        time = 0
        for robot in range(num_robots):
            robots.append(robot_type(room, speed))
        while float(room.getNumCleanedTiles()) < cleanRoom:
            for r in robots:
                #anim.update(room, robots)
                r.updatePositionAndClean()
            time += 1
        steps.append(time)
        #anim.done()
    total = 0
    for i in steps:
        total += i
    return float(total)/len(steps)

# === Problem 4
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def __init__(self, room, speed):
        Robot.__init__(self, room, speed)
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        pos = self.position.getNewPosition(self.direction, self.speed)
        if self.room.isPositionInRoom(pos): #if it's in the room, go there
            self.setRobotDirection(random.randrange(360))
            self.position = pos
            self.room.cleanTileAtPosition(pos)
        else:#if not we need a new direction
            self.setRobotDirection(random.randrange(360))



# === Problem 5
#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#
#

def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print "Plotting", num_robots, "robots..."
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300/width
        print "Plotting cleaning time for a room of width:", width, "by height:", height
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

'''    
room = RectangularRoom(5,5)
robot = Robot(RectangularRoom(5,8), 1.0)
print robot.getRobotPosition()
for x in range(10):
    x = random.random()*room.width
    y = random.random()*room.height
    pos = Position(x,y)
    print pos
    if room.isPositionInRoom(pos):
        robot.setRobotPosition(pos)
        print robot.getRobotPosition()
        print "=================================="
'''
#num_robots, speed, width, height, min_coverage, num_trials, robot_type
"""
if random.randrange(1,3)%2:
    robot = StandardRobot
    robot = RandomWalkRobot
else:
    robot = RandomWalkRobot
avg = runSimulation(random.randrange(2,3), random.random(), random.randrange(2,10), random.randrange(2,10), random.random(), random.randrange(1,5), 'RandomWalkRobot')
"""
#showPlot1('Time to Clean vs. Size of Room', 'size of room (area)', 'number of robots')
showPlot2('', '', 'number of robots')