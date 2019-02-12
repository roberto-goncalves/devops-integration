import pymongo
import smtplib
import time


myclient = pymongo.MongoClient("mongodb://mongodb:27017/")
mydb = myclient["ebot7"]
mycol = mydb["access"]



def createmail():
    gmail_user = 'roberto.forsaken@gmail.com'  
    gmail_password = 'Fartoysoldiers.25'

    sent_from = gmail_user  
    to = ['roberto.forsaken@gmail.com']  
    subject = 'ALERT - ACCESS DENIED IN SERVER'  
    body = 'This is an alert'

    email_text = """\  
    From: %s  
    To: %s  
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.connect('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print 'Email sent!'
        mycol.drop()
    except Exception as e:  
        print 'Error: ' + str(e)

while True:
    cursor = mycol.find({"response":'401'})
    print cursor.count()
    if cursor.count() > 10:
        print 'Attempting to send email...'
        createmail()
    time.sleep(1200) #20 min
