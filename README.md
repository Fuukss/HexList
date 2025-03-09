# HexList

## Zadanie 1 – Funkcja zwracającą reprezentację heksadecymalną wartości liczbowych 

## Opis zadania

Celem zadania było stworzenie klasy `HexList`, która dziedziczy po wbudowanej klasie `list` i zwraca heksadecymalną reprezentację liczb przekazanych podczas inicjalizacji. Dzięki temu, przy odczycie elementu listy, zamiast liczby dziesiętnej, zwracana jest jej reprezentacja w systemie szesnastkowym.

Przykład użycia:

```python
my_list = HexList([1, 15, 16, 25])
print(my_list[0])  # 0x1
print(my_list[1])  # 0xf
print(my_list[2])  # 0x10
print(my_list[3])  # 0x19
