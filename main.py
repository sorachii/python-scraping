import requests as rs
from bs4 import BeautifulSoup

page = rs.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.title
head = soup.head
body = soup.body

first_h1 = soup.select('h1')[0]
seventh_p_text = soup.select('p')[6]
top_items = []

products = soup.select('div.thumbnail')

for elem in products:
    title = elem.select('h4 > a.title')[0].text
    review_label = elem.select('div.ratings')[0].text
    x = elem.select('h4.pull-right.price')[0].text
    info = {
       "title": title.strip(),
       "review": review_label.strip(),
       "price": x
    }
    top_items.append(info)


print(top_items)
