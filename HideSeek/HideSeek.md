
# HideSeek

A simple 2 player game where hiders and seekers move around in a grid, the seeker trying to keep the hider in sight and the hider trying for the opposite.

Controls: \
Arrow keys to move the seeker \
wasd to move the hider

If the hider is seeing the seeker, a line will be drawn between them. \
Whenever the hider is being seen, their colour will keep fading to black, similarly when the hider is not being seen, the colour of the seeker will keep fading to black. \
Whichever turns fully black first looses.

----

To run:
```
$ python3 HideSeek_test.py [solution_executable]
```
To change grid,
```
$ python3 HideSeek_test.py [solution_executable] --file=[path to grid]
```
For example, to play on grid/grid2, using the dummy solution,
```
$ python3 HideSeek_test.py python3 dummy.py --file=grids/grid2
```
