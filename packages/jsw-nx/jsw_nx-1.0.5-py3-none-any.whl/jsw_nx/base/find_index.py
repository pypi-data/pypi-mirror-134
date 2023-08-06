def find_index(list, fn):
    for i in range(len(list)):
        if fn(list[i], i):
            return i
    return -1
