from binascii import *
import cr

import os


text = (b2a_hex(os.urandom(16)))
key=b2a_hex(os.urandom(24))

print ("text ",text)
print ("key ",key,"\n")


key = unhexlify(key)

print(cr.crypto(key,text,"TDES"))
print(cr.crypto(key,text,"AESecb"))
print(cr.crypto(key,text,"AEScbc"))



