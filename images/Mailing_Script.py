import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd



#1
col = pd.read_csv("publicity.csv")
names = col["PARTICIPANT"]
mails = col["EMAIL ID"]



#2
des1 = 'participants_final//'
body = """\

Yaha par body likh.

    """
subject = "Appreciation certificates of Adhyaaya 2020: The technical symposium of GCOE,Nagpur."
sender = "adhyaaya.gcoen@gmail.com"
senderPassword = "adh@GCOEN2020"




#3
for i in range(len(names)):
    filename = des1 + "//" + names[i] + ".pdf"
    receiver = mails[i]

    #instance of MIMEmultipart
    msg = MIMEMultipart()   

    #Sender, Receiver, Subject and Body
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject

    #Attaching body with mail
    msg.attach(MIMEText(body, 'plain'))

    #Attachment
    attachment = open(filename, "rb")

    #Instance of MIMEBase named as p
    p = MIMEBase('application', 'octet-stream')

    #To change the payload into encoded form
    p.set_payload((attachment).read())

    #encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename = %s" % names[i]+".pdf")

    #attach the attachment
    msg.attach(p)

    #create SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender, senderPassword)

    #converts the Multipart msg into a string
    text = msg.as_string()

    s.sendmail(sender, receiver, text)
    s.quit()