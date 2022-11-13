# GameDevChallenge
A set of simple game design problems that can be solved in any language.

You do require python, and numpy and pygame modules installed to run the test cases though.
Pre-requisites installations, **linux**:
```
$ sudo apt install python3
$ sudo apt install python3-pip
$ pip3 install numpy
$ pip3 install pygame
```

**windows** \
Refer to WSL.md

**Any other OS** \
If you're using anything else I assume you know what you're doing 

--- 

The challenge directory contains 4 questions in the following order of increasing difficulty
1. SimpleTarget
2. 2limbIK
3. HideSeek
4. Gridrunner

Each problem statement involves a [challenge name]_test.py file which will embed the user solution to the file and simulate a game environment. \
User solution has to be an executable that communicates via stdin and stdout, the specifications of which will be provided with the problem statement. Do note that the solution file has to be in a while-True loop so that it can be queried indefinitely.
More details about the game and the problem statement are each directory.

You can run the test file with your user solution using the following format:
```
$ python3 [challenge name]_test.py solution_executable
```

for example, if your solution is a python3 file called soln1.py, it can be executed using
```
$ python3 [challenge name]_test.py python3 soln1.py
```

If it is a c or c++ file, first compile it into an executable, then execute it.
```
$ g++ soln1.c++ -o soln1
$ python3 [challenge name]_test.py ./soln1
```

Any other languages can be compiled in a similar format.

The source codes to all the test games are in the directory as well. It will not help you much to solve the problem statements as the problem statements are independant of the actual implementation of the games, but feel free to tweak around.

For more details you can contact the YACC game dev heads.

Oh and I was high on life problems while writing a lot of this code so if you find any bugs ping me \
    -Jyo
