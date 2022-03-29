from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://news.ycombinator.com/').text
print(html_text)

