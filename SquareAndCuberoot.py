import math

num = int(input("Please Enter The Number: "))

squareRoot = num ** 0.5
squareRoot1 = math.sqrt(num)
cubeRoot = num ** (1/3)
cubeRoot1 = math.cbrt(num)

print("--------------Printing The Output----------------------")
print(f"Square Root of {num} By Using Math Function: ", squareRoot1)
print(f"Square root of {num} : ", squareRoot)
print(f"Cube root of {num} : ", cubeRoot)
print(f"Cube Root of {num} By Using Math Function: ", cubeRoot1)
print("------------------------------------------------------")

