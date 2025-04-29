def square(number):
    if number < 1 or number > 64:
        raise ValueError('square must be between 1 and 64')

    if number == 1:
        return number
    new_number = number - 1
    return pow(2, new_number)


def total():
    total_sum: int = 0
    for i in range(1, 65):
        total_sum += square(i)

    return total_sum
