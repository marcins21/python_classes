import random


class IterateInfOneZero:
    def __init__(self):
        self.num = 0
        self.end = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num != 1:
            self.num = 1
            return 0
        self.num = 0
        return 1


class IterateRandomLetter:
    def __init__(self):
        self.letters = ("N", "E", "S", "W")

    def __iter__(self):
        return self

    def __next__(self):
        return random.choice(self.letters)


class IterateRandomDayNumbers:
    def __init__(self):
        self.day_numbers = (0, 1, 2, 3, 4, 5, 6)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        current_number = self.day_numbers[self.index]
        # Adding cycle
        self.index = (self.index + 1) % len(self.day_numbers)
        return current_number


def showing_result():
    iterate01 = IterateInfOneZero()
    iterate_random_letters = IterateRandomLetter()
    iterate_week_days = IterateRandomDayNumbers()

    # Wyniki Pokazuje w petli do 30, tak zeby mogły sie w czytelny sposob wyswietlic w terminalu
    # Oczywiscie pętle iterują sie w nieskonczonosc - "bez zabezpieczenia"
    print("Nieskonczony iterator 0 1 0 1 ...")
    index_01 = 0
    for i in iterate01:
        if index_01 > 30:
            break
        print(i, end=" ")
        index_01 += 1

    print("\nNieskonczony iterator ('N', 'E', 'S', 'W') losowy")
    index_02 = 0
    for i in iterate_random_letters:
        if index_02 > 30:
            break
        print(i, end=" ")
        index_02 += 1

    print("\nNieskonczony iterator numerów dni tygodnia (0,1,2,3,4,5,6)")
    index_03 = 0
    for i in iterate_week_days:
        if index_03 > 30:
            break
        print(i, end=" ")
        index_03 += 1


if __name__ == "__main__":
    showing_result()
