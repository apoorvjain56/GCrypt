#making keys

import random
import string
a=[]
for i in string.ascii_letters:
    a.append(i)
#print(a)

#making value lists

b=a[:]
for i in range(10):
    b.append(str(i))
#print(b)
symbols = ['`','~','!','@','#','$','%','^','&','*','_','-','+','=','|','<','>','.','?','/']
#print(symbols)
for i in symbols:
    b.append(i)


#repeating this process 6 times for 6 diferent keys
#done on anaconda
encrypt=[]
decrypt=[]
for k in range(6):
    random.shuffle(b)
    en={' ':' '}
    de={' ':' '}
    for i in range(52):
        en[a[i]]=b[i]
        de[b[i]]=a[i]
    encrypt.append(en)
    decrypt.append(de)

print(encrypt)
print('\n')
print(decrypt)

