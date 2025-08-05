import requests
from bs4 import BeautifulSoup

def fetch_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        # Try to get headlines from <h2> tags, common for news sites
        headlines = [h2.get_text(strip=True) for h2 in soup.find_all("h2")]
        # Optionally, extend to <h1> or <title> if needed
        if not headlines:
            headlines = [title.get_text(strip=True) for title in soup.find_all("title")]
        return headlines
    except Exception as e:
        print(f"Error occurred: {e}")
        return []

def save_headlines_to_txt(headlines, filename="headlines.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for headline in headlines:
            f.write(headline + "\n")

if __name__ == "__main__":
    # Example: BBC News homepage (replace with any news site)
    url = "https://www.bbc.com/news"
    headlines = fetch_headlines(url)
    if headlines:
        save_headlines_to_txt(headlines)
        print(f"Saved {len(headlines)} headlines to headlines.txt")
    else:
        print("No headlines found.")