import json
import dicttoxml
from os import listdir
from os.path import isfile, join
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import zlib
import base64
import os
import time

fd = open("private_key.pem", "rb")
private_key = fd.read()
fd.close()


def decrypt_files(file_name, public_key):
    rsakey = RSA.importKey(private_key)
    rsakey = PKCS1_OAEP.new(rsakey)
    encrypted_blob = base64.b64decode(file_name)
    chunk_size = 512
    offset = 0
    decrypted = ""
    while offset < len(encrypted_blob):
        chunk = encrypted_blob[offset: offset + chunk_size]
        decrypted += rsakey.decrypt(chunk)
        offset += chunk_size
    return zlib.decompress(decrypted)

while True:
    print "Waiting for files files to decrypt..."
    onlyfiles = [f for f in listdir("encrypt_directory") if isfile(join("encrypt_directory", f))]
    for files in onlyfiles:
        print "Processing file: " + files
        fd = open("encrypt_directory/"+files, "rb")
        encrypted_xml = fd.read()
        fd.close()
        if(os.environ['DELETE_FILES'] == "True"):
            os.remove("encrypt_directory/"+files)
        print "Recieved ENCRYPTED XML with content: " + encrypted_xml
        fd = open("decrypt_directory/"+files+".xml", "wb")
        decrypted = decrypt_files(encrypted_xml, private_key)
        fd.write(decrypted)
        fd.close()
        print "Saved DECRYPTED XML in " + "decrypt_directory/"+files+".xml" + " with content: " + decrypted
    time.sleep(10)
    


