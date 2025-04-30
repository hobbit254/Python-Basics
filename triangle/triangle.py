def equilateral(sides):
    if sides[0] == sides[1] == sides[2] and sides[0] != 0 and sides[1] != 0 and sides[2] != 0:
        return True
    else:
        return False


def isosceles(sides):
    a,b,c = sorted(sides)

    if a + b <= c:
        return False
    else:
        if equilateral(sides):
            return True
        elif sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
            return True
        else:
            return False


def scalene(sides):
    a,b,c = sorted(sides)
    if a + b <= c:
        return False
    else:
        if not isosceles(sides) and not equilateral(sides):
            return True
        else:
            return False