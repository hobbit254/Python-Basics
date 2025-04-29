def is_armstrong_number(number):
    size = len(str(number))
    total = 0

    for i in range(size):
        num = int(str(number)[i])
        total += pow(num, size)

    if total == number:
        return True
    else:
        return False
