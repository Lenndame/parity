"""
Pruefbit (schwer)

# Das letzte Bit wird in der 8-Bit Übertragung als Paritätsbit (Prüfbit) verwendet.

# wenn die Summe der ersten 7 bit gerade (even) ist, muss prüfbit 1 sein
# wenn die Summe der ersten 7 bit ungerade (odd) ist, muss prüfbit 0 sein
# Wenn das nicht zutreffen sollte, hat sich bei der Datenübertragung ein
# Fehler eingeschlichen

m = [
    [0, 1, 1, 0, 1, 1, 0, 1], # richtig (Paritätsbit 1)
    [0, 0, 0, 0, 0, 1, 0, 0], # richtig (Paritätsbit 0)
    [0, 0, 0, 0, 1, 1, 0, 0], # falsch (Paritätsbit 0)
    [0, 0, 0, 1, 1, 1, 0, 1], # falsch (Paritätsbit 1)
]

error_zeilen = [
    2, 3
]

Hinweis: in echt ist die Prüfung aufwändiger und wird mit Hamming-Code
gelöst. Das vorliegende Beispiel ist nur eine start simplifizierte Form.

https://de.wikipedia.org/wiki/Hamming-Code
https://de.wikipedia.org/wiki/Parit%C3%A4tsbit
"""
m = [
    [1, 1, 0, 1, 1, 0, 0, 1],  # 5
    [0, 0, 0, 0, 1, 0, 0, 0],  # 1
    [0, 0, 0, 1, 0, 1, 0, 0],  # 2
    [0, 0, 1, 1, 1, 0, 0, 1],  # 4
]

for bit in m:
    count = 0
    for element in bit:
        count += element
    if (count % 2 == 0):
        print("wahr")
    else:
        print("falsch")
