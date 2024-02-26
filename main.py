import math

# Define angles in degrees
angles_degrees = [83, 72.4, 72.3, 70.5]

equation_1 = []
test = []

# Output 1 + cos(degrees) for each angle
for angle_degrees in angles_degrees:
    angle_radians = math.radians(angle_degrees)
    test.append(angle_radians)
    result = 72.8 * (1 + math.cos(angle_radians))
    equation_1.append(result)

print(test)
print(equation_1)