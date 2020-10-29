from PIL import Image

afbeelding = Image.open("aragorn.PNG")

afbeelding.show()

breedte = afbeelding.width
hoogte = afbeelding.height

print("de afbeelding is " + str(breedte) + " pixels breed en " + str(hoogte) + " pixels hoog")

print(afbeelding.format, afbeelding.size, afbeelding.mode)
