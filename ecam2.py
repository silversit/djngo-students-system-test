#
#
# """integer separated by |"""
# """second line Adventure over """
#
# "Step Backward${start index}${steps}"
# #obo starts moving to the left (backward) from the given start index with the given number of steps.
#
# #vzima itema ot initial stringa i go mahame ot stringa resetvame na 0
#
# #ako izleze ot geiDA se edno zapochva ot zad na pred
# #ako start indeksa is out of rane ignorirame comandata
#
#
# "Step Forward${start index}${steps}"
#
# "Double {index}"
# #Double the value of the item at the given index.
# #If the index is out of bounds, ignore the command.
# "Switch"
# #Reverse the order of the items in the grid.
# "Adventure over"
# #Print the grid and the total items collected.
#
# items = list()
# grid = str(input()).split("|")
#
# def forevard_move(index,steps):
#     steps = int(steps)
#     global grid
#     counter = 0
#     current_index = int(index)
#     item = ""
#     resolver = ""
#     while counter < steps :
#         item = grid[current_index]
#         resolver = current_index
#         current_index += 1
#         counter += 1
#
#         # Reset index if it goes out of the list bounds
#         if current_index >= len(grid) :
#             current_index = 0
#     items.append(item)
#     grid[resolver] = "0"
#     print(grid)
#
# def backword_move(index,steps):
#     global grid,items
#     steps = int(steps)
#     counter = 0
#     current_index = int(index)
#     item = ""
#     resolver = 0
#     while counter < steps :
#         item = grid[current_index]
#         resolver = current_index
#         current_index -= 1
#         counter += 1
#
#
#         # Reset index if it goes out of the list bounds
#         if current_index < 0 :
#             current_index = len(grid) -1
#
#     items.append(item)
#     grid[resolver] = "0"
#     print(grid)
#
# def double_move(index):
#     global grid,items
#     items_count = len(grid)
#     if int(index) > items_count:
#         pass
#     grid[int(index)] = str(int(grid[int(index)])*2)
#
# def switch_move():
#     global grid
#     grid = grid[::-1]
#
# while True:
#     commands = input()
#     if "$" in commands:
#         command, index,steps = commands.split("$")
#     elif commands == "Adventure over":
#         break
#     elif commands == "Switch":
#         command = commands
#     else:
#         command,index = commands.split()
#     if command == "Step Backward":
#         backword_move(index,steps)
#     if command == "Step Forward":
#         forevard_move(index,steps)
#     if command == "Double":
#         double_move(index)
#     if command == "Switch":
#         switch_move()
# print(*grid, sep=" - ")
# print(f"Robo finished the adventure with {sum(int(item) for item in items)} items!")
# print(items)
#
items = list()
grid = str(input()).split("|")


def forevard_move(index, steps) :
    steps = int(steps)
    global grid,items
    current_index = int(index)
    if current_index +1 > len(grid):
        pass
    else:
        for _ in range(steps) :
            current_index += 1
            if current_index >= len(grid) :
                current_index = 0
        items.append(grid[current_index])
        grid[current_index] = "0"



def backword_move(index, steps) :
    global grid, items
    steps = int(steps)
    current_index = int(index)
    if current_index +1 > len(grid):
        pass
    else:
        for _ in range(steps) :
            current_index -= 1
            if current_index < 0 :
                current_index = len(grid) - 1
        items.append(grid[current_index])
        grid[current_index] = "0"



def double_move(index) :
    global grid
    index = int(index)
    if 0 <= index < len(grid) :
        grid[index] = str(int(grid[index]) * 2)


def switch_move() :
    global grid
    grid = grid[: :-1]



while True :
    commands = input()
    if "$" in commands :
        command, index, steps = commands.split("$")
    elif commands == "Adventure over" :
        break
    elif commands == "Switch" :
        command = commands
    else :
        command, index = commands.split()

    if command == "Step Backward" :
        backword_move(index, steps)
    if command == "Step Forward" :
        forevard_move(index, steps)
    if command == "Double" :
        double_move(index)
    if command == "Switch" :
        switch_move()

print(*grid, sep=" - ")
print(f"Robo finished the adventure with {sum(int(item) for item in items)} items!")

