import time
import subprocess
import select
import os
import re
import sys, getopt
import pymongo

f = subprocess.Popen(['tail','-F', "/usr/log/access.log"],\
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
p = select.poll()
p.register(f.stdout)

while True:
    if p.poll(1):
	myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
	mydb = myclient["ebot7"]
	mycol = mydb["access"]
        line = f.stdout.readline()
        array = line.split("%")
	print array
        insert_row = {"date": array[0], "agent_string": array[1], "response": array[2][:3]}
        result = mycol.insert_one(insert_row)
	myclient.close()
    time.sleep(1)
