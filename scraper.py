from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

# creating a file and writing headers

f = open('dziekanat.csv', 'w')
headers = 'title, name, room, phone number, email adress\n'
f.write(headers)

# getting data from the website

with urlopen('http://www.imir.agh.edu.pl/pl/wydzial/wladze_wydzialu/dziekanat/') as html_data:
    page_text = html_data.read()
    page_soup = soup(page_text, 'html.parser')
    soup_info = page_soup.find('div', id='contentStaticSite')

# extracting desired information

for person_info in soup_info.find_all('p')[6:]:
    title = person_info.strong.text.replace(',', ' |').replace(':', '')
    name = person_info.contents[2].strip()
    room = person_info.contents[4].strip().replace(',', ' |')
    phone_number = person_info.contents[6].strip().replace('tel. ', '')
    mail = person_info.a.text

    # writing extracted data to our .csv file

    f.write(title + ',' + name + ',' + room + ',' + phone_number + ',' + mail + '\n')
