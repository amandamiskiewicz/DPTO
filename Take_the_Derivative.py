def derive(coefficient, exponent):
    new_coefficient = coefficient * exponent
    new_exponent = exponent - 1
    if new_exponent == 0:
        return str(new_coefficient)
    elif new_exponent == 1:
        return str(new_coefficient) + "x"
    else:
        return str(new_coefficient) + "x^" + str(new_exponent)

    pass