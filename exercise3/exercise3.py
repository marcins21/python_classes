
                        # --------ZADANIE 3_1-----------

#Ten kod jest poprawny składniowo
#           x = 2
#           y = 3
#           if x > y:
#               result = x
#           else:
#               result = y

#Ten kod także jest poprawny składowniowo
#           for i in "axby": print(ord(i) if ord(i) < 100 else i)

#Tutaj print(i) powinno byc przez instrukcja warunkową if , dodatkowo nie ma instrukcji else
#           for i in "axby": if ord(i) < 100 print(i)



                        #-------------ZADANIE 3_2------------

# Tutaj mamy tylko dwie zmienne, x i y natomiast chcemy im przypisac az 3 liczby
#KOD
#       x, y = 1, 2, 3

# przypisanie nie tworzy listy tylko tuple tzn : X=(1,2,3)
# tuple jest unmutable to znaczy ze nie mozemy zmieniac jej zawartosci dlatego ponizsza akcja nie moze zostac wykonana
#KOD
#     X = 1, 2, 3
#     X[1] = 4


# X=[1,2,3] , X[3] = 4 jest jak najbrdziej poprawne natomiast, natomiast string takze jest unmutable w rozumieniu jako tablica
# chyba ze uzyjemy metody .split() a potem ''.join() zamiast X.append("d") mozemy wykonac X+="d" otrzymamy wtedy 'abcd'
# #KOD
#           X = [1, 2, 3]
#           X[3] = 4
#           X = "abc"
#           X.append("d")

#Poprawniony kod
#           X=[1,2,3]
#           X[3] = 4
#           X="abc"
#           X+='d'


#Tutaj bledem jest przypisanie L=L.sort() z racji ze .sort() zwraca typ None potem mapuje typ None a nie liste
# nalezy uzyc tutaj zamiast L=L.sort() -> L.sort() wtedy nasza lista jest zmodyfikowanai zachownay jest jej typ
# dodatkowo lazey zmienic konstrukcje samej metody map() z L = list(map(pow, range(8))) na L = list(map(pow, L, range(8)))
# poniewaz nie podajemy na jakiej liscie ma byc to wykonane tylko przypisujemy wynik do naszje listy
# dodatkowo funkcja range(int) zaczyna liczenie od 0 takze pierwszy element naszej listy bedzie równy 1
#KOD
#           L = [3, 5, 4]
#           L = L.sort()
#           L = list(map(pow, range(8)))
# Poprawiony KOD
#            L=[3,5,4]
#           L.sort()
#           L = list(map(pow,L,range(1,8)))
#           lub mozemy uzyc range(8) jezeli faktycznie chcemy zaczynac potegowanie od 0



def exc_3_3():
    for i in range(31):
        if i % 3 == 0:
            continue
        print(i)

def exc_3_4():
    print("\nOBLICZANIE TRZECIEJ POTEGI LICZBY RZECZYWISTEJ\n")
    while True:
        user_input = input("Podaj liczbe: ")
        if user_input == "stop":
            break
        if user_input.isnumeric():
            result = pow(float(user_input),3)
            print(f"Twoja liczba {user_input} podniesiona do trzeciej potegi wynosi {result}")
        else:
            print(f"\nNie podales liczby rzeczywistej tylko '{user_input}'")








exc_3_4()