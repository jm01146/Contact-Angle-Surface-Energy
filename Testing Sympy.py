from sympy import symbols, solve, sqrt

ys = symbols('ys')

x = sqrt(ys) * (72.8 - ys)**2

sol = solve(x - 4.786564127, ys)
print(sol)
