import requests
from bs4 import BeautifulSoup
import smtplib
URL = 'https://www.amazon.com/gp/product/B07X6MJ4X7/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=dav0d2-20&creative=9325&linkCode=as2&creativeASIN=B07X6MJ4X7&linkId=332261ff2167c2b3adc3abd7fdf2bd13'

headers = {
    "User-Agent":
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup.prettify(), 'html.parser')

    productTitle = soup2.find(id="productTitle").get_text()
    productPrice = soup2.find(id="priceblock_ourprice").get_text()
    productPrice = productPrice.replace(',', '')

    priceConverted = float(productPrice[1:])
    if priceConverted < 1600.0:
        send_mail()

    print(priceConverted)
    print(productTitle.strip())

    if priceConverted < 1600.0:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('example@gmail.com', 'pass')
    subject = 'Price of the product you were looking for has fell down.'
    body = 'Check the amazon link https://www.amazon.com/gp/product/B07X6MJ4X7/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=dav0d2-20&creative=9325&linkCode=as2&creativeASIN=B07X6MJ4X7&linkId=332261ff2167c2b3adc3abd7fdf2bd13'

    message = f"Subject: {subject}\n\n{body}"

    server.sendmail('example@gmail.com', 'example@gmail.com', message)
    print('Email has been sent')
    server.quit()


check_price()
