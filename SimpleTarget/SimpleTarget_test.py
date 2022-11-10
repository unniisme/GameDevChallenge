
from GameProcess import ProcessMethod
from math_utils import Vector2
import pygame
import sys

screenSize = [800,600]

class CannonBall:

    balls = []

    def __init__(self, position, rotation, speed, radius = 12):
        """
        An object that moves and hits stuff 
        """
        self.position = position    # start position
        self.rotation = rotation    # Start rotation
        self.speed = speed          # Speed of ball
        self.radius = radius        # Radius of ball

        CannonBall.balls.append(self)

    def __del__(self):
        CannonBall.balls.remove(self)

    def Update(self, dt):
        self.position = (Vector2(self.position) + Vector2.PolarConstructorDeg(self.speed, self.rotation) * dt).asTuple()
        CannonBall.OutBound(self)

    def Draw(self, screen):
        pygame.draw.circle(screen, (50,20,20), self.position, self.radius)

    def CheckContact(self, target : tuple) -> bool:
        return (Vector2(target) - Vector2(self.position)).magnitude < self.radius

    def OutBound(ball):
        if not (0<ball.position[0]<screenSize[0] or 0<ball.position[1]<screenSize[1]):
            del ball

    def UpdateAll(dt):
        for ball in CannonBall.balls:
            ball.Update(dt)

    def DrawAll(screen):
        for ball in CannonBall.balls:
            ball.Draw(screen)

    def CheckContactAny(target : tuple):
        return any([ball.CheckContact(target) for ball in CannonBall.balls])
            

class Cannon:

    def __init__(self, position, girth = 15, length = 30, timeFrame = 4):
        self.position = position    # Hinge position
        self.rotation = 0           # Current facing angle
        self.girth = girth          # Width of cannon
        self.length = length        # Length of cannon
        self.timeFrame = timeFrame  # Rate of fire

        self.processMethod = ProcessMethod(sys.argv[1:])  # Child process

    # Look at target
    def Turn(self, target : tuple):
        s = str(self.position[0]) + " " + str(self.position[1]) + "\n" + str(target[0]) + " " + str(target[1]) + "\n"
        
        self.rotation = float(self.processMethod(s))

    def Shoot(self):
        CannonBall(self.position, self.rotation, 0.5)
        

    def Draw(self, screen):

        pygame.draw.circle(screen, (0,0,0), self.position, self.girth)
        pts = []
        pts.append((Vector2(self.position) + Vector2.PolarConstructorDeg(self.girth, self.rotation+90)).asTuple())
        pts.append((Vector2(self.position) + Vector2.PolarConstructorDeg(self.girth, self.rotation-90)).asTuple())
        pts.append((Vector2.PolarConstructorDeg(self.length, self.rotation) + Vector2(pts[1])).asTuple())
        pts.append((Vector2.PolarConstructorDeg(self.length, self.rotation) + Vector2(pts[0])).asTuple())
        pygame.draw.polygon(screen, (0,0,0), pts)



def game():

    #Pygame initialization
    pygame.init()
    screen = pygame.display.set_mode(screenSize)
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)

    # Initialization variables
    cannon = Cannon((400,300))

    while True:
        # Per frame initialization
        R=pygame.mouse.get_pos()

        # UI
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

        # User process
        cannon.Turn(R)
        CannonBall.UpdateAll(clock.get_time())

        if pygame.time.get_ticks() % (cannon.timeFrame*100) == 0:
            cannon.Shoot()

        if CannonBall.CheckContactAny(R):
            print("You've been hit!")
            return

        # Pygame display
        screen.fill((255,255,255))

        cannon.Draw(screen)
        CannonBall.DrawAll(screen)
        pygame.display.flip()
        clock.tick()



if __name__ == '__main__':
    
    game()




