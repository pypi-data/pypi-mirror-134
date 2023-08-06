def indexof(list, value):
    for i, v in enumerate(list):
        if v == value:
            return i
    return -1