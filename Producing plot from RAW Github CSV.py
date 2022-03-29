from bs4 import BeautifulSoup
from requests import get
import re

page = "https://www.eurocham-cambodia.org/member/476/2-LEau-Protection"

content = get(page).content
soup = BeautifulSoup(content, "lxml")

exp = re.compile(r"(?:.*?='(.*?)')")
# Find any element with the mail icon
for icon in soup.findAll("i", {"class": "icon-mail"}):
    # the 'a' element doesn't exist, there is a script tag instead
    script = icon.next_sibling
    # the script tag builds a long array of single characters- lets gra
    chars = exp.findall(script.text)
    output = []
    # the javascript array is iterated backwards
    for char in reversed(list(chars)):
        # many characters use their ascii representation instead of simple text
        if char.startswith("|"):
            output.append(chr(int(char[1:])))
        else:
            output.append(char)
    # putting the array back together gets us an `a` element
    link = BeautifulSoup("".join(output))
    email = link.findAll("a")[0]["href"][8:]
    # the email is the part of the href after `mailto: `
    print(email)
