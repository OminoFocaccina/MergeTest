# indovina_il_numero.py
import random

def gioca():
    print("🎯 Indovina il numero tra 1 e 100!")
    difficolta = {"facile": 10, "medio": 7, "difficile": 5}
    scelta = input("Scegli difficoltà (facile/medio/difficile) [medio]: ").strip().lower() or "medio"
    tentativi = difficolta.get(scelta, 7)

    segreto = random.randint(1, 100)
    usati = 0

    while usati < tentativi:
        try:
            guess = int(input(f"Tentativo {usati+1}/{tentativi}: "))
            if not 1 <= guess <= 100:
                print("Inserisci un numero tra 1 e 100.")
                continue
        except ValueError:
            print("Devi inserire un numero intero!")
            print("Se sbagli ancora ti devasto il pc di virus")
            continue

        usati += 1
        if guess == segreto:
            print(f"Bravo! Hai indovinato in {usati} tentativi.")
            break
        elif guess < segreto:
            print("Troppo basso.", end=" ")
        else:
            print("Troppo alto.", end=" ")

        diff = abs(segreto - guess)
        if diff <= 5:
            print("Caldissimo!")
        elif diff <= 10:
            print("Caldo!")
        elif diff <= 20:
            print("Tiepido.")
        else:
            print("Freddo.")
    else:
        print(f"Finito! Il numero era {segreto}.")

if __name__ == "__main__":
    while True:
        gioca()
        if input("Vuoi rigiocare? (s/n): ").strip().lower() != "s":
            print("Alla prossima!")
            break

