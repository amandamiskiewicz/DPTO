def integrate(coefficient, exponent):
    new_coefficient = coefficient // (exponent + 1)
    new_exponent = exponent + 1
    return str(new_coefficient) + "x^" + str(new_exponent)
    pass