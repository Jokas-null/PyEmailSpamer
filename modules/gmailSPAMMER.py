import smtplib

class Gmail:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def send(self, to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.username, self.password)
        server.sendmail(self.username, to, content)
        server.quit()