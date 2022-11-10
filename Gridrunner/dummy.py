import random

while True:
    rows,columns = map(int, input().split())

    grid = []

    for i in range(rows):
        grid.append(input().split())

    print(random.choice([0,1,2,3])) #Returns a random directions