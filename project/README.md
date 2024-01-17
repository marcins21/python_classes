# Gra w statki / Ships Game 

PL

# 1) Stworzenie Wirtualnego Srodowiska `python3 -m venv env` --- Creating a Virtual Environment `python3 -m venv env`
# 2) Uruchomienie Wirtualnego Środowiska `Scripts/activate` `(linux) source Scripts/activate` --- Activating the Virtual Environment `Scripts/activate` `(Linux) source Scripts/activate`
# 3) Zainstalowanie potrzebnych bibliotek `python3 -m pip install -r requirements.txt` --- Installing the necessary libraries `python3 -m pip install -r requirements.txt`
# 4) Uruchomienie glownego pliku aplikacji `python3 game.py` --- Running the main application file `python3 game.py` 

# UWAGA ⚠️
## Należy zwiekszyć rozmiar terminala podczas uruchamiania aplikacji (zaleceny rozmiar FULL-SCREEN)
## It is recommended to increase the size of the terminal when launching the application (recommended size: FULL-SCREEN).

---
Glówne Menu / Main Menu

![image](https://github.com/marcins21/python_classes/assets/62626012/c2690147-eb78-439d-a1bb-c257a41649a1)

---
Gra / Game

![image](https://github.com/marcins21/python_classes/assets/62626012/c89aadae-c473-42ac-961e-dcee4d9ba610)


---
Pozycje Statków są generowane losowo poprzez algorytm / Randomized ship placement 

![image](https://github.com/marcins21/python_classes/assets/62626012/f227dbbf-69c6-4ae5-a31c-9dbaa35b2a2f)


---
Opcja Oszukiwania / Cheat Option 

![image](https://github.com/marcins21/python_classes/assets/62626012/85ffc495-e0b6-4f3a-b29f-f915dfc485f3)



---
# Board.py
## Klasa Board:
### Metoda __init__(self, board_name: str)

>Konstruktor klasy Board inicjujący obiekt planszy gry.
>Ustawia szerokość, wysokość, nazwę planszy i inicjuje planszę oraz listę statków.

### Metoda generate_board(self)
>Generuje planszę gry w formie dwuwymiarowej tablicy wypełnionej symbolami "#".

### Metoda add_ship(self, ship: "ship.Ship")
>Dodaje statek do listy statków przypisanej do planszy.

### Metoda place_ship(self, ship: "ship.Ship")
>Umieszcza statek na planszy, zamieniając symbole na planszy na zielone "X".

### Metoda is_valid_position(self, ship: "ship.Ship")
>Sprawdza, czy umieszczenie statku na planszy jest poprawne, czy nie koliduje z innymi statkami.

### Metoda randomize_ships_across_board(self)
>Losowo rozmieszcza statki na planszy, uwzględniając różne rozmiary statków.

### Metoda randomly_place_ship(self, ship: "ship.Ship")
>Losowo umieszcza statek na planszy, zapewniając poprawność rozmieszczenia.

### Metoda calculate_ship_coordinates(self, start_row, start_col, ship_width, orientation)
>Oblicza współrzędne statku na podstawie punktu startowego, szerokości i orientacji.


### Funkcja show_game_board_with:
>Wyświetla plansze gry dla gracza i bota, umożliwiając opcjonalne ujawnienie planszy bota (cheats).

#### Parametry:
* player_board: Obiekt klasy Board reprezentujący planszę gracza.
* bot_board: Obiekt klasy Board reprezentujący planszę bota.
* bot_title: Nazwa bota do wyświetlenia.
* user_name: Nazwa gracza do wyświetlenia.
* show_with_cheats: Opcjonalny parametr określający, czy ujawnić planszę bota (cheats).

---
# Game.py
### Funkcja game_menu:
>Wyświetla menu opcji dla gracza podczas trwania gry, zawierające możliwość uderzenia w komórkę, losowego rozmieszczenia statków lub wyjścia z gry.

### Funkcja starting_menu_options:
>Wyświetla menu opcji początkowych, umożliwiając graczowi ustawienie nazwy użytkownika, rozpoczęcie nowej gry lub wyjście z aplikacji.

### Funkcja validate_user_hit:
>Waliduje poprawność wprowadzonych współrzędnych przez użytkownika podczas uderzenia w komórkę.
Sprawdza, czy współrzędne są liczbami całkowitymi i czy mieszczą się w zakresie planszy.

### Funkcja game:
> Realizuje główną logikę gry, obsługując ruchy gracza i bota.
Pozwala graczowi na uderzenie w komórkę, losowe rozmieszczenie statków, aktywację cheatów lub wyjście z gry.
Wyświetla informacje o aktualnym stanie gry oraz plansze gracza i bota.

### Funkcja starting_menu:
>Implementuje interaktywne menu początkowe, umożliwiając graczowi ustawienie nazwy użytkownika, rozpoczęcie nowej gry lub wyjście z aplikacji.
Tworzy plansze gracza i bota oraz rozpoczyna grę.


# Ship.py
### Klasa Ship:
> Klasa reprezentująca ogólny statek w grze.
Inicjalizuje obiekt statku przyjmując szerokość i współrzędne jako argumenty.
Posiada metody do sprawdzania, czy statek został trafiony (is_hit) oraz czy został zniszczony (is_destroyed).

### Klasa SmallShip:
> Klasa dziedzicząca po klasie Ship.
Reprezentuje statek o małej szerokości, korzystając z ustalonego rozmiaru statku małego z ustawień.

### Klasa MediumShip:
>Klasa dziedzicząca po klasie Ship.
Reprezentuje statek o średniej szerokości, korzystając z ustalonego rozmiaru statku średniego z ustawień.

### Klasa LargeShip:
>Klasa dziedzicząca po klasie Ship.
Reprezentuje statek o dużej szerokości, korzystając z ustalonego rozmiaru statku dużego z ustawień.