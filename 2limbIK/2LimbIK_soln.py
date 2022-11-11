 
import numpy as np
import sys

increment = 0.0001

while True:
    alpha, beta = map(float, input().split())
    arm1, arm2 = map(int, input().split())
    rx, ry = map(int, input().split())
    UpperAngle, LowerAngle = map(float, input().split())

    R = np.array([rx,ry])

    O = np.array([0,0])
    OP = arm1*np.array([np.cos(np.radians(alpha)),np.sin(np.radians(alpha))])
    PQ = arm2*np.array([np.cos(np.radians(beta)), np.sin(np.radians(beta))])
    OQ = OP+PQ
    
    #To calculate change in alpa and beta so that distance between effector and target is minimum
    d_by_alpha = 2*((OQ - R)[1]*OP[0] - (OQ - R)[0]*OP[1])
    d_by_beta = 2*((OQ - R)[1]*OQ[0] - (OQ - R)[0]*OQ[1])
    alpha += -d_by_alpha*increment
    beta += -d_by_beta*increment

    #angle limits
    theta = beta - alpha
    if theta < UpperAngle:
        alpha -= (UpperAngle - theta)
    if theta > LowerAngle:
        alpha -= (LowerAngle - theta)


    print(alpha, beta)



