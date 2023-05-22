class fanta_automata:
    Narancs = 5
    Citrom = 5
    Zero = 5
    Bodza = 5
    Afonya = 5


fanntak = fanta_automata()
print(fanntak.Narancs)

penz = 5000
print(penz)
while penz > 300:
    bekeres = int(input("Valassz Fantat: "))
    if bekeres == 1:
        if fanntak.Narancs > 0:
            fanntak.Narancs = fanntak.Narancs - 1
            penz = penz - 550
            print(fanntak.Narancs)
            print(f"{penz}ft-od maradt")
        elif fanntak.Narancs == 0:
            print(f"{penz}ft-od maradt")
            print("kifogyott")

    elif bekeres == 2:
        if fanntak.Citrom > 0:
            fanntak.Citrom = fanntak.Citrom - 1
            penz = penz - 300
            print(fanntak.Citrom)
            print(f"{penz}ft-od maradt")
        elif fanntak.Citrom == 0:
            print(f"{penz}ft-od maradt")
            print("Kifogyott")

    elif bekeres == 3:
        if fanntak.Zero > 0:
            fanntak.Zero = fanntak.Zero - 1
            penz = penz - 470
            print(fanntak.Zero)
            print(f"{penz}ft-od maradt")
        elif fanntak.Zero == 0:
            print(f"{penz}ft-od maradt")
            print("Kifogyott")

    elif bekeres == 4:
        if fanntak.Bodza > 0:
            fanntak.Bodza = fanntak.Bodza - 1
            penz = penz - 400
            print(fanntak.Bodza)
            print(f"{penz}ft-od maradt")
        elif fanntak.Bodza == 0:
            print(f"{penz}ft-od maradt")
            print("Kifogyott")

    elif bekeres == 5:
        if fanntak.Afonya > 0:
            fanntak.Afonya = fanntak.Afonya - 1
            penz = penz - 500
            print(fanntak.Afonya)
            print(f"{penz}ft-od maradt")
        elif fanntak.Afonya == 0:
            print(f"{penz}ft-od maradt")
            print("Kifogyott")
else:
    print("\n Kifogytál te csoró")
    print(penz)