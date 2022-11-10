from Spars.engine.Objects import *
from Spars.engine.Grid import *
from Spars.engine.Game import *
from GameProcess import ProcessMethod
import sys

GROUND = '0'
WALL = '1'
PLAYER1 = 'a'
PLAYER2 = 'b'

class Player(GameObject):

    players = []

    def __init__(self, transform : Transform2D, grid : Grid):
        """
        Player object
        """
        self.grid = grid        # Embedded grid
        self.health = 100       # Health
        super().__init__(transform)

        self.grid.NewObject(self)
        Player.players.append(self)

    # Move one cell in the given direction
    def Move(self, direction : float):
        nextCell = self.grid.CellInDirection(self.transform.position.asTuple(), direction)       

        if nextCell == None:
            return False
        # Check if next cell is ground and no object is present on it
        if self.grid[nextCell].GetLabel() == GROUND and self.grid.objectGrid[nextCell] == None:
            self.grid.MoveObject(self.transform.position.asTuple(), nextCell)
            self.transform.position = Vector2(grid[nextCell].GetPosition())
            return True

        return False

    def __del__(self):
        self.grid.DelObject(self)
        Player.players.remove(self)

    def DecreaseHealth(self, dx):
        self.health -= dx
        if self.health < 0:
            self.health == 0

    def CheckAlive(self):
        return self.health > 0

class Observer(ProcessMethod):

    def IsObserving(self, grid : Grid) -> bool:
        s = str(grid.height) + " " + str(grid.breadth) + "\n"
        s += str(grid)
        return bool(int(self(s)))
        
class Game(PyGameInstance):

    # Colours
    WALL_COL = (200,10,10) 

    P1_COL = [0, 200, 0]
    P2_COL = [0, 0, 200]

    OBJ_COL_DIR = {PLAYER1 : P1_COL,
                    PLAYER2 : P2_COL}

    # Conditional dictionaries
    MOVE_DIR_P1 = {pygame.K_RIGHT : Direction.RIGHT,
                pygame.K_LEFT : Direction.LEFT,
                pygame.K_DOWN : Direction.UP,
                pygame.K_UP : Direction.DOWN}

    MOVE_DIR_P2 = {pygame.K_d : Direction.RIGHT,
                pygame.K_a : Direction.LEFT,
                pygame.K_s : Direction.UP,
                pygame.K_w : Direction.DOWN}

    deathRate = 0.2     # rate of decrease of health

    def Run(self, p1, p2):

        while self.isPlaying():

            Game.P1_COL[1] = 2*p1.health    # Seeker colour fade
            Game.P2_COL[2] = 2*p2.health    # Hider colour fade

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True

                # Player input
                if event.type == pygame.KEYDOWN:
                    try:
                        p1.Move(Game.MOVE_DIR_P1[event.key])
                    except:
                        pass

                    try:
                        p2.Move(Game.MOVE_DIR_P2[event.key])
                    except:
                        pass

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
                                            scale/3) 

            # Point checks
            if obs.IsObserving(grid):
                pygame.draw.line(game.screen, (200,200,200), 
                                (p1.transform.position*scale + Vector2(scale/2,scale/2)).asTuple(), 
                                (p2.transform.position*scale + Vector2(scale/2,scale/2)).asTuple())
                p2.DecreaseHealth(Game.deathRate)
                if not p2.CheckAlive():
                    print("Seeker won!")
                    return True
            
            else:
                p1.DecreaseHealth(Game.deathRate)
                if not p1.CheckAlive():
                    print("Hider won!")
                    return True

            self.endFrame()
        
        return False


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
            elif c == PLAYER1:
                player1pos = (j,i)
            elif c == PLAYER2:
                player2pos = (j,i)

    file.close()
    
    grid.InitObjectGrid()

    scale = 1000/max(rows,columns)
    
    p1 = Player(Transform2D(Vector2(player1pos), 0, PLAYER1), grid)
    p2 = Player(Transform2D(Vector2(player2pos), 0, PLAYER2), grid)
    grid.NewObject(p1)
    grid.NewObject(p2)

    obs = Observer(processFile)

    game = Game(scale*columns, scale*rows)

    game.Start()
    game.Run(p1, p2)
