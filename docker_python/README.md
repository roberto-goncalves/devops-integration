Python with docker-compose pipeline for a integration between two containers for encrypt and decrypt JSON files

- Objective: JSON -> XML -> encryption -> transfer -> decryption -> XML

- INSTRUCTIONS

   Execution: docker-compose up
   ATTENTION: set DELETE_FILES environment variable to False and see each file saved on directory.
   If DELETE_FILES == True, only directory that files will not be deleted is: decrypt_directory

- Explanation

1. JSON files need to be inserted in json_directory(host machine) that is mapped according to docker-compose.yml
2. Every 10 seconds container_a.py will read from json_directory
3. container_a will transform the JSON file into XML file and transfer it to xml_directory
4. container_a will read XML content and encrypt it with RSA encryption key(public_key.pem)
5. container_a will delete readed files from json_directory and xml_directory to ensure pipeline's atomicity
6. container_a will save the encrypted content on encrypt_directory
7. Every 10 seconds container_b will read from encrypt_directory
8. container_b will decrypt any files encrypted with public_key.pem using RSA private_key.pem
9. container_b will delete readed files from encrypt_directory to ensure pipeline's atomicity
10. container_b will transform decrypted content in XML file and save in decrypt_directory

Obs: The deleted content will be printed on container stdout for testing

- Extras

If wanted, you can generate your own keys using generate_key.py, just remember to delete the old ones. The encryption algorithm was inspired from https://medium.com/@ismailakkila/black-hat-python-encrypt-and-decrypt-with-rsa-cryptography-bd6df84d65bc

