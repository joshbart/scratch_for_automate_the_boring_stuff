def convert_list_to_string(list):
    string_from_list = ''
    for index, item in enumerate(list):
        if index == (len(list) - 1):
            string_from_list += 'and %s.' % item
        else:
            string_from_list += '%s, ' % item
    return string_from_list

# spam = ['apples', 'bananas', 'tofu', 'cats']
# spam = []
spam = [1, 2, 3, 4, 5]

print(convert_list_to_string(spam))