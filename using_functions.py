from IPython.display import display, Math

# def compute_remainder(x, y):

#     divis = int(x/y)
#     remainder = x % y

#     print("{} goes into {} {} times with a remainder of {}".format(y, x, divis, remainder))


# numerator = int(input("Please put in a number: "))
# denomenantor = int(input("Please select another number: "))

# compute_remainder(numerator, denomenantor)



def divide(x, y):

    print(display(Math("x^y = %g"), x**y))


def exponent(x, y):

    print(display(Math("x //divide y = %g"), x / y))

    
print("Hello")

first = int( input("Choose a number: "))
second = int ( input("Choose another number: "))


select_operation = int( input(display(Math("Press 1 to compute first^second or 2 to compute first \\divide second"))))

if(select_operation == 1):
    exponent(first, second)
elif(select_operation == 2):
    divide(first, second)
else:
    print("Invalid selection")

