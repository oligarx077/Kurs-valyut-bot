import requests


def date():
    get_date = requests.get('https://cbu.uz/ru/arkhiv-kursov-valyut/json/').json()
    date_info = [i.get('Date') for i in get_date]
    return date_info


# Берём значение Эвро
def eur():
    get_eur = requests.get('https://cbu.uz/ru/arkhiv-kursov-valyut/json/eur/').json()
    eur_info = [[i.get('Ccy'), i.get('Rate')] for i in get_eur]
    return eur_info


def usd():
    # Берём значение Эвро
    get_usd = requests.get('https://cbu.uz/ru/arkhiv-kursov-valyut/json/usd/').json()
    usd_info = [[i.get('Ccy'), i.get('Rate')] for i in get_usd]
    return usd_info


def rub():
    # Берём значение Эвро
    get_rub = requests.get('https://cbu.uz/ru/arkhiv-kursov-valyut/json/rub/').json()
    rub_info = [[i.get('Ccy'), i.get('Rate')] for i in get_rub]
    return rub_info
