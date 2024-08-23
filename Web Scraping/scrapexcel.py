from bs4 import BeautifulSoup
import requests
import csv


file = open("scraped_quotes.csv", "w")
writer = csv.writer(file)
writer.writerow(["Quote" , "Author"])
page_scrape = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_scrape.text, "html.parser")
quotes = soup.findAll("span", attrs={"class": "text"})
authors  = soup.findAll("small", attrs={"class": "author"})

for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)
    writer.writerow([quote.text, author.text])
file.close()