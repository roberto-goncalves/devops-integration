import json
import dicttoxml
import os
from os import listdir
from os.path import isfile, join
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import zlib
import time
import base64

fd = open("public_key.pem", "rb")
public_key = fd.read()
fd.close()

def encrypt_files(file_name, public_key):
    rsa_key = RSA.importKey(public_key)
    rsa_key = PKCS1_OAEP.new(rsa_key)

    blob = zlib.compress(file_name)
    chunk_size = 470
    offset = 0
    end_loop = False
    encrypted =  ""

    while not end_loop:
        chunk = blob[offset:offset + chunk_size]
        if len(chunk) % chunk_size != 0:
            end_loop = True
            chunk += " " * (chunk_size - len(chunk))
        encrypted += rsa_key.encrypt(chunk)
        offset += chunk_size
    return base64.b64encode(encrypted)

while True:
    print "Waiting for JSON files to transform to XML..."
    onlyfiles = [f for f in listdir("json_directory") if isfile(join("json_directory", f))]
    for files in onlyfiles:
        print "Processing file: " + files
        json_object  = open("json_directory/"+files, "r")
        json_file = json.loads(json_object.read())
        json_object.close()
        xml = dicttoxml.dicttoxml(json_file)
        xml_object = open("xml_directory/"+files+".xml", "w")
        xml_object.write(xml)
        xml_object.close()
        print "File saved as XML in: " + "xml_directory/"+files+".xml" + " with content: "+ xml
        fd = open("xml_directory/"+files+".xml", "rb")
        unencrypted_xml = fd.read()
        fd.close()
        if(os.environ['DELETE_FILES'] == "True"):
            os.remove("xml_directory/"+files+".xml")
        encrypted_xml = encrypt_files(unencrypted_xml, public_key)
        fd = open("encrypt_directory/"+files, "wb")
        fd.write(encrypted_xml)
        fd.close()
        print "Sending XML ENCRYPTED file in: " + "encrypt_directory/"+files+".xml"+ " with content: "+ encrypted_xml
        if(os.environ['DELETE_FILES'] == "True"):
            os.remove("json_directory/"+files)
    time.sleep(10)


