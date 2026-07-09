# -*- coding: utf-8 -*-

import requests

URL = "https://static.altinkaynak.com/public/Currency"


def get_rates(timeout=10):
    """
    Altınkaynak JSON verisini indirir.

    Dönen değer:
        {
            "USD": {...},
            "EUR": {...}
        }
    """

    response = requests.get(URL, timeout=timeout)
    response.raise_for_status()

    data = response.json()

    rates = {}

    for item in data:
        code = item.get("Kod")
        if code:
            rates[code] = item

    return rates
