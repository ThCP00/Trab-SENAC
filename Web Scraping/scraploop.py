from bs4 import BeautifulSoup
import requests
import csv

file = open("G1.csv", "w")
writer = csv.writer(file)
for i in range (1, 10):
    url = 'https://g1.globo.com/index/feed/pagina-' + str(i) + '.ghtml'

    content = requests.get(url)
    soup = BeautifulSoup(content.text, "html.parser")
    for item in soup.find_all('a', class_ = 'feed-post-link gui-color-primary gui-color-hover'):
        print(item.text)
        writer.writerow([item.text])
file.close()

