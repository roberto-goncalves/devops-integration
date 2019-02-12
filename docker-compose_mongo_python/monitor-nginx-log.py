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

myclient = pymongo.MongoClient("mongodb://mongodb:27017/")
mydb = myclient["ebot7"]
mycol = mydb["access"]

while True:
    if p.poll(1):
        line = f.stdout.readline()
        array = line.split("%")
        insert_row = {"date": array[0], "agent_string": array[1], "response": array[2][:3]}
        result = mycol.insert_one(insert_row)
    time.sleep(1)