from IPython.display import display, Math

x = 5 
y = 5.1

print("{:.2f}".format(x**(3/4) * 4**y))
print("{:.8f}".format(3**3 / x**y))
print(10**(x - 4))

display(Math("{x}^(3/4) * 4^y"))
display(Math("3^3 * x^y"))
display(Math("10^({x} - 4)"))

# adding comment







