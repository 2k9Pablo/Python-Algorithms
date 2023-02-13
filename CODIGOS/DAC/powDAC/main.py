'''
POW IMPLEMENTATION 23/12/22
'''
def powDAC(x, y):

    if y == 0:
        return 1
    elif y == 1:
        return x
    else:

        temp = powDAC(x, int(y / 2))

        if y % 2 == 0:
            return temp * temp

        else:
            if y > 0:
                return x * temp * temp
            else:
                return temp * temp / x
