from requests_html import HTMLSession

s = HTMLSession()

url = 'https://www.google.com/search?q=clima+brasilia'

r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'})

temp = r.html.find('span#wob_tm', first=True).text
unidade = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
print(r.html.find('div.nawv0d', first=True))
