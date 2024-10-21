def beolvas_fajlbol(fajlnev): 
    try:
        with open(fajlnev, 'r') as f:  # fajl sorainak beolvasasa
            adatok = f.read().splitlines()  
        return adatok
    except:
        print("Hiba: A fájl nem található.")  # hiba, ha nincs fajl
        return None

def eldonto(adatok):
    if all(x.isdigit() for x in adatok):  # ha minden szam, atalakitas
        return [int(x) for x in adatok] 
    elif all(isinstance(x, str) for x in adatok):  # ha minden szoveg, szovegkent marad
        return adatok  
    else:
        print("Hiba: Vegyes típusú adatok!")  # hibauzenet vegyes adat esetén
        return None

def csere_rendezes(lista, novekvo=True):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):  # osszehasonlitas es csere, ha szukseges
            if (novekvo and lista[i] > lista[j]) or (not novekvo and lista[i] < lista[j]):
                lista[i], lista[j] = lista[j], lista[i]  
    return lista

def beszurasos_rendezes(lista, novekvo=True):
    for i in range(1, len(lista)):
        kulcs = lista[i]
        j = i - 1
        while j >= 0 and ((novekvo and lista[j] > kulcs) or (not novekvo and lista[j] < kulcs)):  # elore tologatas
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = kulcs  # beszuras a megfelelo helyre
    return lista

def beszuras(lista, uj_elem, novekvo=True):
    lista.append(uj_elem)  # uj elem hozzaadasa
    return beszurasos_rendezes(lista, novekvo)  # ujrarendezve

def main():
    fajlnev = "ki.txt"
    adatok = beolvas_fajlbol(fajlnev)  # fajlbol adatok beolvasasa
    
    if adatok is None:  # ha nincs adat, kilepes
        return  

    adatok = eldonto(adatok)  # adatok tipusanak ellenorzese

    if adatok is None:  # ha hiba van, kilepes
        return  

    print("Válassz rendezési sorrendet:")
    print("1. Növekvő")
    print("2. Csökkenő")
    
    sorrend_valasztas = input("Sorrend választás (1 vagy 2): ")
    novekvo = True if sorrend_valasztas == "1" else False

    print("Válassz rendezési algoritmust:")
    print("1. Csere rendezés")
    print("2. Beszúrásos rendezés")

    algoritmus_valasztas = input("Algoritmus választás (1 vagy 2): ")

    if algoritmus_valasztas == "1":
        rendezett_adatok = csere_rendezes(adatok, novekvo)  # csere rendezest hasznal
    else:
        rendezett_adatok = beszurasos_rendezes(adatok, novekvo)  # beszurasos rendezest hasznal

    print("Rendezett lista:", rendezett_adatok)

    uj_elem = input("Adj meg egy új elemet: ")
    if uj_elem.isdigit():  # szamok kezelese
        uj_elem = int(uj_elem)

    uj_lista = beszuras(rendezett_adatok, uj_elem, novekvo)
    print("Új lista:", uj_lista)

main()
