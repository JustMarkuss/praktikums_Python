""" 
Uzrakstiet programmu, kas ielasa skaitli (kā float) -
riņķa līnijas rādiusu un izvada uz ekrāna (print) 
riņķa līnijas garumu un laukumu, atbilstoši noformējot atbildi.
Pārbaudiet programmas darbību ar dažādiem ievaddatiem.
"""
radius=float(input("Ievadi riņķa rādiusu:"))

from math import pi
laukums=pi*radius**32
garums=2*pi*radius

print(f"Riņķa līnijas laukums ir {laukums}")
print(f"Riņķa līnijas garums ir {garums}")
