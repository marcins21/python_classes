from typing import List

def make_ruler(n: int) -> str:
    dot_number = 4
    ruler = "".join([f"|{'.' * dot_number}" for x in range(n)]) + "|"
    numbers = ""
    for i in range(n + 1):
        spaces = 1 + dot_number - len(str(i + 1))
        numbers += f"{i}" + " " * spaces

    result = f"{ruler}\n{numbers}"
    return result


def make_grid(cols: int, rows: int) -> str:
    try:
        line = "+----"
        pipes = "|    "

        horizontal_line = line * rows
        horizontal_line += "+"
        horizontal_pipes = pipes * rows
        horizontal_pipes += "|"

        result = horizontal_line + "\n"
        units = 0
        while units != cols:
            result += horizontal_pipes + "\n"
            result += horizontal_line + "\n"
            units += 1
        return result
    except Exception as e:
        raise ValueError(f"Error in make_grid: {str(e)}")


def factorial(n: int) -> int:
    try:
        result = 1
        while n != 1:
            result *= n
            n -= 1
        return result
    except Exception as e:
        raise ValueError(f"Error in factorial: {str(e)}")


def fibonacci(n: int) -> int:
    result = 1
    a = 1
    b = 1
    c = 1
    if n < 3:
        return c
    try:
        while n != 2:
            c = a + b
            a = b
            b = c
            result += c
            n -= 1
        return c
    except Exception as e:
        raise ValueError(f"Error in fibonacci: {str(e)}")


def odwracanie_iter(L: List, left: int, right: int) -> List:
    try:
        while left < right:
            L[left], L[right] = L[right], L[left]
            right -= 1
            left +=  1
        return L
    except Exception as e:
        raise ValueError(f"Error in odwracanie_iter: {str(e)}")


def odwracanie_rek(L: List, left: int, right: int) -> List:
    try:
        if left < right:
            L[left], L[right] = L[right], L[left]
            odwracanie_rek(L, left + 1, right - 1)
        return L
    except Exception as e:
        raise ValueError(f"Error in odwracanie_rek: {str(e)}")


def sum_seq(sequence):
    result = 0
    for i in sequence:
        if isinstance(i, (list, tuple)):
            result += sum_seq(i)
        else:
            result += i
    return result


def flatten(seq, sort=False):
    result = []
    for i in seq:
        if isinstance(i, (list, tuple)):
            result += flatten(i)
        else:
            result.append(i)
    if sort:
        return sorted(result)
    return result
