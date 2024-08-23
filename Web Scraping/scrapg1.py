from bs4 import BeautifulSoup
import requests

page_scrape = requests.get("https://g1.globo.com/")
soup = BeautifulSoup(page_scrape.text, "html.parser")
lidas = soup.findAll("a", attrs={"class": "feed-post-link gui-color-primary gui-color-hover"})

for i in lidas:
    print(i.text)
