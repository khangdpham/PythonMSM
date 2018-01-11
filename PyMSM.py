import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def SendMail(ImgFileName):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'From SmartHome'
    msg['From'] = 'username.bot@gmail.com'
    msg['To'] = '1234567890@msg.fi.google.com'

    text = MIMEText("Taco from smarthome")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("username.bot","password")
    s.sendmail("noreply@gmail.com","1234567890@msg.fi.google.com", msg.as_string())
    s.quit()
        
if __name__ == '__main__':
    SendMail('taco.jpg')
