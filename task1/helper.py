def b_sort(lst, key = None, reverse = False):
    if key:
        if reverse:
            for i in range (len(lst)):
                for j in range(i + 1, len(lst)):
                    if key(lst[i]) < key(lst[j]):
                        temp = lst[i]
                        lst[i] = lst[j]
                        lst[j] = temp
        else:
            for i in range (len(lst)):
                for j in range(i + 1, len(lst)):
                    if key(lst[i]) > key(lst[j]):
                        temp = lst[i]
                        lst[i] = lst[j]
                        lst[j] = temp

    else:
        if reverse:
            for i in range (len(lst)):
                    for j in range(i + 1, len(lst)):
                        if lst[i] < lst[j]:
                            temp = lst[i]
                            lst[i] = lst[j]
                            lst[j] = temp
        else:
            for i in range (len(lst)):
                    for j in range(i + 1, len(lst)):
                        if lst[i] > lst[j]:
                            temp = lst[i]
                            lst[i] = lst[j]
                            lst[j] = temp

def uppercase(string):
    new_string = ""
    for character in string:
        ascii_value = ord(character)
        if ascii_value > 96 and ascii_value < 123:
            new_string += chr(ascii_value - 32)
        else:
            new_string += character
    return new_string