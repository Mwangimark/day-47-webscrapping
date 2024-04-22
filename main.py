
import requests
from bs4 import BeautifulSoup
from email_sender import Email

email = Email()
url = "https://www.amazon.com/dp/B0C2DZZ637/ref=twister_B0CXQ2716D?_encoding=UTF8&th=1"

response = requests.get(url)

if response:
    soup = BeautifulSoup(response.text, "html.parser")
    product = soup.find('span',{'id':'productTitle','class':'a-size-large product-title-word-break'})
    product_title = product.text
    cost = soup.find('span', {'class': 'a-price-whole'})
    actual_cost = int(cost.text.strip("."))

    if actual_cost < 30:
        try:
            email.sendingEmail(product_title,url)
            print("Mail sent successfully")
        except Exception as e:
            print(e)
    else:
        print("price not lower")
else:
    print("no response yet")
