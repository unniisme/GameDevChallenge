Problem Statement 3

# Grid Raycasting
Raycasting is a problem that comes up often in game development, it primarily tries to answer the following question: \
`When I look in one direction, what do I see?`

The usual way this is implemented is that, a ray is cast from the veiwer in the direction that they are looking, and the first thing the ray touches is your answer. Hence the name _raycasting_.

In this problem, you will be implementing raycasing in the context of a 2D grid. \
The grid will have 2 players, a and b. Your program is to return whether a can see b or not. 

----
Input and output are to be queried indefinitely.

**Input**:

First line of input is 2 integers m and n separated by space, representing the height (number of rows) and width (number of columns) of the grid respectively \
The next m lines contain n characters seperated by space. \
Each character can be one of the following
- 0, representing a free space on the grid
- 1, representing a wall on the grid, which cannot be seen looked through
- a, represeting the seeker
- b, representing the hider

**Output**:

Either 0 or 1, \
0 representing the hider is not seeing the seeker, 1 representing the opposite

----

**Eg. Test cases**:

1.

Input
```
3 3
0 0 0
a 1 b
0 0 0
```
output
```
0
```
Explanation: \
a cannot see b due to the wall at (1,1)  (0 indexed)

2.

Input
```
3 3
0 0 0
a 0 b
0 1 0
```
output
```
0
```
Explanation: \
a can see b

3.

Input
```
5 5
0 0 0 0 0
a 0 0 0 0
0 1 1 b 0
0 1 1 0 0
0 0 0 0 0
```
output
```
0
```
Explanation: \
a cannot see b due to the wall at (2,2)


4.

Input
```
5 5
0 0 0 0 0
0 a 0 0 0
0 1 1 0 b
0 1 1 0 0
0 0 0 0 0
```
output
```
1
```
Explanation: \
a can see b

It is to be noted that these cases are not going to be evaluated based on exact accuracy. Say if you feel like test case 3 should be 1, go for it, we'll simulate it in game with bigger testcases and visually see how it works.

Read more about the game in HideSeek.md