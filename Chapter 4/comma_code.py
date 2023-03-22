def convert_list_to_string(list):
    string_from_list = ''
    for item in list:
        string_from_list += item
    return string_from_list

spam = [
    'apples', 
    'bananas', 
    'tofu', 
    'cats'
]

print(convert_list_to_string(spam))