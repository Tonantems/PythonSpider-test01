import requests
from bs4 import BeautifulSoup
import re
resp = requests.get('http://jwlin.github.io/py-scraping-analysis-book/ch2/blog/blog.html')
soup = BeautifulSoup(resp.text, 'html.parser')

# titles = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
# for title in soup.find_all(re.compile('h[1-6]')):
# print(title.text.strip())

# 利用 regex 找出所有 .png 結尾的圖片
for img in soup.find_all('img', {'src': re.compile('beginner.*\.png$')}):
    print(img['src'])