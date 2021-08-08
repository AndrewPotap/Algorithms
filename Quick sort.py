
def quick_sort(list):
    if len(list) < 2:
        return list
    else:
        fundamental_point = list[0]
        smaller = [i for i in list[1:] if i <= fundamental_point]
        bigger = [i for i in list[1:] if i > fundamental_point]
        return quick_sort(smaller) + [fundamental_point] + quick_sort(bigger)


my_list = [1, 3, 5, 2, 4, 6, 1, 10, 0]
print(quick_sort(my_list))
