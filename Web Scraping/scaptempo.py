from bs4 import BeautifulSoup
import requests
import csv



file = open("prev_tempo.csv", "w")
writer = csv.writer(file)
writer.writerows(["max" , "min", "extra", "extra1", "prox"])
page_scrape = requests.get("https://g1.globo.com/previsao-do-tempo/df/brasilia.ghtml")
soup = BeautifulSoup(page_scrape.text, "html.parser")
temp_max = soup.find("div", attrs={"forecast-today__temperature forecast-today__temperature--max"})
print(temp_max.text)
temp_min = soup.find("div", attrs={"forecast-today__temperature forecast-today__temperature--min"})
print(temp_min.text)
extra = soup.find("div", attrs={"forecast-table__column"})
print(extra.text)
extra1 = soup.find("div", attrs={"forecast-table__column forecast-today-detail__extra-data"})
print(extra1.text)
prox = soup.find("div", attrs={"forecast-next-days__content"})
print(prox.text)


writer.writerow([temp_max.text])
writer.writerow([temp_min.text])
writer.writerow([extra.text])
writer.writerow([extra1.text])
writer.writerow([prox.text])
file.close()