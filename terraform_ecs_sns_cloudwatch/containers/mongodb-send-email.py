import pymongo
import smtplib
import time


myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb = myclient["ebot7"]
mycol = mydb["access"]

while True:
    myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    mydb = myclient["ebot7"]
    mycol = mydb["access"]
    cursor = mycol.find({"response":'401'})
    print cursor.count()
    if cursor.count() > 10:
        print 'ACCESS VIOLATION'
        mycol.drop()
    myclient.close()
    time.sleep(10) #20 min
