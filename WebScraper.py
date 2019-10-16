import requests
from bs4 import BeautifulSoup
import pyautogui
page = requests.get('http://nypost.com')

list = []
newList = []
contentOfPage = page.content

soup = BeautifulSoup(contentOfPage, 'html.parser')

for webLinks in soup.find_all('a'):
    otherArticles = webLinks.get('href')
    list.append(otherArticles)

print(list)

num = 0

for websites in list:
    indexx = list.index(websites)
    placement = websites.find('2019')
    if placement == -1:
        list.pop(indexx)
    else:
        newList.append(newList)
