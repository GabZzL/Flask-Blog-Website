import requests
import smtplib


class Blogs:
    def __init__(self):
        self.URL = "https://api.npoint.io/f898f61d299f18b0fa2f"
        self.response = requests.get(url=self.URL)

    def get_blogs(self):
        return self.response.json()


class Email:
    def __init__(self, name, email, phone_number, message):
        # set your email information
        self.MY_ACCOUNT = "your email account"
        self.PASSWORD = "password account"
        self.text = f"name: {name}\nemail: {email}\nphone: {phone_number}\n{message}"

    def send_email(self):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.MY_ACCOUNT, password=self.PASSWORD)
            connection.sendmail(from_addr=self.MY_ACCOUNT,
                                to_addrs="armandogabrieljl@gmail.com",
                                msg=f"Subject:Blog Website (Contact)\n\n{self.text}")
