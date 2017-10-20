# simple factorial function

# Calculate factorial of the input_fac
input_fac = input('deger')

look = 7
# Define the factorial function
def factorial(number):
    result_fac = 1
    for i in range(number):
        result_fac = (number - i) * result_fac
    return result_fac

# Call the factorial function
r = factorial(4)

print(r)

