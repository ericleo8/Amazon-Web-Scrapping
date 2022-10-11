from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime

url='https://www.amazon.com/Audioengine-Wireless-Bookshelf-Speakers-Resolution/dp/B017E10MPU/ref=sr_1_1_sspa?c=ts&keywords=Bookshelf+Speakers&qid=1665488900&qu=eyJxc2MiOiI3LjI4IiwicXNhIjoiNi40OCIsInFzcCI6IjUuNjcifQ%3D%3D&s=aht&sr=1-1-spons&ts_id=3236451011&psc=1&smid=A1MDP7AFOR891V'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(url, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")


soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
print(soup2)

title = soup2.find(id='productTitle').get_text()
price = soup2.find('span',class_='a-offscreen')
pricetext=price.text

print(title)
print(pricetext)


title=title.strip()
pricetext=pricetext.strip()[1:]
today = datetime.date.today()


type(pricetext)

import csv
header = ['Title', 'Price','Date']
data = [title,pricetext,today]

with open('AmazonWebScraper.csv', 'w', newline='', encoding='UTF8') as f:
    writer=csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

import pandas as pd
df = pd.read_csv('AmazonWebScraper.csv')
print(df)

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('ericleonardo.milis@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "The Headset you want is below $500! Now is your chance to buy!"
    body = "Eric, This is the moment we have been waiting for. Now is your chance to pick up the headset of your dreams. Don't mess it up! Link here: https://www.amazon.com/Audioengine-Wireless-Bookshelf-Speakers-Resolution/dp/B017E10MPU/ref=sr_1_1_sspa?c=ts&keywords=Bookshelf+Speakers&qid=1665488900&qu=eyJxc2MiOiI3LjI4IiwicXNhIjoiNi40OCIsInFzcCI6IjUuNjcifQ%3D%3D&s=aht&sr=1-1-spons&ts_id=3236451011&psc=1&smid=A1MDP7AFOR891V"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'ericleonardo.milis@gmail.com',
        msg
     
    )


def check_price():
    url='https://www.amazon.com/Audioengine-Wireless-Bookshelf-Speakers-Resolution/dp/B017E10MPU/ref=sr_1_1_sspa?c=ts&keywords=Bookshelf+Speakers&qid=1665488900&qu=eyJxc2MiOiI3LjI4IiwicXNhIjoiNi40OCIsInFzcCI6IjUuNjcifQ%3D%3D&s=aht&sr=1-1-spons&ts_id=3236451011&psc=1&smid=A1MDP7AFOR891V'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    print(soup2)

    title = soup2.find(id='productTitle').get_text()
    price = soup2.find('span',class_='a-offscreen')
    pricetext=price.text

    title=title.strip()
    pricetext=pricetext.strip()[1:]
    today = datetime.date.today()

    import csv
    header = ['Title', 'Price','Date']
    data = [title,pricetext,today]

    with open('AmazonWebScraper.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    
    if(price<600):
        send_mail()




while(True):
    check_price()
    time.sleep(5)


df=pd.read_csv('AmazonWebScraper.csv')
print(df)

