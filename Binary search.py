
def binary_search(some_list, value):
    low = 0
    high = len(some_list) - 1
    count = 0

    while low <= high:
        mid_point = (low + high) // 2
        guess = some_list[mid_point]
        if guess == value:
            count += 1
            print('Amount of steps:', count)
            return mid_point
        elif guess > value:
            count += 1
            high = mid_point - 1
        elif guess < value:
            count += 1
            low = mid_point + 1
    return None


my_list = []
for i in range(10):
    my_list.append(i**2)
print("Value's position:", binary_search(my_list, 5))
