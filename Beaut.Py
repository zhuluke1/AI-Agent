import requests
from bs4 import BeautifulSoup 

def fetch_headlines():
    url = "https://www.bbc.com/news"  # Example: BBC News
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []
    for item in soup.find_all('h3', limit=5):  # Fetch top 5 headlines
        headlines.append(item.text.strip())

    return headlines

# Test the function
print(fetch_headlines())
