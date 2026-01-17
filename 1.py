import sys

if len(sys.argv) == 3:
    script_name = sys.argv[0]
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
else:
    script_name = "arithmetic operations"
    num1 = 10
    num2 = 5

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print("Number 1:", num1)
print("Number 2:", num2)
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)