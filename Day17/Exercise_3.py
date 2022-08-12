#Print the following dictionary using the format method and ** unpacking.

country = {
    "name": "Germany",
    "population": "83 million",
    "capital": "Berlin",
    "currency": "Euro"
}

country_template = """Name= {name}
Population= {population}
Capital= {capital}
Currency= {currency}"""

print(country_template.format(**country))


