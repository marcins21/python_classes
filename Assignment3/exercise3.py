# Author Marcin Sitko


def exercise_3_3():
    for i in range(31):
        if i % 3 == 0:
            continue
        print(i)


def exercise_3_4():
    print("\nCALCULATING THE CUBE OF A REAL NUMBER\n")
    while True:
        user_input = input("Enter a number: ")
        if user_input == "stop":
            break
        if user_input.isnumeric():
            result = pow(float(user_input), 3)
            print(f"Your number {user_input} raised to the third power is {result}")
        else:
            print(f"\nYou didn't enter a real number; you entered '{user_input}'")


def exercise_3_5(length: int) -> str:
    dot_number = 4
    ruler = "".join([f"|{'.'*dot_number}" for x in range(length)]) + "|"
    numbers = ""
    for i in range(length + 1):
        spaces = 1 + dot_number - len(str(i + 1))
        numbers += f"{i}" + " " * spaces

    result = f"{ruler}\n{numbers}"
    return result


def exercise_3_6(height: int, width: int) -> str:
    line = "+----"
    pipes = "|    "

    horizontal_line = line * width
    horizontal_line += "+"
    horizontal_pipes = pipes * width
    horizontal_pipes += "|"

    result = horizontal_line + "\n"
    units = 0
    while units != height:
        result += horizontal_pipes + "\n"
        result += horizontal_line + "\n"
        units += 1
    return result


def exercise_3_8(list_a, list_b):
    list_a = set(list_a)
    list_b = set(list_b)
    a = list_a.intersection(list_b)
    b = list_a.union(list_b)

    return list(a), list(b)


def exercise_3_9(lst):
    result = []
    for seq in lst:
        result.append(sum(seq))
    return result


def exercise_3_10(input_user: str):
    roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    arabic_numeral = 0
    prev_value = 0
    for numeral in input_user[::-1]:
        value = roman_values[numeral]
        if value < prev_value:
            arabic_numeral -= value
        else:
            arabic_numeral += value
        prev_value = value
    return arabic_numeral
