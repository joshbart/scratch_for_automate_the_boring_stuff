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

def check_for_streaks(list):
    streaks = 0
    for index, flip_value in enumerate(list):
        if flip_value == 'H':
            compare_list = ['H'] * 6
        else:
            compare_list = ['T'] * 6
        if compare_list == list[index:index + 6]:
            streaks += 1
    return streaks

if __name__ == '__main__':
    number_of_streaks = 0
    for experiment in range(10000):
        coin_flip_list = generate_list_of_coin_flips()
        number_of_streaks += check_for_streaks(coin_flip_list)
    print('Chance of streak: %s%%' % (number_of_streaks / (10000 * 100)))