import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, solve


# Sample data
data = {
    'Water': (72.8, .26555),
    'Glycerol': (64, .1279),
    'Ethylene Glycol': (48., .7080)
}

# Extract labels, x, and y values
labels, points = zip(*data.items())
x, y = zip(*points)

# Fit a line (polynomial of degree 1) using numpy's polyfit function
coefficients = np.polyfit(x, y, 1)
poly_fit = np.poly1d(coefficients)

# Generate y values for the line of best fit
line_of_best_fit = poly_fit(x)

# Plot the original data points
plt.scatter(x, y, label='Data Points')

# Annotate each data point with its label
for label, x_point, y_point in zip(labels, x, y):
    plt.text(x_point, y_point, label)

# Plot the line of best fit
plt.plot(x, line_of_best_fit, color='red', label='Line of Best Fit')

# Display the equation of the line of best fit
equation = f'Line of Best Fit: y = {coefficients[0]:.2f}x + {coefficients[1]:.2f}'
plt.text(1, 5, equation, color='red')

# Find the intersection of the line of best fit and y = 1.0
x_symbol = symbols('x')
intersection_x = solve(poly_fit(x_symbol) - 1.0, x_symbol)[0]
intersection_y = poly_fit(intersection_x)

# Mark the intersection point
plt.scatter(intersection_x, intersection_y, color='green', label='Intersection (1.0)')

# Add labels and a legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Show the plot
plt.show()

print(f'Intersection point (1.0): x = {intersection_x:.2f}, y = {intersection_y:.2f}')
