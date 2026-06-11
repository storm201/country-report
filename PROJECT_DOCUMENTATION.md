# Country Intelligence Search Tool - Project Documentation

## Project Overview

**Repository:** [storm201/Country-Report](https://github.com/storm201/Country-Report)  
**Language:** Python  
**Repository ID:** 1260206395  
**Created:** June 5, 2026  
**Last Updated:** June 11, 2026  

---

## Project Description

A Python-based Country Intelligence Search Tool that fetches comprehensive country information using public APIs. The tool allows users to search for any country and retrieve detailed reports including economic indicators, development metrics, and geographical information.

### Key Features:
- 🔍 Country name search functionality
- 💰 GDP and GDP Per Capita data
- 📊 Life Expectancy metrics
- 🌐 Internet Usage statistics
- 👥 Population information
- 🏛️ Capital city details
- 🗺️ Regional classification

---

## Technology Stack

| Technology | Purpose |
|-----------|---------|
| **Python** | Core programming language |
| **Requests Library** | HTTP requests for API calls |
| **REST Countries API** | Country basic information (name, capital, region, population, currencies, languages) |
| **World Bank API** | Economic and development indicators |

**Dependencies:**
```
requests
```

---

## Repository Structure

```
Country-Report/
├── README.md                 # Project overview
├── requirements.txt          # Python dependencies
├── country_report.py         # Main application file
├── OP1.png                   # Screenshot 1
├── OP2.png                   # Screenshot 2
└── OP3.png                   # Screenshot 3
```

---

## Screenshots & Output Examples

### Screenshot 1 - Initial Application Launch
![OP1](https://github.com/storm201/Country-Report/blob/main/OP1.png)
**Description:** Shows the application startup screen with the Country Intelligence Search Tool header and welcome message.

### Screenshot 2 - Successful Country Search
![OP2](https://github.com/storm201/Country-Report/blob/main/OP2.png)
**Description:** Displays a complete country report with all economic, development, and geographical information.

### Screenshot 3 - Additional Search Example
![OP3](https://github.com/storm201/Country-Report/blob/main/OP3.png)
**Description:** Shows the tool's ability to retrieve data for different countries with varying data availability.

---

## Code Architecture

### Main Components

#### 1. **API Constants**
```python
COUNTRIES_API = "https://restcountries.com/v3.1/all?fields=name,capital,region,population,currencies,languages,cca3"

INDICATORS = {
    "GDP": "NY.GDP.MKTP.CD",
    "GDP_PER_CAPITA": "NY.GDP.PCAP.CD",
    "LIFE_EXPECTANCY": "SP.DYN.LE00.IN",
    "INTERNET_USERS": "IT.NET.USER.ZS"
}
```

#### 2. **Core Functions**

**fetch_countries()** - [Line 16-23](https://github.com/storm201/Country-Report/blob/main/country_report.py#L16-L23)
- Fetches all countries from REST Countries API
- Handles network errors with exception handling
- Returns JSON array of country data

**search_country()** - [Line 26-35](https://github.com/storm201/Country-Report/blob/main/country_report.py#L26-L35)
- Performs case-insensitive country name search
- Compares against common country names
- Returns matched country object or None

**fetch_indicator()** - [Line 38-61](https://github.com/storm201/Country-Report/blob/main/country_report.py#L38-L61)
- Retrieves World Bank indicators for specific country
- Parameters: country code (cca3), indicator ID
- Returns most recent non-null indicator value
- Graceful error handling for unavailable data

**format_currency()** - [Line 64-77](https://github.com/storm201/Country-Report/blob/main/country_report.py#L64-L77)
- Converts large numbers to human-readable currency format
- Supports Trillion, Billion, Million, and standard dollar formatting
- Handles None values with "Not Available" message

**display_report()** - [Line 80-163](https://github.com/storm201/Country-Report/blob/main/country_report.py#L80-L163)
- Constructs complete country intelligence report
- Fetches all required World Bank indicators
- Displays formatted output with sections:
  - Basic Country Info (Name, Capital, Region, Population)
  - Economy (GDP, GDP Per Capita)
  - Development (Life Expectancy, Internet Users)
  - Additional Info (Currency, Languages)

**main()** - [Line 166-194](https://github.com/storm201/Country-Report/blob/main/country_report.py#L166-L194)
- Application entry point
- Interactive loop for country searches
- Exit functionality via 'exit' command

---

## How to Use

### Installation
```bash
# Clone the repository
git clone https://github.com/storm201/Country-Report.git
cd Country-Report

# Install dependencies
pip install -r requirements.txt
```

### Running the Application
```bash
python country_report.py
```

### Example Usage
```
======================================================
      COUNTRY INTELLIGENCE SEARCH TOOL
======================================================

Enter country name (or type 'exit' to quit): United States

Fetching World Bank data...

============================================================
           COUNTRY INTELLIGENCE REPORT
============================================================

Country           : United States
Capital           : Washington, D.C.
Region            : Americas
Population        : 331,002,651

---------------- ECONOMY ----------------

GDP               : $21.06 Trillion
GDP Per Capita    : $63,543.58

------------- DEVELOPMENT --------------

Life Expectancy   : 78.9 years
Internet Users    : 90.0%

------------- ADDITIONAL INFO ----------

Currency          : United States dollar
Languages         : English

============================================================
```

---

## API Endpoints Used

### 1. REST Countries API
- **URL:** `https://restcountries.com/v3.1/all`
- **Method:** GET
- **Fields Requested:** name, capital, region, population, currencies, languages, cca3
- **Response:** JSON array of all countries with specified fields
- **Documentation:** [REST Countries API](https://restcountries.com)

### 2. World Bank API
- **Base URL:** `https://api.worldbank.org/v2/country/`
- **Endpoint Structure:** `/{country_code}/indicator/{indicator_id}?format=json`
- **Parameters:**
  - `country_code`: ISO 3-letter country code (cca3)
  - `indicator_id`: World Bank indicator code
- **Documentation:** [World Bank Data API](https://data.worldbank.org/developers/api-overview)

---

## Data Fields & Indicators

### Country Information (REST Countries API)
| Field | Description | Example |
|-------|-------------|---------|
| name.common | Country common name | "United States" |
| capital | Capital city | ["Washington, D.C."] |
| region | Geographical region | "Americas" |
| population | Total population | 331002651 |
| cca3 | ISO 3-letter code | "USA" |
| currencies | Currency information | {"USD": {"name": "United States dollar"}} |
| languages | Languages spoken | {"eng": "English"} |

### World Bank Indicators
| Indicator | Code | Measurement |
|-----------|------|-------------|
| GDP | NY.GDP.MKTP.CD | Current US$ |
| GDP Per Capita | NY.GDP.PCAP.CD | Current US$ |
| Life Expectancy | SP.DYN.LE00.IN | Years |
| Internet Users | IT.NET.USER.ZS | % of population |

---

## Error Handling

The application implements robust error handling:

1. **Network Errors:** Timeout and connection errors are caught and reported
2. **Missing Data:** Indicators not available for a country display "Not Available"
3. **Invalid Searches:** Non-existent countries prompt user to try again
4. **API Failures:** Graceful fallback when APIs are unreachable

---

## GitHub Repository Links

- **Main Repository:** [storm201/Country-Report](https://github.com/storm201/Country-Report)
- **Main File:** [country_report.py](https://github.com/storm201/Country-Report/blob/main/country_report.py)
- **README:** [README.md](https://github.com/storm201/Country-Report/blob/main/README.md)
- **Requirements:** [requirements.txt](https://github.com/storm201/Country-Report/blob/main/requirements.txt)

---

## Project Status

✅ **Complete and Functional**
- Core search functionality implemented
- World Bank API integration working
- User-friendly interactive interface
- Error handling implemented
- Sample screenshots documented

---

## Future Enhancement Possibilities

- [ ] Add filtering by region or population range
- [ ] Export reports to PDF/CSV formats
- [ ] Add caching to reduce API calls
- [ ] Implement comparison between multiple countries
- [ ] Add historical data tracking
- [ ] Create web interface using Flask/Django
- [ ] Add data visualization with charts

---

## Author

**GitHub:** [@storm201](https://github.com/storm201)

---

*Documentation Last Updated: June 11, 2026*
