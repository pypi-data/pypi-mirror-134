def find(list, fn):
    for i in range(len(list)):
        if fn(list[i], i):
            return list[i]
    return None
