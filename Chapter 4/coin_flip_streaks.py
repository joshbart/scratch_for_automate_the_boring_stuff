def generate_list_of_coin_flips():
    return None

def check_for_streaks():
    return None

if __name__ == '__main__':

    number_of_streaks = 0

    for experiment in range(10000):
        generate_list_of_coin_flips()
        check_for_streaks()

    print('Chance of streak: %s%%' % (number_of_streaks / 100))