from typing import List


# Jezeli dlugosc liczby na miarce sie zwieksza, trzeba zadbac o to by odleglosci pomiedzy kolejnymi liczbami byly mniejsze
# PRZYKLAD -  0    1    2 ...  (4 spacje odstępu)   10   11   12 ...  (3 spacje)  100  101  102 ... (2 spacje)
# Wtedy liczba zawsze bedzie znajdowac sie po znakiem "|"
# oczywiscie to wszystko przy zalozeniu ze linijka posiada 4 znaki '.' oraz dwa znaki '|' w kazdym segmencie przy innych zalozeniach trzeba dostosowac zmienna offset
def make_ruler(n: int) -> str:
    try:
        result = ""
        unit = "|...."
        for i in range(n):
            result += unit
        result += "|"

        spaces = {}
        off_set = 4

        for i in range(n + 1):
            if len(str(i)) > len(str(i - 1)):
                off_set -= 1
            spaces[i] = off_set

        numbers = ""
        for k, v in spaces.items():
            numbers += f"{k}" + (" " * v)

        result += "\n" + numbers

        return result
    except Exception as e:
        raise ValueError(f"Error in make_ruler: {str(e)}")


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
        for i in range(left, (right + 1) // 2):
            L[i], L[right - i] = L[right - i], L[i]
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


class PerformTests:
    def test_factorial(self):
        assert factorial(5) == 120
        assert factorial(6) == 720

    def test_fibonacci(self):
        assert fibonacci(6) == 8
        assert fibonacci(7) == 13

    def test_odwracanie_iter(self):
        assert odwracanie_iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 4) == [
            5,
            4,
            3,
            2,
            1,
            6,
            7,
            8,
            9,
            10,
        ]

    def test_odwracanie_rek(self):
        assert odwracanie_rek([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 4) == [
            5,
            4,
            3,
            2,
            1,
            6,
            7,
            8,
            9,
            10,
        ]

    def test_sum_seq(self):
        assert sum_seq([1, 2, [3, 3, [1, 2, 3]]]) == 15

    def test_flatten(self):
        seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
        assert flatten(seq) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert flatten([1, 2, [3, 3, [1, 2, 3]]], sort=True) == [1, 1, 2, 2, 3, 3, 3]
        assert flatten([1, 2, [3, 3, [1, 2, 3]]]) == [1, 2, 3, 3, 1, 2, 3]


# Jezeli program wykonuje sie bez zadnych błedów, oznacza to ze testy przeszly prawidłowo
if __name__ == "__main__":
    Test = PerformTests()

    print("\nFunkcje make_ruler i make_grid")
    print(make_ruler(10))
    print(make_ruler(20))
    print(make_grid(2, 4))

    print("Funkcja factorial (iteracyjnie)")
    Test.test_factorial()
    print("Funkcja Fibonacci (iteracyjnie)")
    Test.test_fibonacci()
    print("Funkcja odwracanie_iter (iteracyjnie)")
    Test.test_odwracanie_iter()
    print("Funkcja odwracanie_rek (rekurencyjnie)")
    Test.test_odwracanie_rek()
    print("Funcja sum_seq")
    Test.test_sum_seq()
    print("Funkcja flatten (dodalem parametr sort)")
    Test.test_flatten()
