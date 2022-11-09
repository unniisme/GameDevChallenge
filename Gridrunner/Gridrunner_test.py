from Spars.engine.Objects import *
from Spars.engine.Grid import *
from Spars.engine.Game import *
from GameProcess import ProcessMethod
import sys

GROUND = '0'
WALL = '1'
PLAYER1_f = 'a'
PLAYER1_h = 'A'
PLAYER2_f = 'b'
PLAYER2_h = 'B'
PLAYER3_f = 'c'
PLAYER3_h = 'C'
POWERUP = 'o'

player1pos = None
player2pos = None
poweruppos = None


class Player(GameObject):

    STATE_FREE = 0
    STATE_HUNTING = 1

    players = []

    COLLECTABLE = False

    MAX_POWER = 10

    def __init__(self, transform : Transform2D, grid : Grid, altLabel : str):
        self.grid = grid
        self.state = Player.STATE_FREE
        self.altLabel = altLabel
        self.powerLevel = 0
        super().__init__(transform)

        self.grid.NewObject(self)
        Player.players.append(self)

    def Move(self, direction : float):
        # Power Level
        if self.powerLevel == 0:
            if self.state == Player.STATE_HUNTING:
                self.TogglePower()
        else:
            self.powerLevel -= 1

        nextCell = self.grid.CellInDirection(self.transform.position.asTuple(), direction)       

        if nextCell == None:
            return False
        # Check if next cell is ground and no object is present on it
        if self.grid[nextCell].GetLabel() == GROUND and self.grid.objectGrid[nextCell] == None:
            self.grid.MoveObject(self.transform.position.asTuple(), nextCell)
            self.transform.position = Vector2(grid[nextCell].GetPosition())
            return True
        # If another object is present on it, try to eat it
        elif self.grid.objectGrid[nextCell] != None:
            if self.Eat(self.grid.objectGrid[nextCell]):
                self.grid.MoveObject(self.transform.position.asTuple(), nextCell)
                self.transform.position = Vector2(grid[nextCell].GetPosition())
                return True

        return False
        
    def Eat(self, other : 'GameObject'):
        if self.state > other.state:
            print(self.label, "ate", other.label)
            other.grid.DelObject(other)
            if other.COLLECTABLE:
                self.PowerUp()
            else:
                other.players.remove(other)
            return True
        return False

    def TogglePower(self):
        self.label, self.altLabel = self.altLabel, self.label
        self.transform.label = self.label

        self.state = not self.state  

    def PowerUp(self):
        if self.state == Player.STATE_FREE:
            self.TogglePower()
        self.powerLevel = Player.MAX_POWER


class PowerUp(GameObject):

    COLLECTABLE = True
    state = -1

    def __init__(self, transform : Transform2D, grid : Grid):
        self.grid = grid
        super().__init__(transform)

        self.grid.NewObject(self)

class BotProcess(ProcessMethod):

    def GetGridAction(self, grid):
        """
        Return convention:
        0 : Right
        1 : Down
        2 : Left
        3 : Up
        """
        s = str(grid.height) + " " + str(grid.breadth) + "\n"
        s += str(grid)
        out = self(s)

        return int(out)


class Game(PyGameInstance):

    WALL_COL = (200,10,10) 
    P1_COL = (0,100,0)
    P1_HUNGRY_COL = (0,200,0) 
    P2_COL = (0,0,100)
    P2_HUNGRY_COL = (0,00,200)
    ORB_COL = (200,50,40)

    OBJ_COL_DIR = {PLAYER1_f : P1_COL,
                    PLAYER1_h : P1_HUNGRY_COL,
                    PLAYER2_f : P2_COL,
                    PLAYER2_h : P2_HUNGRY_COL,
                    POWERUP : ORB_COL}

    OBJ_SCALE_DIR = {PLAYER1_f : 0.4,
                    PLAYER1_h : 0.5,
                    PLAYER2_f : 0.4,
                    PLAYER2_h : 0.5,
                    POWERUP : 1/3}

    MOVE_DIR = {pygame.K_RIGHT : Direction.RIGHT,
                pygame.K_LEFT : Direction.LEFT,
                pygame.K_DOWN : Direction.UP,
                pygame.K_UP : Direction.DOWN}


    def Run(self, grid, p1, p2, orb):

        lastDir = -1
        
        while self.isPlaying():
            

            # Win condition
            if len(Player.players) == 1:
                print(Player.players[0], "won!")
                return


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True

                # Player input
                if event.type == pygame.KEYDOWN:
                    try:
                        lastDir = Game.MOVE_DIR[event.key]
                    except:
                        pass

            if lastDir != -1:
                # Updating Powerup
                if orb not in grid.objects:
                    if p1.state == Player.STATE_FREE and p2.state == Player.STATE_FREE:
                        # If either player is in orb spot
                        if grid.objectGrid[poweruppos] != None:
                            grid.objectGrid[poweruppos].PowerUp()
                        else:
                            orb = PowerUp(Transform2D(Vector2(poweruppos), 0, POWERUP), grid)

                botAction = self.bot.GetGridAction(p2.grid)
                p2.Move(90*botAction)        # Note that bot action is first

                p1.Move(lastDir) 
                lastDir = -1
            
            self.initFrame()

            # Draw on screen
            for i in range(grid.breadth):
                for j in range(grid.height):
                    if grid[i,j].label == WALL:     # Walls
                        pygame.draw.rect(game.screen, Game.WALL_COL, pygame.Rect(i*scale, j*scale, scale, scale))
                    if grid.objectGrid[i,j] != None:   # Objects
                        pygame.draw.circle(game.screen, 
                                            Game.OBJ_COL_DIR[grid.objectGrid[i,j].label], 
                                            (i*scale + scale/2, j*scale + scale/2), 
                                            scale*Game.OBJ_SCALE_DIR[grid.objectGrid[i,j].label]) 

            self.endFrame()
        
        return True


if __name__ == '__main__':

    # Argument processing
    args = sys.argv
    if len(args) < 2:
        print("No user file given", file=sys.stderr)
        exit(1)
    gridFile = 'grids/grid1'
    processFile = args[1:]
    for i,arg in enumerate(args):
        if arg.startswith("--file="):
            gridFile = arg[7:]
            processFile.remove(arg)


    # Load grid from file
    file = open(gridFile, 'r')    

    rows,columns = map(int, file.readline().split())

    grid = Grid(rows, columns)
    for i in range(rows):
        for j,c in enumerate(file.readline().split()):
            if c == WALL or c == GROUND:
                grid[j,i].label = c
            elif c == PLAYER1_f:
                player1pos = (j,i)
            elif c == PLAYER2_f:
                player2pos = (j,i)
            elif c == POWERUP:
                poweruppos = (j,i)

    file.close()
    
    grid.InitObjectGrid()

    scale = 1000/max(rows,columns)
    
    p1 = Player(Transform2D(Vector2(player1pos), 0, PLAYER1_f), grid, PLAYER1_h)
    p2 = Player(Transform2D(Vector2(player2pos), 0, PLAYER2_f), grid, PLAYER2_h)

    orb = PowerUp(Transform2D(Vector2(poweruppos), 0, POWERUP), grid)

    bot = BotProcess(processFile)

    game = Game(scale*columns, scale*rows)
    game.bot = bot  # Bad practice kids I'm mildly lazy

    game.Start()
    game.Run(grid, p1, p2, orb)




