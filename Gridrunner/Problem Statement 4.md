Problem Statement 4
# The Pacman problem

A problem that lies between the borders of Aritificial intelligence and game development is, can a bot (an AI) play a video game? 

As a game developer, to have an AI that is as intelligent as a player is usually good for immersion, level design and difficulty design. \
As an AI developer, a video game is a good platform to simulate AI behaviour, and compete it against human players and playstyle.

This problem is a search problem on a game which is quite similar to pacman. You can read the gamerules in Gridrunner.md \
In this problem you will be writing an algorithm to calculate the best move that a bot player can take given a game state.

----
Input and output are to be queried indefinitely.

**Input**:

First line of input is 2 integers m and n separated by space, representing the height (number of rows) and width (number of columns) of the grid respectively \
The next m lines contain n characters seperated by space. \
Each character can be one of the following
- 0, representing a free space on the grid
- 1, representing a wall on the grid, which cannot be moved into
- a, representing the human player, powered down.
- A, representing the human player, powered up.
- b, representing the bot player, powered down.
- B, representing the bot player, powered up.
- o, representing the orb

a and A will not be on the grid at the same time \
b and B will not be on the grid at the same time \
A and B will not be on the grid at the same time \
o will not be on the grid if A or B is on the grid.

**Output**:

A single integer d \
d represents the direction of the action of the bot, it can be one of the following:
- 0, representing Right motion
- 1, representing Downwards motion
- 2, representing Left motion
- 3, representing Upwards motion

----

**Eg. Test cases**:

1.

Input
```
5 5
0 0 0 0 0
b 0 0 o 0
0 1 1 0 0
0 1 1 0 0
0 0 0 0 a
```
output
```
0
```
Explanation: \
Best move a can take is to move to the right towards the orb.

2.

Input
```
5 5
0 0 0 0 0
0 0 0 0 0
0 1 1 0 0
0 1 1 0 0
b 0 0 A 0
```
output
```
3
```
Explanation: \
Since human player is currently powered up, best action to take will be to move away from them, which in this case is to move upwards.

3.

Input
```
5 5
b 0 0 o a
0 1 1 0 0
0 1 1 0 0
0 1 1 0 0
0 0 0 0 0
```
output
```
1
```
Explanation: \
This is a slightly harder case, the human player will probably eat the orb in the next move, which will leave the bot trapped if it tries to move towards the orb. Thus the ideal action is to move downwards.

Yet again, this is a very open ended problem. The example testcases above do not represent the only idea solutions.