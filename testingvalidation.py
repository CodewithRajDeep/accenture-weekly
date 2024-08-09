def print_if_else(num1, num2, num3):


  if num1 >= num2 and num1 >= num3:
    print("num1 is the largest")
  elif num2 >= num1 and num2 >= num3:
    print("num2 is the largest")
  else:
    print("num3 is the largest")

# Test cases with diverse inputs
print_if_else(5, 3, 2)  # Expected output: num1 is the largest
print_if_else(2, 5, 3)  # Expected output: num2 is the largest
print_if_else(3, 2, 5)  # Expected output: num3 is the largest
print_if_else(5, 5, 3)  # Expected output: There is no unique largest number
print_if_else(-2, -5, -3)  # Expected output: num1 is the largest (negative numbers)
print_if_else(0, 0, 0)  # Expected output: There is no unique largest number (all equal)
