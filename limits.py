import sympy

# Define the variable x
x = sympy.Symbol('x')

# Define the limit expression
expr = input("Enter the limit expression: ")
f = sympy.sympify(expr)

# Evaluate the limit
limit = sympy.limit(f, x, 0)

# Print the result
print("The limit of", expr, "as x approaches 0 is", limit)
