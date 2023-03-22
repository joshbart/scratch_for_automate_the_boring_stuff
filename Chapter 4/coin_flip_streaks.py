import random

def generate_list_of_coin_flips():
    list = []
    index = 0
    while index < 100:
        index += 1
        flip = random.randint(0, 1)
        if flip == 0:
            list.append('H')
        else:
            list.append('T')
    return list

def check_for_streaks():
    return None

if __name__ == '__main__':

    number_of_streaks = 0

    for experiment in range(10000):
        coin_flip_list = generate_list_of_coin_flips()
        check_for_streaks()
        
    print('Chance of streak: %s%%' % (number_of_streaks / 100))