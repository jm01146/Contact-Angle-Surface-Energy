from sympy import symbols, solve, sqrt
import math


def processing(yl, theta):
    ys = symbols('ys')
    left_hand_equ = yl * (1 + math.cos(theta))
    right_hand_equ = 1.9997886 * sqrt(yl) * sqrt(ys) * (yl**2 - 2*yl*ys + ys**2)
    solution = solve(right_hand_equ - left_hand_equ, ys)
    return solution


print(processing(72.8, 83))