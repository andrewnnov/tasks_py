# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
# then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

import math


def reverse_int(x: int):
    if x >= 2 ** 31 -1 and x <= -2 ** 31 and x == 0:
        return 0

    if x > 0:
        number_in_str = str(x)
        list_of_number = []
        list_of_number[:0] = number_in_str
        print(list_of_number)

        for i in range(0, len(list_of_number)//2):
            temp = list_of_number[i]
            list_of_number[i] = list_of_number[len(list_of_number) - 1 - i]
            list_of_number[len(list_of_number) - 1 - i] = temp

        print(list_of_number)
        new_number = int("".join(list_of_number))
        return new_number


print(reverse_int(123456789))