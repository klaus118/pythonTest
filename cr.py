from Cryptodome.Cipher import DES3,AES
from binascii import *
import os

def crypto(key,text,mode):

    if mode=="TDES":
        cipherD=cipherE = DES3.new(key, DES3.MODE_ECB)
    else:
        if mode=="AESecb":
            cipherD=cipherE = DES3.new(key, AES.MODE_ECB)
        else:
            if mode=="AEScbc":
                iv=unhexlify(b2a_hex(os.urandom(8)))
                cipherE = DES3.new(key, AES.MODE_CBC, iv)
                cipherD = DES3.new(key, AES.MODE_CBC, iv)

    ciphertext = cipherE.encrypt(text)
    print("ciphertext ", hexlify(ciphertext))
    text2 = (cipherD.decrypt(ciphertext))
    print("decrypted text ", text2)
    print(" original text ", text)

    if text == text2:
        return ("true\n")
    else:
        return ("false\n")
