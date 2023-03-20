import sys

def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

def ask_for_int():
    print('Please input a number to run through the Collatz sequence: ', end='')
    try:
        input_number = int(input())
    except ValueError:
        print('ERROR - not a valid integer.')
        input_number = ask_for_int()
    return input_number

print('COLLATZ SEQUENCE CALCULATOR')
collatz_number = ask_for_int()
while collatz_number != 1:
    collatz_number = collatz(collatz_number)