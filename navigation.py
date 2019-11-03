import requests
from bs4 import BeautifulSoup

resp = requests.get('http://jwlin.github.io/py-scraping-analysis-book/ch2/table/table.html')
soup = BeautifulSoup(resp.text, 'html.parser')

# 儲存課程價錢list
# 取得所有課程售價 : 方法一, 使用index

# rows = soup.find('table', 'table').tbody.find_all('tr')
# for row in rows:
    # price = row.find_all('td')[2].text  # 第3個<td>(index為2)
    # prices.append(int(price))
    # print(sum(prices)/len(prices))  # 計算課程均價

# 取得每一列所有的欄位資訊 : find_all('td') or row.chlidren
rows = soup.find('table', 'table').tbody.find_all('tr')
for row in rows:
    # method.1 find_all('td')
    all_tds = row.find_all('td')
    # method.2 找出row(<tr>) 所有的直接(下一層) children
    all_tds = [td for td in row.children]
    # get href Attributes before check presence
    if 'href' in all_tds[3].a.attrs:
        href = all_tds[3].a['href']
    else:
        href = None
        print(all_tds[0].text, all_tds[1].text, all_tds[2].text, href, all_tds[3].a.img['src'])