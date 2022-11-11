# Grid Runner
**Controls:** \
Arrow keys to move the player

**Rules**: \
There are 2 players, and 1 orb. \
A player gets powered up if they eat an orb. \
A powered up player can eat the other player. \
A powered up player powers down after 10 moves, the orb regenerates in the next move. \
Last player standing wins.

----

To run:
```
$ python3 Gridrunner_test.py [solution_executable]
```
To change grid,
```
$ python3 Gridrunner_test.py [solution_executable] --file=[path to grid]
```
For example, to play on grid/grid2, using the dummy solution,
```
$ python3 Gridrunner_test.py python3 dummy.py --file=grids/grid2
```

