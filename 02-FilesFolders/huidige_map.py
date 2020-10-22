import os

mapnaam = ""

lengte_mapnaam = 0

while lengte_mapnaam == 0:

    mapnaam = input("welke naam wil je voor de map? ")
    lengte_mapnaam = len(mapnaam)

    if lengte_mapnaam > 0:
        os.mkdir(mapnaam)
    else:
        print("je hebt geen naam ingevoerd")

print("de map " + mapnaam + " is gemaakt.")
