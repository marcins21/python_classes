from typing import List

# Author Marcin Sitko


def exercise_2_10(line: str) -> int:
    return len(line.split())


def exercise_2_11(word: str) -> str:
    return "_".join([char for char in word])


def exercise_2_12(line: str):
    line = line.split()
    first_letters = "".join([word[0] for word in line])
    last_letters = "".join([word[-1] for word in line])
    return first_letters, last_letters


def exercise_2_13(line: str) -> int:
    line = line.split()
    result = sum([len(word) for word in line])
    return result


def exercise_2_14(line: str) -> tuple:
    line = line.split()
    length_of_words = [len(word) for word in line]
    biggest_length_of_word = max(length_of_words)
    longest_word = line[length_of_words.index(biggest_length_of_word)]
    return longest_word, biggest_length_of_word


def exercise_2_15(l: List[int]) -> str:
    result = ""
    for i in l:
        result += str(i)
    return result


def exercise_2_16(line: str) -> str:
    str_to_change = "Guido van Rossum"
    str_to_find = "GvR"
    if "GvR" in line:
        line = line.replace(str_to_find, str_to_change)
        return line
    else:
        error = f"{str_to_find} Doesn't exists in text '{line}'"
        return error


def exercise_2_17(line: str) -> tuple:
    line = line.split()
    alphabetical_order = " ".join(sorted(line))
    length_order = " ".join(sorted(line, key=len))
    return alphabetical_order, length_order


def exercise_2_18(number: int) -> int:
    number = str(number)
    return number.count("0")


def exercise_2_19(l: List[int]) -> List[str]:
    list_with_strs = [str(number).zfill(3) for number in l]
    return list_with_strs
