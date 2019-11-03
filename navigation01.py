import requests
from bs4 import BeautifulSoup

resp = requests.get('http://jwlin.github.io/py-scraping-analysis-book/ch2/table/table.html')
soup = BeautifulSoup(resp.text, 'html.parser')

rows = soup.find('table', 'table').tbody.find_all('tr')
for row in rows:
    print([s for s in row.stripped_strings])  # s for s 是甚麼?