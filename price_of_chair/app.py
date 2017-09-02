__author__ = 'Manu Arora'
# IF we want to request a page from the internet, we need a library called requests. Makes it pretty easy to GET requests

import requests
from bs4 import BeautifulSoup
request = requests.get("http://www.amazon.in/Afydecor-A-CH034-Wingback-Chair-Off-White/dp/B019DR97A4/ref=sr_1_1?s=kitchen&ie=UTF8&qid=1503586475&sr=1-1-spons&keywords=chair&psc=1")

# Prints HTML code of Amazon.com
#<span id="priceblock_saleprice" class="a-size-medium a-color-price"><span class="currencyINR">&nbsp;&nbsp;</span> 23,245.00</span>

# print request.content To print the complete page

content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"id": "priceblock_saleprice" , "class": "a-size-medium a-color-price"})

print(element.text.strip())