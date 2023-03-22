my_pets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name: ',end='')
name = input()
if name not in my_pets:
    print('I do not have a pet named %s.' % name)
else:
    print('%s is my pet.' % name)