from typing import List
from math import gcd

# frac - [numerator, denominator]


def add_frac(frac1: List[int], frac2: List[int]):
    common_den = frac1[1] * frac2[1]
    result_numerator = (frac1[0] * frac2[1]) + (frac2[0] * frac1[1])
    greates_common_divisor = gcd(result_numerator, common_den)
    if common_den == 0:
        return "unknown"
    elif result_numerator == 0:
        return 0
    return [
        result_numerator // greates_common_divisor,
        common_den // greates_common_divisor,
    ]


def sub_frac(frac1: List[int], frac2: List[int]):
    common_den = frac1[1] * frac2[1]
    result_numerator = (frac1[0] * frac2[1]) - (frac2[0] * frac1[1])
    greates_common_divisor = gcd(result_numerator, common_den)
    if common_den == 0:
        return "unknown"
    elif result_numerator == 0:
        return 0
    return [
        result_numerator // greates_common_divisor,
        common_den // greates_common_divisor,
    ]


def mul_frac(frac1: List[int], frac2: List[int]):
    result_numerator = frac1[0] * frac2[0]
    result_den = frac1[1] * frac2[1]
    greates_common_divisor = gcd(result_numerator, result_den)
    if result_den == 0:
        return "unknown"
    elif result_numerator == 0:
        return 0
    return [
        result_numerator // greates_common_divisor,
        result_den // greates_common_divisor,
    ]


def div_frac(frac1: List[int], frac2: List[int]):
    result_numerator = frac1[0] * frac2[1]
    result_den = frac1[1] * frac2[0]
    greates_common_divisor = gcd(result_numerator, result_den)
    if result_den == 0:
        return "unknown"
    elif result_numerator == 0:
        return 0
    return [
        result_numerator // greates_common_divisor,
        result_den // greates_common_divisor,
    ]


def is_positive(frac: List[int]) -> bool:
    return (frac[0]) > 0 and (frac[1] > 0)


def is_zero(frac: List[int]) -> bool:
    return frac[0] == 0


def cmp_frac(frac1: List[int], frac2: List[int]):
    frac_1 = frac1[0] * frac2[1]
    frac_2 = frac2[0] * frac1[1]

    if frac_1 > frac_2:
        return -1
    elif frac_1 < frac_2:
        return 1
    else:
        return 0


def frac2float(frac: List[int]):
    return frac[0] / frac[1]


# print(add_frac([1,9],[3,27]))
# print(sub_frac([1,9],[3,27]))
# print(sub_frac([1, 17], [81, 27]))
# print(mul_frac([0,1],[3,27]))
# print(div_frac([1,9],[3,27]))
# print(cmp_frac([1,27],[1,81]))
# print(frac2float([10,4]))
