import requests
# response = requests.get("https://en.wikipedia.org/robots.txt")
response = requests.get("https://en.wikipedia.org/wiki/MediaWiki:Robots.txt")
test =  response.text
print("robots.txt for http://www.wikipedia.org/")
print("===================================================")
print(test)
#Practical web scraping for data science was instrumental in the construction of this code.