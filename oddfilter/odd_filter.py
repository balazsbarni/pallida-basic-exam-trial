# Create a function that takes a list as a parameter,
# and returns a new list with every odd number from the orignal list
# example: [1, 2, 3, 4, 5] should produce [1, 3, 5]

#print(odd_filter([1, 2, 3, 4, 5]))  # should print [1, 3, 5]

list_to_filter = [ 1, 2, 3, 4, 5, 6]


def odd_filter(input_list):
    odd_list = []
    for items in input_list:
        if items % 2 > 0:
            odd_list.append([items])
    return odd_list


print(odd_filter(list_to_filter))

