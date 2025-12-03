def max(list):
    if len(list) == 0:
        return None
    if len(list) == 1:
        return list[0]
    else:
        max_num = max(list[1:])
        return list[0] if list[0] > max_num else max_num