
def fast_sorting(list):
    sum = 0
    for i in list:
        sum += i
    return sum


def recursion_element_amount(my_list):
    if my_list != []:
        return 1 + recursion_element_amount(my_list[1:])
    return 0


def biggest_number(list):
    index = 0
    for i in list:
        if i > index:
            index = i
    return index


my_list = [1, 2, 3, 6, 7, 8, 10, 2, 3]
print(fast_sorting(my_list))
print(recursion_element_amount(my_list))
print(biggest_number(my_list))
