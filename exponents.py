from IPython.display import display, Math

x = 5 
y = 5.1

answer_one = "{:.2f}".format(x**(3/4) * 4**y)
answer_two = "{:.8f}".format(3**3 / x**y)
answer_three = 10**(x - 4)

display(Math("x^{3/4} \\times 4^y = %g"), answer_one)
display(Math("3^3 \\times x^y = %g"), answer_two)
display(Math("10^{x - 4} = %g"), answer_three)







