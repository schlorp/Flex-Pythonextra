import io

bestand = open("test.txt", "w")

bestand.write("test 123!");

bestand.close()

bestand2 = open("test.txt", "r")

bestand2.write("lekker alles overschriven")

