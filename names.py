print("Mam na imię Krzysztof")  # tutaj wpisz swoje imię
# i dodaj jeszcze jakiś ciekawy kod

# Gra w zlokalizowanie i zatopienie lotniskowca

import random

print()
print("Spróbuj zatopić lotniskowiec")
print("Pozycja lotniskowca znajduje się na mapie o rozmiarze 10x10 licząć w prawo i od dołu.")
print("Masz 10 prób. Wyślij eskadrę i powodzenia!\n")

# Losowanie współrzędnych lotniskowca
position_x = random.randint(1, 10)
position_y = random.randint(1, 10)
maks_raid = 10

# Pętla do odgadywania położenia lotnislowca
for raid in range(1, maks_raid + 1):
    print(f"Próba {raid}/{maks_raid}")
    try:
        raid_x = int(input("Podaj współrzędną X (1-10): "))
        raid_y = int(input("Podaj współrzędną Y (1-10): "))
    except ValueError:
        print("Podaj prawidłową liczbę z zakresu 1-10.")
        continue

    if raid_x < 1 or raid_x > 10 or raid_y < 1 or raid_y > 10:
        print("Współrzędne muszą być z zakresu 1-10.")
        continue

    if raid_x == position_x and raid_y == position_y:
        print(f"Zwycięstwo! Zatopiłeś lotniskowiec na współrzędnych ({position_x}, {position_y}) za {raid} razem.")
        break
    else:
        # Podpowiedzi
        if raid_x < position_x:
            print("Lotniskowiec jest bardziej na prawo.")
        elif raid_x > position_x:
            print("Lotniskowiec jest bardziej na lewo.")

        if raid_y < position_y:
            print("Lotniskowiec jest bardziej do góry.")
        elif raid_y > position_y:
            print("Lotniskowiec jest bardziej na dół.")
else:
    print(f"Niestety, nie udało się zatopić lotniskowca. Jego pozycja to ({position_x}, {position_y}). Może następna ekspedycja się powiedzie")