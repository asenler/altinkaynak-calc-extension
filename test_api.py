from altinkaynak.api import get_rates

rates = get_rates()

for kod, bilgi in rates.items():
    print(
        kod,
        bilgi["Alis"],
        bilgi["Satis"]
    )
