
import numpy as np

# 1. Create two NumPy arrays
array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([2, 4, 5, 8, 10])

# 2. Display the arrays
print("NUMPY ARRAY OPERATIONS")
print("-" * 35)

print("Array 1:", array1)
print("Array 2:", array2)

# 3. Check the shape of both arrays
print("\nARRAY SHAPES")
print("Shape of Array 1:", array1.shape)
print("Shape of Array 2:", array2.shape)

# 4. Perform addition
addition = array1 + array2
print("\nADDITION")
print("Array 1 + Array 2 =", addition)

# 5. Perform subtraction
subtraction = array1 - array2
print("\nSUBTRACTION")
print("Array 1 - Array 2 =", subtraction)

# 6. Perform multiplication
multiplication = array1 * array2
print("\nMULTIPLICATION")
print("Array 1 * Array 2 =", multiplication)

# 7. Perform division
division = array1 / array2
print("\nDIVISION")
print("Array 1 / Array 2 =", division)

# 8. Explain vectorized operations
print("\nVECTORIZED OPERATIONS")
print(
    "NumPy performs arithmetic operations on corresponding "
    "array elements without requiring an explicit Python loop."
)
