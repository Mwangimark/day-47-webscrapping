from dotenv import load_dotenv
import os
import smtplib

from_email = os.getenv("FROM_EMAIL")
app_password = os.getenv("PASSWORD")

class Email:
    def sendingEmail(self, product_title, url):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(from_email, app_password)

            subject = f"Price of coffee machine\n {product_title}"
            body = f"The price of coffee machine is lower than 30 , you can purchase it now from: \n{url}"
            message = subject + "\n" + body

            connection.sendmail(from_addr=from_email,
                                to_addrs=from_email,
                                msg=message
                                )

