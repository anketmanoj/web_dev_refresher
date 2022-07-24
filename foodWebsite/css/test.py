list1 = [1, 2, 3, 4, 5]
print("The first 5 natural numbers are", list1)


def get_odd_squares(listOfNaturalNumbers):
    odd_squares = []
    for no in listOfNaturalNumbers:
        if no % 2 != 0:
            odd_squares.append(no ** 2)

    return odd_squares


odd_numbers_list = get_odd_squares(list1)

print("Square of odd numbers is", odd_numbers_list)
