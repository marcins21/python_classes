from typing import List

# Author Marcin Sitko


def exc_2_10(line: str) -> int:
    return len(line.split())


def exc_2_11(word: str) -> str:
    return "_".join([char for char in word])


def exc_2_12(line: str):
    line = line.split()
    first_letters = "".join([word[0] for word in line])
    last_letters = "".join([word[-1] for word in line])
    return first_letters, last_letters


def exc_2_13(line: str) -> int:
    line = line.split()
    result = sum([len(word) for word in line])
    return result


def exc_2_14(line: str) -> tuple:
    line = line.split()
    length_of_words = [len(word) for word in line]
    biggest_length_of_word = max(length_of_words)
    longest_word = line[length_of_words.index(biggest_length_of_word)]
    return longest_word, biggest_length_of_word


def exc_2_15(l: List[int]) -> str:
    result = ""
    for i in l:
        result += str(i)
    return result


def exc_2_16(line: str) -> str:
    str_to_change = "Guido van Rossum"
    str_to_find = "GvR"
    if "GvR" in line:
        line = line.replace(str_to_find, str_to_change)
        return line
    else:
        error = f"{str_to_find} nie wystepuje w tekscie '{line}'"
        return error


def exc_2_17(line: str) -> tuple:
    line = line.split()
    alphabetical_order = " ".join(sorted(line))
    length_order = " ".join(sorted(line, key=len))
    return alphabetical_order, length_order


def exc_2_18(number: int) -> int:
    number = str(number)
    return number.count("0")


def exc_2_19(l: List[int]) -> List[str]:
    list_with_strs = [str(number).zfill(3) for number in l]
    return list_with_strs


class PerformTests:
    def test_exc_2_10(self):
        # ZADANIE 2.10
        # Mamy dany napis wielowierszowy line. Podać sposób obliczenia liczby wyrazów w napisie. Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi znakami (spacja, tabulacja, newline).
        assert exc_2_10("Hello world") == 2
        assert exc_2_10("Lorem ipsum dolor sit amet") == 5
        assert exc_2_10("One") == 1

    def test_exc_2_11(self):
        # ZADANIE 2.11
        # Podać sposób wyświetlania napisu word tak, aby jego znaki były rozdzielone znakiem podkreślenia.
        assert exc_2_11("Python") == "P_y_t_h_o_n"
        assert exc_2_11("Test") == "T_e_s_t"
        assert exc_2_11("12345") == "1_2_3_4_5"

    def test_exc_2_12(self):
        # ZADANIE 2.12
        # Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line. Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.
        assert exc_2_12("This is a test") == ("Tiat", "ssat")
        assert exc_2_12("Another example") == ("Ae", "re")
        assert exc_2_12("One") == ("O", "e")

    def test_exc_2_13(self):
        # ZADANIE 2.13
        # Znaleźć łączną długość wyrazów w napisie line. Wskazówka: można skorzystać z funkcji sum().
        # Znajdowanie dlugosci WYRAZÓW nie uwzględniam znaków białych (spacji tabluratów)
        assert exc_2_13("Python is fun") == 11
        assert exc_2_13("One") == 3

    def test_exc_2_14(self):
        # ZADANIE 2.14
        # Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line.
        assert exc_2_14("Python is a great language") == ("language", 8)
        assert exc_2_14("This is a test") == ("This", 4)
        assert exc_2_14("One") == ("One", 3)

    def test_exc_2_15(self):
        # ZADANIE 2.15
        # Na liście L znajdują się liczby całkowite dodatnie. Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.
        assert exc_2_15([1, 2, 3, 4, 5]) == "12345"
        assert exc_2_15([10, 20, 30]) == "102030"
        assert exc_2_15([0, 9, 8]) == "098"

    def test_exc_2_16(self):
        # ZADANIE 2.16
        # W tekście znajdującym się w zmiennej line zamienić ciąg znaków "GvR" na "Guido van Rossum", @@ dodalem obsluge przypadku gdy "GvR" nie wystepuje w tekscie
        assert (
            exc_2_16("I love programming in GvR")
            == "I love programming in Guido van Rossum"
        )
        assert (
            exc_2_16("This is a test") == "GvR nie wystepuje w tekscie 'This is a test'"
        )
        assert (
            exc_2_16("GvR is the creator of Python")
            == "Guido van Rossum is the creator of Python"
        )

    def test_exc_2_17(self):
        # ZADANIE 2.17
        # Posortować wyrazy z napisu line raz alfabetycznie, a raz pod względem długości. Wskazówka: funkcja wbudowana sorted().
        # Najpierw jest sortowanie pod wzgledlem dlugosci wyrazow,pozniej sortowanie alfabetyczne
        assert exc_2_17("Python is a great language") == (
            "Python a great is language",
            "a is great Python language",
        )
        assert exc_2_17("This is a test") == ("This a is test", "a is This test")

    def test_exc_2_18(self):
        # ZADANIE 2.18
        # Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na napis.
        assert exc_2_18(10203040) == 4
        assert exc_2_18(1234567890) == 1
        assert exc_2_18(0) == 1

    def test_exc_2_19(self):
        # ZADANIE 2.19
        # Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. Chcemy zbudować napis z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami, np. 007, 024. Wskazówka: str.zfill().
        assert exc_2_19([1, 22, 333, 4444, 55555]) == [
            "001",
            "022",
            "333",
            "4444",
            "55555",
        ]
        assert exc_2_19([9, 876, 5432, 10]) == ["009", "876", "5432", "010"]
        assert exc_2_19([7, 888, 6666]) == ["007", "888", "6666"]


# Testy - nie uzyzwalem zadnej biblioteki do wykonywania testow jak np. unitest, pytest uzyłem zwykłego 'assert'
# Jezeli program wykonuje sie bez zadnych Error'ów to oznacza ze testy przeszly prawidłowo
if __name__ == "__main__":
    test_class = PerformTests()
    test_class.test_exc_2_10()
    test_class.test_exc_2_11()
    test_class.test_exc_2_12()
    test_class.test_exc_2_13()
    test_class.test_exc_2_14()
    test_class.test_exc_2_15()
    test_class.test_exc_2_16()
    test_class.test_exc_2_17()
    test_class.test_exc_2_18()
    test_class.test_exc_2_19()
