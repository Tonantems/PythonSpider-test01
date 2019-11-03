import requests
from bs4 import BeautifulSoup

resp = requests.get('http://www.yeastract.com/view.php?existing=regulation&proteinname=Abf1p&orfname=YKL112W')
soup = BeautifulSoup(resp.text, 'html.parser')
divs = soup.find_all('td', 'align', '2')
for div in divs:
    print([s for s in div.stripped_strings])