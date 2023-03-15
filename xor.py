#!/usr/bin/env python

import sys

def truth_value(arg):
    if arg == 'True':
        return True
    elif arg == 'False':
        return False
    else:
        print('Error: not a truth value.')
        exit(1)

def xor():
    p = truth_value(sys.argv[1])
    q = truth_value(sys.argv[2])

    mid_nand = not (p and q)
    left_nand = not (p and mid_nand)
    right_nand = not (mid_nand and q)
    final_nand = not (left_nand and right_nand)

    return final_nand

if __name__ == "__main__":
    print(xor())
