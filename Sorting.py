
def find_smallest(list):
    smallest = list[0]
    smallest_index = 0
    for i in range(len(list)):
        if list[i] < smallest:
            smallest = list[i]
            smallest_index = i
    return smallest_index


def find_biggest(list):
    biggest = list[0]
    biggest_index = 0
    for i in range(len(list)):
        if list[i] > biggest:
            biggest = list[i]
            biggest_index = i
    return biggest_index


def sorting_smallest(list):
    sorted_list_smallest = []
    for _ in range(len(list)):
        smallest = find_smallest(list)
        sorted_list_smallest.append(list.pop(smallest))
    return sorted_list_smallest


def sorting_biggest(list):
    sorted_list_biggest = []
    for _ in range(len(list)):
        biggest = find_biggest(list)
        sorted_list_biggest.append(list.pop(biggest))
    return sorted_list_biggest


my_list = [1, 3, 5, 7, 8, 6, 4, 2]
print(sorting_smallest(my_list[:]))  # Need to use copy of the my_list, because object LIST can be changed; if you
# need to use same list for both sorting functions
print(sorting_biggest(my_list))
