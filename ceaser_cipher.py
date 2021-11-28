def encrypt(msg,key):
    msg = msg.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for i in msg :
        if i in alpha:
            index = (alpha.find(i)+key) % len(alpha)
            result += alpha[index] 
    return result.lower()
    
def decrypt(msg,key):
    msg = msg.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for i in msg :
        if i in alpha:
            index = (alpha.find(i)-key) % len(alpha)
            result += alpha[index] 
    return result.lower()
    
def brute_force(ciphet):
    ciphet = ciphet.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0,26):
        result = ""
        for j in ciphet :
            if j in alpha :
                index = (alpha.find(j)-i) % len(alpha)
                result += alpha[index]
        print("Key #",i," = ",result.lower())
    
if __name__ == "__main__":
    while(1):
        x = int(input("Enter ur choice : [(1.Encrypt 2.Decrypt 3.Brute Force 4.Exit)] : "))
        if x==1:
            Message = input("\nEnter the text : ")
            key = int(input("Enter key value : "))
            cipher = encrypt(Message,key)
            print("Cipher text is : ",cipher)
        elif x==2:
            Message = input("\nEnter the text : ")
            key = int(input("Enter key value : "))
            plain = decrypt(Message,key)
            print("Plain text is : ",plain)
        elif x==3:
            brute_force(cipher)
        else:
            exit()