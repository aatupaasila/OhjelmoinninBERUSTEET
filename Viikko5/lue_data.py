# Copyright (c) 2025 Aatu Paasila
# License: MIT

from datetime import datetime, date
from typing import List, Tuple, Dict

Mittaus = Tuple[datetime, float, float, float, float, float, float]
PaivaYhteenveto = Tuple[float, float, float, float, float, float]


def lue_data(viikko42: str) -> List[Mittaus]:
    """Lukee viikko42.csv tiedoston ja palauttaa sen listana mittauksista."""
    mittaukset: List[Mittaus] = []

    with open(viikko42, "r", encoding="utf-8") as f:
        for i, rivi in enumerate(f):
            rivi = rivi.strip()

            if i == 0:
                continue
                
            osat = rivi.split(";")

            aika = datetime.fromisoformat(osat[0])

            kul_v1 = float(osat[1])
            kul_v2 = float(osat[2])
            kul_v3 = float(osat[3])
                
            tuo_v1 = float(osat[4])
            tuo_v2 = float(osat[5])
            tuo_v3 = float(osat[6])

            mittaus: Mittaus = (aika, kul_v1, kul_v2, kul_v3, tuo_v1, tuo_v2, tuo_v3)
            mittaukset.append(mittaus)

    return mittaukset


def laske_paivittaiset_yhteenvedot(mittaukset: List[Mittaus]) -> Dict[date, PaivaYhteenveto]:
    """Laskee joka päivälle kulutuksen ja tuotannon summat"""
    paiva_summat: Dict[date, list[float]] = {}

    for mittaus in mittaukset:
        aika, kul1, kul2, kul3, tuo1, tuo2, tuo3 = mittaus
        paiva = aika.date()

        if paiva not in paiva_summat:
            paiva_summat[paiva] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        
        summat = paiva_summat[paiva]
        summat[0] += kul1
        summat[1] += kul2
        summat[2] += kul3
        summat[3] += tuo1
        summat[4] += tuo2
        summat[5] += tuo3

    tulos: Dict[date, PaivaYhteenveto] = {}
    for paiva, summat in paiva_summat.items():
        tulos[paiva] = (
            summat[0],
            summat[1],
            summat[2],
            summat[3],
            summat[4],
            summat[5],
        )

    return tulos        


def viikonpaiva_suomeksi(pvm: date) -> str:
    """Palauttaa viikonpäivän nimen suomeksi."""
    nimet = [
        "maanantai",
        "tiistai",
        "keskiviikko",
        "torstai",
        "perjantai",
        "lauantai",
        "sunnuntai",
    ]
    return nimet[pvm.weekday()]


def muotoile_kwh(wh: float) -> str:
    """Muuntaa Wh -> kWh, 2 desimaalia ja pilkku desimaalierottimena."""
    kwh = wh / 1000
    teksti = f"{kwh:.2f}"
    return teksti.replace(".", ",")


def tulosta_taulukko(paiva_yhteenvedot: Dict[date, PaivaYhteenveto]) -> None:
    """Tulostaa viikon 42 taulukon konsoliin."""

    print("Viikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n")
    print(
        f"{'Päivä':<12}{'Pvm':<12}  {'Kulutus [kWh]':<27}  {'Tuotanto [kWh]'}"
    )
    print(
        f"{'':<12}{'(pv.kk.vvvv)':<12}  {'v1':>7}{'v2':>7}{'v3':>7}    {'v1':>7}{'v2':>7}{'v3':>7}"
    )
    print("-" * 78)

    for pvm in sorted(paiva_yhteenvedot.keys()):
        kul1, kul2, kul3, tuo1, tuo2, tuo3 = paiva_yhteenvedot[pvm]

        paiva_nimi = viikonpaiva_suomeksi(pvm)
        pvm_str = f"{pvm.day}.{pvm.month}.{pvm.year}"

        k1 = muotoile_kwh(kul1)
        k2 = muotoile_kwh(kul2)
        k3 = muotoile_kwh(kul3)
        t1 = muotoile_kwh(tuo1)
        t2 = muotoile_kwh(tuo2)
        t3 = muotoile_kwh(tuo3)

        print(
            f"{paiva_nimi:<12}{pvm_str:<12}  "
            f"{k1:>7}{k2:>7}{k3:>7}    {t1:>7}{t2:>7}{t3:>7}"
        )



def main() -> None:
    """Ohjelman pääfunktio: lukee datan, laskee yhteenvedot ja tulostaa raportin."""
    mittaukset = lue_data("viikko42.csv")
    paiva_yhteenvedot = laske_paivittaiset_yhteenvedot(mittaukset)
    tulosta_taulukko(paiva_yhteenvedot)


if __name__ == "__main__":
    main()


    
