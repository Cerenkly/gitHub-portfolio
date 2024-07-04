from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

while True:
    user_input = input("What's your equation? > ")
    tokens = user_input.split()

    if "q" in tokens:
        break

    if len(tokens) < 2:
        print("Not a full equation.")
        continue
    
    operator = tokens[0]
    operands = tokens[1:]

    if operator not in ["+", "-", "*", "/", "square", "cube", "pow", "mod", "x+", "cubes+"]:
        print("Unsupported operator.")
        continue

    if any(not is_number(num) for num in operands):
        print("Please enter numbers.")
        continue

    nums = list(map(float, operands))

    if operator == "+":
        result = add(*nums)

    elif operator == "-":
        result = subtract(*nums)
    
    elif operator == "*":
        result = multiply(*nums)
    
    elif operator == "/":
        if nums[1] == 0:
            result = "Division by zero error."
        else:
            result = divide(nums[0], nums[1])

    elif operator == "square":
        if len(nums) != 1:
            result = "square operation requires exactly one number."
        else:
            result = square(nums[0])

    elif operator == "cube":
        if len(nums) != 1:
            result = "cube operation requires exactly one number."
        else:
            result = cube(nums[0])

    elif operator == "pow":
        if len(nums) != 2:
            result = "pow operation requires exactly two numbers."
        else:
            result = power(nums[0], nums[1])

    elif operator == "mod":
        if len(nums) != 2:
            result = "mod operation requires exactly two numbers."
        elif nums[1] == 0:
            result = "Division by zero error in mod operation."
        else:
            result = mod(nums[0], nums[1])

    elif operator == "x+":
        if len(nums) != 3:
            result = "x+ operation requires exactly three numbers."
        else:
            result = nums[0] + nums[1] * nums[2]

    elif operator == "cubes+":
        if len(nums) != 2:
            result = "cubes+ operation requires exactly two numbers."
        else:
            result = nums[0]**3 + nums[1]**3

    print(result)

