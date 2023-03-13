# 1- input first numebr.
first_numebr = float(input("enter first number: "))

# 2- input operation type.
operation = input("enter operation type: ")

# 3- input second number.
second_numebr = float(input("enter second number: "))

# 4- print the result
if operation == "+":
  print(first_numebr + second_numebr)
elif operation == "-":
  print(first_numebr - second_numebr)
elif operation == "*":
  print(first_numebr * second_numebr)
elif operation == "/":
  print(first_numebr / second_numebr)
else:
  print("Error!!!")
