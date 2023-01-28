set_of_nums = [-4, 6, -1, 43, -18, 2, 0]


for num in set_of_nums: 
    if num < -5 or num > 2:
        print("Absolute value of {} is {}".format(num, abs(num)))
    else:
        print("{} was not tested".format(num))
    