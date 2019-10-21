#!/usr/bin/env python3

import random

def print_grid(grid, attrs, people):
    for k in range(len(grid)):
        print('   |',end='')
        for j in range(len(people)):
            print((attrs[k] + people[j]).rjust(3) + '|', end='')
        print()
        for j in range(len(grid[k])):
            print(('P' + people[j]).rjust(3) + '|', end='')
            for i in range(len(grid[k][j])):
                print(grid[k][j][i].rjust(3) + '|', end='')
            print()
        print()

def y_count(grid, board_ind=None, row=None, col=None):
    count = 0

    if (board_ind is None):
        for k in range(len(grid)):
            count += y_count(grid, k)
    elif (row is None and col is None):
        for j in range(len(grid[board_ind])):
            count += y_count(grid, board_ind, j)
    elif (row is not None and col is None):
        for i in range(len(grid[board_ind][row])):
            if (grid[board_ind][row][i] == 'Y'):
                count += 1
    elif (row is None and col is not None):
        for j in range(len(grid[board_ind])):
            if (grid[board_ind][j][col] == 'Y'):
                count += 1

    return count

def initialize_grid(grid):
    for k in range(len(grid)):
        key = [i for i in range(len(grid[k]))]
        random.shuffle(key)
        for j in range(len(grid[k])):
            grid[k][j][key[j]] = 'Y'

def delete_initial_ys(grid):
    for k in range(len(grid)):
        key = random.randint(0, len(grid[k])-1)
        for i in range(len(grid[k][key])):
            if (grid[k][key][i] == 'Y'):
                grid[k][key][i] = ' '

def delete_unknown_ns(grid, board_ind, row, col):
    for i in range(len(grid[board_ind][row])):
        if (y_count(grid, board_ind, col=i) == 0):
            grid[board_ind][row][i] = ' '
    for j in range(len(grid[board_ind])):
        if (y_count(grid, board_ind, row=j) == 0):
            grid[board_ind][j][col] = ' '

def gen_clue(grid, attrs):
    clue_type = random.randint(0, 2)
    clue = ''

    board_ind = random.choice([k for k in range(len(grid)) if (y_count(grid,k) > 0)])
    row = random.choice([j for j in range(len(grid[board_ind])) if (y_count(grid, board_ind, j) > 0)])
    col = 0
    for i in range(len(grid[board_ind][row])):
        if (grid[board_ind][row][i] == 'Y'):
            col = i

    if (clue_type == 0):
        #Not these things / This or that (same player)
        #Can be horizontal or vertical
        ys = y_count(grid,board_ind) - 1
        if (ys == 0):
            return

        #delete Y and unknown ns
        grid[board_ind][row][col] = ' '
        delete_unknown_ns(grid, board_ind, row, col)
        if (ys >= len(grid[board_ind])/2):
            #Mostly filled up
            #Use Not these things mode
            if (random.randint(0,1) == 0):
                #Horizontal mode
                blanks = [attrs[board_ind]+str(i) for i in range(len(grid[board_ind][row])) if (i != col and grid[board_ind][row][i] == ' ')]
                return 'P' + str(row) + ' does not have ' + ','.join(blanks)
            else:
                #Vertical mode
                blanks = ['P'+str(j) for j in range(len(grid[board_ind])) if (j != row and grid[board_ind][j][col] == ' ')]
                return ','.join(blanks) + ' do not have ' + attrs[board_ind] + str(col)
        else:
            #Mostly empty
            #Use This or that mode
            if (random.randint(0,1) == 0):
                #Horizontal mode
                filled = [attrs[board_ind]+str(i) for i in range(len(grid[board_ind][row])) if (i != col and grid[board_ind][row][i] == 'n')]
                filled.append(attrs[board_ind]+str(col))
                return 'P' + str(row) + ' has either ' + ','.join(filled)
            else:
                #Vertical mode
                filled = ['P'+str(j) for j in range(len(grid[board_ind])) if (j != row and grid[board_ind][j][col] == 'n')]
                filled.append('P'+str(row))
                return 'Either ' + ','.join(filled) + ' has ' + attrs[board_ind] + str(col)

    elif (clue_type == 1):
        #This or that mode
        if (y_count(grid) == 1):
            return

        grid[board_ind][row][col] = ' '
        delete_unknown_ns(grid, board_ind, row, col)

        statements = []
        for i in range(2):
            #Find partner for false information
            board_ind_2 = random.choice([k for k in range(len(grid)) if (y_count(grid, k) > 0)])
            row_2 = random.choice([j for j in range(len(grid[board_ind_2])) if (j != row)])
            col_2 = random.choice([i for i in range(len(grid[board_ind_2][row_2])) if (grid[board_ind_2][row_2][i] == 'n')])
            statements.append('P' + str(row_2) + ' has ' + attrs[board_ind_2] + str(col_2))

        truth = 'P' + str(row) + ' has ' + attrs[board_ind] + str(col)

        
        if (random.randint(0, 1) == 0 and statements[0] != statements[1]):
            statements.append(truth)
            random.shuffle(statements)
            return 'Either ' + ' or '.join(statements)
        else:
            if (random.randint(0, 1) == 0):
                return 'Either ' + truth + ' or ' + statements[0]
            else:
                return 'Either ' + statements[0] + ' or ' + truth

    else:
        #The thing of this is that mode
        #This same player must have other Ys
        #Find preclause statement
        board_ind_2 = [k for k in range(len(grid)) if (k != board_ind and y_count(grid, k, row) > 0)]
        if (board_ind_2 is None or len(board_ind_2) == 0):
            return
        else:
            board_ind_2 = random.choice(board_ind_2)

        grid[board_ind][row][col] = ' '
        delete_unknown_ns(grid, board_ind, row, col)

        #Get our preclause's column
        col_2 = 0
        for i in range(len(grid[board_ind_2][row])):
            if (grid[board_ind_2][row][i] == 'Y'):
                col_2 = i

        return 'The player who has ' + attrs[board_ind_2] + str(col_2) + ' also has ' + attrs[board_ind] + str(col)
    
        
    print('Sumting Wong')


attributes = ['W', 'L', 'M']
people = [str(i) for i in range(10)]

grid = [[['n' for i in range(len(people))] for j in range(len(people))] for k in range(len(attributes))]

if (y_count(grid) == 0):
    initialize_grid(grid)

print_grid(grid, attributes, people)
print(grid)

#Print key
print()
print('Answer key:')
for j in range(len(people)):
    print('Answer: P' + str(j) + ' has ', end='')
    attrs = []
    for k in range(len(attributes)):
        for i in range(len(grid[k][j])):
            if (grid[k][j][i] == 'Y'):
                attrs.append(attributes[k] + str(i))
    print(','.join(attrs))
print()

delete_initial_ys(grid)

while (y_count(grid) > 1):
    clue = gen_clue(grid, attributes)
    if (clue is not None):
        print(clue)

#Make the first clue
for k in range(len(grid)):
    for j in range(len(grid[k])):
        for i in range(len(grid[k][j])):
            if (grid[k][j][i] == 'Y'):
                print('P' + str(j) + ' has ' + attributes[k] + str(i))

