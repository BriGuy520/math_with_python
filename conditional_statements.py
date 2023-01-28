from IPython.display import display, Math

for i in range(4):
    for j in range(5):
        if i > 0 and j > 0:
            display(Math("%g^%g = %g"),i,-j, i**(-j))