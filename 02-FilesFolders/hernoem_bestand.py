import os

bestandsnaam = "demobestand.txt"

huidige_map = os.getcwd()

volledige_pad = os.path.join(huidige_map, bestandsnaam)
print("dit bestand gaan we hernoemen: " + volledige_pad)

nieuwe_naam = input("nieuwe bestandsnaam: ")

if len(nieuwe_naam) > 0:
    
    nieuwe_volledige_pad = os.path.join(huidige_map, nieuwe_naam)
    print("bestand wordt hernoemd naar: " + nieuwe_volledige_pad)
    
    os.rename(volledige_pad, nieuwe_volledige_pad)
    print("bestand hernoemd")
    
else:
    print("sorry, geen geldige invoer, einde programa")
