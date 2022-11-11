 
import numpy as np
import pygame
import subprocess
import sys

proc = None

def processMethod(alpha, beta, l1, l2, rx, ry, minAngle, maxAngle):
    """
    Communicate with user process.
    input:
        alpha beta
        l1 l2
        rx ry
        minAngle maxAngle
    output:
        new_alpha new_beta

    all angles in degrees
    """ 
    proc.stdin.write(str(alpha) + " " + str(beta) + "\n" 
                    + str(l1) + " " + str(l2) + "\n" 
                    + str(rx) + " " + str(ry) + "\n" 
                    + str(minAngle) + " " + str(maxAngle) + "\n")
    proc.stdin.flush()
    
    
    line = proc.stdout.readline() 

    proc.stdout.flush()
    
    
    return map(float , line.split())



def game():

    #Pygame initialization
    pygame.init()
    centre = np.array([400,400])
    screen = pygame.display.set_mode(2*centre)
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)

    # Initialization variables
    arm1 = 100
    arm2 = 100
    minAngle = -170
    maxAngle = 170
    
    alpha = 0
    beta = 0
 
    O = np.array([0,0])
    OP = arm1*np.array([np.cos(alpha),np.sin(alpha)])
    PQ = arm2*np.array([np.cos(beta), np.sin(beta)])
    OQ = OP+PQ

    while True:
        # Per frame initialization
        R=pygame.mouse.get_pos()
        R=np.asarray(R)
        R = R - centre

        # UI
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # User process
        alpha, beta = processMethod(alpha, beta, arm1, arm2, R[0], R[1], minAngle, maxAngle)        

        # Caluclations
        OP = arm1*np.array([np.cos(np.radians(alpha)),np.sin(np.radians(alpha))])
        PQ = arm2*np.array([np.cos(np.radians(beta)),np.sin(np.radians(beta))])
        OQ = OP+PQ

        # Pygame display
        screen.fill((255,255,255))

        pygame.draw.line(screen, (100,100,100), (O + centre), (OP + centre),10)
        pygame.draw.line(screen, (80,80,80), (OP + centre), (OQ + centre),7)
        pygame.display.flip()
        clock.tick()



if __name__ == '__main__':
    
    proc = subprocess.Popen(sys.argv[1:] , stdout=subprocess.PIPE, stdin=subprocess.PIPE, encoding='utf8')
    game()
    proc.terminate()




