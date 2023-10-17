# US City Directory Web Scraper
This repository houses a robust web scraper designed to navigate through the US City Directory website and extract valuable city-related information. The project showcases the power of Python combined with the Beautiful Soup and Requests libraries to parse complex website structures, retrieve data efficiently, and store it in a structured format.

## Features:
Deep Link Navigation: Traverses through state listings to individual city pages, ensuring comprehensive data extraction.

Multi-threading Support: Harnesses the power of multi-threading to expedite the scraping process, especially beneficial given the large number of pages.

Structured Data Storage: Extracted data is not only stored individually by city in the Data directory but can also be compiled into a single database-like structure for easy access.

Error Handling: Gracefully handles potential website structure changes, missing data, or other anomalies to ensure the scraper doesn't break midway.

## Usage:
Clone the repository.
Install the required dependencies: pip install -r requirements.txt
Run the main script: python main.py
## Output:
For each city, a JSON formatted .txt file will be generated containing the key city attributes. Moreover, a consolidated database-like file can also be generated, housing data from all scraped cities.

## Contributions:
Feel free to fork, enhance, or raise issues. This project welcomes contributions from web scraping enthusiasts and beginners alike!

## Me
### https://www.linkedin.com/in/kenneth-alonso-castillo-herrera/
