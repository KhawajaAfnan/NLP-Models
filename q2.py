from urllib import request
from bs4 import BeautifulSoup

url = 'https://www.dsu.edu.pk/contact-us/'
response = request.urlopen(url)
html = response.read().decode('utf8')
        
soup = BeautifulSoup(html, 'html.parser')
        
result=soup.get_text()



print(result)
