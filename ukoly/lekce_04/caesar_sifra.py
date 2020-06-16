#continue = True

while(True):
    key = input("Zadejte prosim hodnotu klice: ")
    # kontrola klice
    if(key.isdigit()):
        plaintext = input("Prosim zadejte text k zasifrovani: ")
        ciphertext = ""

        #sifrovani po jednom znaku
        for i in range(len(plaintext)):
            pi = plaintext[i]
            if(pi.isupper()):
                ciphertext += chr((ord(pi) + int(key) - 65) % 26 + 65)
            elif(pi.islower()):
                ciphertext += chr((ord(pi) + int(key) - 97) % 26 + 97)
            
            # znaky mimo abecedu zustavaji stejne
            else:
                ciphertext += pi

        print("Plain text: " + plaintext)
        print("Key: " + key)
        print("Cipher: " + ciphertext)
        break
    else:
        print("Klic musi byt cele kladne cislo")