import requests
from bs4 import BeautifulSoup

def fetch_headlines(url="https://www.bbc.com/news"):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch the page: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract headlines - this may vary by site
    headline_tags = soup.find_all(["h1", "h2"], limit=20)  
    headlines = [tag.get_text(strip=True) for tag in headline_tags if tag.get_text(strip=True)]
    
    return headlines

def save_headlines(headlines, filename="headlines.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for i, headline in enumerate(headlines, 1):
            file.write(f"{i}. {headline}\n")
    print(f"Saved {len(headlines)} headlines to {filename}")

def main():
    print("Fetching headlines...")
    headlines = fetch_headlines()
    if headlines:
        save_headlines(headlines)
    else:
        print("No headlines found.")

if __name__ == "__main__":
    main()
