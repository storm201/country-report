import requests

COUNTRIES_API = (
    "https://restcountries.com/v3.1/all"
    "?fields=name,capital,region,population,currencies,languages,cca3"
)

INDICATORS = {
    "GDP": "NY.GDP.MKTP.CD",
    "GDP_PER_CAPITA": "NY.GDP.PCAP.CD",
    "LIFE_EXPECTANCY": "SP.DYN.LE00.IN",
    "INTERNET_USERS": "IT.NET.USER.ZS"
}


def fetch_countries():
    try:
        response = requests.get(COUNTRIES_API, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error fetching countries:", e)
        return []


def search_country(countries, search_term):
    search_term = search_term.lower()

    for country in countries:
        name = country.get("name", {}).get("common", "")

        if name.lower() == search_term:
            return country

    return None


def fetch_indicator(country_code, indicator):
    try:
        url = (
            f"https://api.worldbank.org/v2/country/"
            f"{country_code}/indicator/{indicator}"
            f"?format=json"
        )

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if len(data) < 2:
            return None

        for entry in data[1]:
            if entry["value"] is not None:
                return entry["value"]

        return None

    except Exception:
        return None


def format_currency(value):
    if value is None:
        return "Not Available"

    if value >= 1_000_000_000_000:
        return f"${value/1_000_000_000_000:.2f} Trillion"

    if value >= 1_000_000_000:
        return f"${value/1_000_000_000:.2f} Billion"

    if value >= 1_000_000:
        return f"${value/1_000_000:.2f} Million"

    return f"${value:,.2f}"


def display_report(country):
    name = country.get("name", {}).get("common", "N/A")

    capital = country.get("capital", ["N/A"])[0]

    region = country.get("region", "N/A")

    population = country.get("population", 0)

    cca3 = country.get("cca3", "")

    currencies = country.get("currencies", {})
    currency_names = []

    for cur in currencies.values():
        currency_names.append(cur.get("name", ""))

    languages = list(country.get("languages", {}).values())

    print("\nFetching World Bank data...\n")

    gdp = fetch_indicator(
        cca3,
        INDICATORS["GDP"]
    )

    gdp_per_capita = fetch_indicator(
        cca3,
        INDICATORS["GDP_PER_CAPITA"]
    )

    life_expectancy = fetch_indicator(
        cca3,
        INDICATORS["LIFE_EXPECTANCY"]
    )

    internet_users = fetch_indicator(
        cca3,
        INDICATORS["INTERNET_USERS"]
    )

    print("=" * 60)
    print("           COUNTRY INTELLIGENCE REPORT")
    print("=" * 60)

    print(f"\nCountry           : {name}")
    print(f"Capital           : {capital}")
    print(f"Region            : {region}")
    print(f"Population        : {population:,}")

    print("\n---------------- ECONOMY ----------------")

    print(f"GDP               : {format_currency(gdp)}")

    if gdp_per_capita:
        print(f"GDP Per Capita    : ${gdp_per_capita:,.2f}")
    else:
        print("GDP Per Capita    : Not Available")

    print("\n------------- DEVELOPMENT --------------")

    if life_expectancy:
        print(f"Life Expectancy   : {life_expectancy:.1f} years")
    else:
        print("Life Expectancy   : Not Available")

    if internet_users:
        print(f"Internet Users    : {internet_users:.1f}%")
    else:
        print("Internet Users    : Not Available")

    print("\n------------- ADDITIONAL INFO ----------")

    print(
        f"Currency          : "
        f"{', '.join(currency_names) if currency_names else 'N/A'}"
    )

    print(
        f"Languages         : "
        f"{', '.join(languages) if languages else 'N/A'}"
    )

    print("\n" + "=" * 60)


def main():
    print("=" * 60)
    print("      COUNTRY INTELLIGENCE SEARCH TOOL")
    print("=" * 60)

    countries = fetch_countries()

    if not countries:
        return

    while True:
        search = input(
            "\nEnter country name "
            "(or type 'exit' to quit): "
        ).strip()

        if search.lower() == "exit":
            print("\nGoodbye!")
            break

        country = search_country(
            countries,
            search
        )

        if country:
            display_report(country)
        else:
            print("\nCountry not found.")


if __name__ == "__main__":
    main()