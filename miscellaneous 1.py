import sympy

m=1
x = (( m + 3 )**3+1)/(3*m)
x.is_integer()

while m<=10:
    x = (( m + 3 )**3+1)/(3*m)
    print(m, x, x.is_integer())
    m += 1