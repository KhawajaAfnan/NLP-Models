import re
from urllib import request
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from pprint import pprint





# Patterns
phone_pattern = re.compile(r'\+?\d[\d -]{8,}\d')
email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')



url = 'https://www.dsu.edu.pk/contact-us/'

response = request.urlopen(url)
html = response.read().decode('utf8')
soup = BeautifulSoup(html, 'html.parser')
text =soup.get_text()

tokens = word_tokenize(text)
phone = set(re.findall(phone_pattern, text))
email = set(re.findall(email_pattern, text))


print("Tokens:")
#print(tokens) 

print("\nPhone Numbers:")
pprint(phone)

print("\nEmail Addresses:")
pprint(email)




