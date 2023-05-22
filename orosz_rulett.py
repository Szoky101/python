import random
random_szam = random.randint(0, 10)

random_halal = random.randint(0, 10)
print(random_halal, "Ez a tipp halálos NE üsd be")

print("Ez egy Orosz rulett")
tipp = int(input("Irj be egy számot hátha nem halsz meg \n"))

if tipp == random_szam:
    print("Meghaltál xd")
else:
    print("Lucky you are still alive")
