"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin käyttäen funkitoita.
Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19,95 €
Kokonaishinta: 39,90 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""
from datetime import datetime

def hae_varaaja(varaus: list[str]) -> None:
    nimi = varaus[1]
    print(f"Varaaja: {nimi}")

def hae_tuntimaara(varaus: list[str]) -> int:
    tunnit = int(varaus[4])
    print(f"Tuntimäärä: {tunnit}")
    return tunnit

def hae_varausnumero(varaus):
    Varausnumero = varaus[0]
    print(f"Varausnumero: {Varausnumero}")
    return Varausnumero

def hae_paiva(varaus):
    paiva_str = varaus[2]  # esim. "2025-10-31"
    paiva_date = datetime.strptime(paiva_str, "%Y-%m-%d")  # muuntaa datetimeksi
    uusi_paiva = paiva_date.strftime("%d.%m.%Y")  # muotoon "31.10.2025"
    print(f"Päivämäärä: {uusi_paiva}")

def hae_aloitusaika(varaus):
    Aloitusaika = varaus[3]
    muotoiltu = Aloitusaika.replace(":", ".")
    print(f"Aloitusaika: {muotoiltu}")

def hae_tuntihinta(varaus):
    hinta = float(varaus[5])
    print(f"Tuntihinta: {hinta}")

def hae_kohde(varaus):
    kohde =  varaus[7]
    print(f"Varauskohde: {kohde}")

def hae_puhelin(varaus):
    puhku = varaus[8]
    print(f"Puhelinnumero: {puhku}")

def hae_sahkoposti(varaus):
    sposti = varaus[9]
    print(f"Sähköposti: {sposti}")

def hae_maksettu(varaus: list[str]) -> float:
    maksu = varaus[6]
    if maksu == "True": 
        print(f"Maksettu: Kyllä.")
    else: 
        print(f"Maksettu: Ei.")

def laske_kokonaishinta(varaus: list[str]) -> float:
    tunnit = int(varaus[4])
    hinta = float(varaus[5])
    kokonaishinta = tunnit * hinta
    text = "{:.2f}".format(kokonaishinta)
    text = text.replace(".", ",")
    print(f"Kokonaishinta: {text}€")
    return kokonaishinta

def tulosta_varaus(varaus):
    hae_varausnumero(varaus)
    hae_varaaja(varaus)
    hae_paiva(varaus)
    hae_aloitusaika(varaus)
    hae_tuntimaara(varaus)
    hae_tuntihinta(varaus)
    laske_kokonaishinta(varaus)
    hae_maksettu(varaus)
    hae_kohde(varaus)
    hae_puhelin(varaus)
    hae_sahkoposti(varaus)

    

def main():
    # Maaritellaan tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"

    # Avataan tiedosto, luetaan ja splitataan sisalto
    with open(varaukset, "r", encoding="utf-8") as f:
        for rivi in f:
            rivi = rivi.strip()
            varaus = rivi.split('|')
            print()
            print("-" * 30)
            tulosta_varaus(varaus)

if __name__ == "__main__":
    main()