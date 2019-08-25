import requests 
from bs4 import BeautifulSoup

result = requests.get('https://www.google.com/')
# To check status of page . f 200 than accesible
# print(result.status_code)

# To Chech the data in header
# print(result.headers)

# To check the page content of website accesed
src = result.content
# print(src)

soup = BeautifulSoup(src, 'lxml')

links = soup.find_all('a')
# print(links)
# print('\n')

for link in links:
    if 'About' in link.text:
        print(link)
        print(link.attrs['href'])