# BBC News Headlines Scraper  

## Objective  
This project fetches the latest news headlines from the **BBC News** website and saves them into a text file.  

## Tools Used  
- **Python**  
- **requests** (for fetching webpage data)  
- **BeautifulSoup (bs4)** (for parsing HTML)  

## Features  
- Scrapes up to **20 latest headlines** from BBC News.  
- Saves headlines in a neatly formatted `headlines.txt` file.  
- Handles network errors gracefully.  

## How It Works  
1. Sends a GET request to BBC News.  
2. Parses the response HTML to extract `<h1>` and `<h2>` tags.  
3. Saves the extracted headlines into `headlines.txt`.  

## Usage  
1. Install dependencies:  
   ```bash
   pip install requests beautifulsoup4
