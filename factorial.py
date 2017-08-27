# simple factorial function
input_fac = 6


def factorial(number):
    result_fac = 1
    for i in range(number):
        result_fac = (number - i) * result_fac
    return result_fac

r = factorial(input_fac)

print(r)