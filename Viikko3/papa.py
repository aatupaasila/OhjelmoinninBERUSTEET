from datetime import datetime

def muunna_varaustiedot(varaus: list) -> list:
    muunnettu = []
    muunnettu.append(int(varaus[0]))  
    muunnettu.append(str(varaus[1]))
    muunnettu.append(str(varaus[2]))
    muunnettu.append(str(varaus[3]))
    muunnettu.append(datetime.strptime(varaus[4], "%Y-%m-%d").date())
    muunnettu.append(datetime.strptime(varaus[5], "%H:%M").time())
    muunnettu.append(int(varaus[6]))
    muunnettu.append(float(varaus[7]))
    muunnettu.append(varaus[8] == "True")
    muunnettu.append(str(varaus[9]))
    muunnettu.append(datetime.strptime(varaus[10], "%Y-%m-%d %H:%M:%S"))
    return muunnettu

def hae_varaukset(tiedostonimi: str) -> list:
    varauslista = []
    varauslista.append([
        "varausId", "nimi", "sähköposti", "puhelin",
        "varauksenPvm", "varauksenKlo", "varauksenKesto",
        "hinta", "varausVahvistettu", "varattuTila", "varausLuotu"
    ])

    with open(tiedostonimi, "r", encoding="utf-8") as f:
        for rivi in f:
            rivi = rivi.strip()
            kentat = rivi.split('|')
            varauslista.append(muunna_varaustiedot(kentat))
    return varauslista

def main():
    varausdata = hae_varaukset("varaukset.txt")

    print("1) Vahvistetut varaukset")
    for merkinta in varausdata[1:]:
        if merkinta[8] == True:
            print(f'- {merkinta[1]}, {merkinta[9]}, {merkinta[4].strftime("%d.%m.%Y")}, klo {merkinta[5].strftime("%H.%M")}')
    print()

    print("2) Pitkät varaukset (> 3 h)")
    for merkinta in varausdata[1:]:
        if merkinta[6] >= 3:
            print(
                f'- {merkinta[1]}, {merkinta[4].strftime("%d.%m.%Y")} klo {merkinta[5].strftime("%H.%M")}'
                f' kesto {merkinta[6]} h, {merkinta[9]}'
            )
    print()

    print("3) Varausten vahvistusstatus")
    for merkinta in varausdata[1:]:
        if merkinta[8]:
            print(f'{merkinta[1]} -> Vahvistettu')
        else:
            print(f'{merkinta[1]} -> Ei vahvistettu')
    print()

    print("4) Yhteenveto Vahvistuksista")
    tunnistetut = 0
    tunnistamattomat = 0

    for merkinta in varausdata[1:]:
        if merkinta[8]:
            tunnistetut += 1
        else:
            tunnistamattomat += 1

    print(f'- Vahvistettuja varauksia: {tunnistetut} kpl')
    print(f'- Ei-vahvistettuja varauksia: {tunnistamattomat} kpl')
    print()

    print("5) Vahvistettujen varausten kokonaistulot")
    summa_rahana = 0

    for merkinta in varausdata[1:]:
        if merkinta[8]:
            yksikkohinta = merkinta[7]
            tunnit = merkinta[6]
            summa_rahana += yksikkohinta * tunnit

    print(f'Vahvistettujen varausten kokonaistulot: {summa_rahana} €')

if __name__ == "__main__":
    main()
