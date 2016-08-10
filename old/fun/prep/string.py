def reversed(string):
    str_list = list(string)
    size = len(string)
    for i in range(0, int(size/2)):
        tmp = str_list[size-i-1]
        str_list[size-i-1] = str_list[i]
        str_list[i] = tmp

    return ''.join(str_list)

print(reversed('fuck'))
