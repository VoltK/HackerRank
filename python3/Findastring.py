def count_substring(string, sub_string):
    counter = 0
    for index in range(len(string)):
        if string[index:index+len(sub_string)] == sub_string:
            counter += 1
    return counter

