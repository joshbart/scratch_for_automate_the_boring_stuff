cat_names = []
while True:
    print('Enter the name of cat ' + str(len(cat_names) + 1) + ' (Or press enter to stop): ', end='')
    name = input()
    if name == '':
        break
    cat_names = cat_names + [name]          # list concatenation
print('The cat names are: ')
for cat in cat_names:
    print(' ' + cat)