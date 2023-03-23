#!/usr/bin/env python

grid = [
    ['.', '.', '.', '.', '.', '.'], 
    ['.', 'O', 'O', '.', '.', '.'], 
    ['O', 'O', 'O', 'O', '.', '.'], 
    ['O', 'O', 'O', 'O', 'O', '.'], 
    ['.', 'O', 'O', 'O', 'O', 'O'], 
    ['O', 'O', 'O', 'O', 'O', '.'], 
    ['O', 'O', 'O', 'O', '.', '.'], 
    ['.', 'O', 'O', '.', '.', '.'], 
    ['.', '.', '.', '.', '.', '.']
]

def print_picture(pattern):
    y = 0
    while y < len(pattern[0]):
        for x in pattern:
            print(x[y], end='')
        print()
        y += 1

if __name__ == '__main__':
    print_picture(grid)
