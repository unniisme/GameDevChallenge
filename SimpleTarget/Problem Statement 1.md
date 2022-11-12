Problem Statement 1

# Target Direction Finding

Timmy is a war-criminal who is imprisoned in the National jail of the Soviet Russia. One day,
during the lunch time, he escapes from the prison and starts his escapade. To avoid such
circumstances, the prison guard has integrated every prisoner with a GPS tracker, the prison
has canon whose co-ordinates are entered by the guard, and the co-ordinates of Timmy will
be traced down by the GPS tracker. Find the angle by which the canon has to turn to shoot
Timmy down 

----
Input and output are to be queried indefinitely.

**Input**:

First line of input is x coordinate and y coordinate of cannon separated by space. \
Second line of input is x coordinate and y coordinate of timmy separated by space.

**Output**:

A single float value, representing the angle in degrees, measured from the X axis, representing the direction the cannon has to point to to shoot Timmy.

----

**Eg. Test cases**:

1.

Input
```
0 0
1 1
```
output
```
45
```
Explanation: \
The canon is at (0,0) and Timmy is at (1,1) so the canon has to turn 45° anti-clockwise to
shoot Timmy down

2. 
Input
```
2 4
5 6
```
output
```
33.690067
```
Explanation: \
The canon is at (2,4) whereas Timmy is at (5,6) so the canon has to rotate by 33.69°

3. 
Input
```
9 9
0 0
```
output
```
-135
```
Explanation: \
The canon is at (9,9) whereas Timmy is at (0, 0) so the canon has to rotate by 135° clockwise so it can aim at Timmy

4. 
Input
```
5 0
-5 0
```
output
```
180
```
Explanation: \
The canon is at (5,0) whereas Timmy is at (-5, 0) so the canon has to rotate by 180° to aim at Timmy

---
Note that these answers are not the only answers. You can test your answer using the game script, more info about this is in SimpleTarget.md. \
Also note that if you wish to, you can implement it in slightly different, perhaps innovative ways, like perhaps you don't want the cannon to directly snap on the mouse and instead just wants it to follow the mouse with a bit of a lag. Feel free to implement it this way. We will be demonstrating game environments, not the actual line by line solution to the code.