'''
* Author:  Dyuthi Pedaballi
'''
""" j is replaced by i, "X" is inserted between repeated
letters and also used for padding if the plaintext has an odd length"""

#remove spaces and duplictae letters from teh key
ikey = "first"  
def removekeydups(ikey):
    ikey = ikey.replace(" ","")
    key = ""
    for letter in ikey:
        if letter not in key:
           key = key + letter
    return key
    
key = removekeydups(ikey)

def keytable(key):
    
    alphabet = "abcdefghijKLmnopqrstuvwxyz"
    alphabet = alphabet.lower()
    alphabet = alphabet.replace("j", "i")
    keytable = ""
    for letter in alphabet:
      if letter not in key:
          if letter not in keytable:
           keytable = keytable+letter
    keytable = key+keytable
    return(keytable)

#Creating a keymatrix, by including in it distinct letters in key and alphabet
def keysquare():
    
   keyref = keytable(key)
   keylist = []
   keylist1 = []
   keylist2 = []
   keylist3 = []
   keylist4 = []
   keylist5 = []
      
   row1 = keyref[0:5]
   for ch in row1:
     keylist1.append(ch)

   row2 = keyref[5:10]
   for ch in row2:
     keylist2.append(ch)
     
   row3 = keyref[10:15]
   for ch in row3:
     keylist3.append(ch)

   row4 = keyref[15:20]
   for ch in row4:
     keylist4.append(ch)

   row5 = keyref[20:25]
   for ch in row5:
     keylist5.append(ch)

   keylist.append(keylist1)
   keylist.append(keylist2)
   keylist.append(keylist3)
   keylist.append(keylist4)
   keylist.append(keylist5)
   
   
   return keylist
iplaintext = "hi there dyuthi"

"""Removing spaces from the plaintext and appending with "x"
in case of odd length plaintext"""

def cleanplaintext(iplaintext):
    if " " in iplaintext:
     iplaintext = iplaintext.replace(" ","")
    mplaintext = ""

    for letindex in range(len(iplaintext)-1):
         
         if iplaintext[letindex] == iplaintext[letindex+1]:
            mplaintext =  mplaintext+iplaintext[letindex]+"x"
         else:
            mplaintext = mplaintext+iplaintext[letindex]
            
    mplaintext = mplaintext+iplaintext[-1]
    return mplaintext
    
space = []
for index in range(len(iplaintext)):
    if iplaintext[index] == " ":
     space.append(index)
     
#Splitting the plaintext into pairs             
def makedigraps():
    char = []
    mplaintext = cleanplaintext(iplaintext)
    plaintext = ""
    if len(mplaintext)%2 == 0:
        plaintext = mplaintext
    else:
        plaintext = mplaintext+"x"
    
    for ch in plaintext:
        char.append(ch)
    
    digraph = []
    
    for index in range(0,len(char),2):
      digraph.append(char[index:index+2])
    return digraph

#Encrypts message by using the three rules
def encrypttext():
    
    keymatrix = keysquare()
    char = makedigraps()
    ciphertext = []
    index1 = 0
    index2 = 0
    index3 = 0
    index4 = 0
    for ch in char: 
        for i in range(len(keymatrix)):
            for j in range(len(keymatrix)):
              if ch[0] == keymatrix[i][j]:
                index1 = i
                index2 = j
                j =0
                i =0
            
        for i in range(len(keymatrix)):
            for j in range(len(keymatrix)):
               if ch[1] == keymatrix[i][j]:
                         index3 = i
                         index4 = j                   
                             
        if index1==index3:
                             
                 if index2 == 4:
                     index2= 0
                     ciphertext.append(keymatrix[index1][index2])
                     ciphertext.append(keymatrix[index3][index4+1])
                 elif index4 == 4:
                      index4 = 0

                      ciphertext.append(keymatrix[index1][index2+1])
                      ciphertext.append(keymatrix[index3][index4])
                 else:
                      ciphertext.append(keymatrix[index1][index2+1])
                      ciphertext.append(keymatrix[index3][index4+1])
                          
        elif index2 == index4:
                    if index1 == 4:
                        index1 = 0
                        ciphertext.append(keymatrix[index1][index2])
                        ciphertext.append(keymatrix[index3+1][index4])
                    elif index3 == 4:
                        index3 = 0
                        ciphertext.append(keymatrix[index1][index2])
                        ciphertext.append(keymatrix[index3+1][index4])
                    else:
                        ciphertext.append(keymatrix[index1+1][index2])
                        ciphertext.append(keymatrix[index3+1][index4])
        else:
                     ciphertext.append(keymatrix[index1][index4])
                     ciphertext.append(keymatrix[index3][index2])
    if " " in iplaintext:
     for index in range(len(space)):   
      ciphertext.insert(space[index]," ")

    cipherstr = "".join(ciphertext)
    
    print("The ciphertext for the given plaintext:",cipherstr)
    return cipherstr

#decrypts message by using the three rules
def decrypttext():
    cipher = encrypttext()
    cipheros = cipher.replace(" ","")
    cipherdi = []
    for index in range(0,len(cipheros),2):
        cipherdi.append(cipheros[index:index+2])

    keymatrix = keysquare()
    plaintextc = []
    index1 = 0
    index2 = 0
    index3 = 0
    index4 = 0
    for ch in cipherdi: 
        for i in range(len(keymatrix)):
            for j in range(len(keymatrix)):
              if ch[0] == keymatrix[i][j]:
                index1 = i
                index2 = j
                j =0
                i =0
        for i in range(len(keymatrix)):
            for j in range(len(keymatrix)):
               if ch[1] == keymatrix[i][j]:
                         index3 = i
                         index4 = j
                             
        if index1==index3:
                             
                 if index2 == 0:
                     index2= 4
                     plaintextc.append(keymatrix[index1][index2])
                     plaintextc.append(keymatrix[index3][index4-1])
                 elif index4 == 0:
                      index4 = 4
                      plaintextc.append(keymatrix[index1][index2-1])
                      plaintextc.append(keymatrix[index3][index4])
                 else:
                      plaintextc.append(keymatrix[index1][index2-1])
                      plaintextc.append(keymatrix[index3][index4-1])
                          
        elif index2 == index4:
                    if index1 == 0:
                        index1 = 4
                        plaintextc.append(keymatrix[index1][index2])
                        plaintextc.append(keymatrix[index3][index2])
                    elif index3 == 0:
                        index3 = 4
                        plaintextc.append(keymatrix[index1][index2])
                        plaintextc.append(keymatrix[index3-1][index4])
                    else:
                        plaintextc.append(keymatrix[index1-1][index2])
                        plaintextc.append(keymatrix[index3-1][index4])
        else:
                     plaintextc.append(keymatrix[index1][index4])
                     plaintextc.append(keymatrix[index3][index2])
    
    if "x" in plaintextc:
      plaintextc.remove("x")
    if " " in cipher:
        for index in range(len(space)):
           plaintextc.insert(space[index]," ")
    plainstr = "".join(plaintextc)

    print("The plaintext for the given ciphertext:",plainstr)

decrypttext()
