def search_recursive(list, item, low=0, high=None):
    if high is None:
        high = len(list) - 1
    
    if low > high:
        return None
    
    mid = (low + high) // 2
    guess = list[mid]

    if guess == item:
        return mid
    elif guess > item:
        return search_recursive(list, item, low, mid - 1)
    else:
        return search_recursive(list, item, mid + 1, high)
    

test_input = [1, 3, 5, 7, 9]
print(search_recursive(test_input, 3))
print(search_recursive(test_input, 7))
print(search_recursive(test_input, 2))