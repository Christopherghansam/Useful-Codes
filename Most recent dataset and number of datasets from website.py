from lxml import html
import requests
response = requests.get('http://catalog.data.gov/dataset?q=&sort=metadata_created+desc')
doc = html.fromstring(response.text)
title = doc.cssselect('h3.dataset-heading')[0].text_content()
print("The name of the most recently added dataset on data.gov:")
print(title.strip())

response1 = requests.get('http://www.data.gov/')
doc_gov = html.fromstring(response1.text)
link_gov = doc_gov.cssselect('small a')[0]
print("Number of datasets currently listed on data.gov:")
print(link_gov.text)