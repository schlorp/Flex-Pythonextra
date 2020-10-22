import os

bestand = input("welk bestand wil je verwijderen? ")

if len(bestand) > 0:
    if os.path.exists(bestand):
        os.remove(bestand)
        print("het bestand " + bestand + " is verwijdered. jammer dan.")
    else:
        print("dit bestand bestaat niet, sorry.")
else:
    print("geen invoer, script zal stoppen")
