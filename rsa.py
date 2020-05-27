from math import *
'''
    RSA Cryptography System
        Steps :
            1) take input two variables p and q as prime
            2) apply touation formula to find total prime factors of p*q
            3) display all possible public exponent 
            4) take input public exponent of given list
            5) extract public key
            6) find private exponent using chinese remainder theorem
            7) extract private key
            8) take input message from user
            9) Apply Encryption ---> for message security
            10) Apply decryption ---> to get message
        Note :
            If p and q are very large prime numbers then probability of breaking the message is 
            impossible in this era.

'''

def prime_check(var):
    count=0
    for i in range(2,int(sqrt(var))+1):
        if var%i==0 and var>2:
            count+=1
    if count:
        return False
    else:
        return True
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def coprimes(a):
    l = []
    for x in range(2, a):
        if gcd(a, x) == 1 and modinv(x,pie) != None:
            l.append(x)
    for x in l:
        if x == modinv(x,pie):
            l.remove(x)
    return l
def rsa_encryption(s,e,n):
    store_message_values=[]
    for temp in s:
        i = ord(temp)
        c = (i**e)%n
        store_message_values.append(c)
    return store_message_values


    
def rsa_decryptrion(encryptkey , prvt_key , n ):
    decrypt_message=""
    for temp in encryptkey:
        m = (temp**prvt_key)%n
        decrypt_message += chr(m)
    return decrypt_message


print("------------------RSA CRYPTOGRAPHY SYSTEM------------------")
p = int(input("Enter Prime Number 1  : "))
q = int(input("number Prime Number 2 : "))
if prime_check(p) and prime_check(q):
    n=p*q
    print(f"Prime Multiplication : {n}")
    pie=(p-1)*(q-1)
    print(f"Total Number Of Prime Factors P*Q = {pie}")
    print("--All Possible Public Exponents Are Listed Below--")
    print(coprimes(pie))
    print("Select Public Exponent From Given list : ",end='')
    s_pe = int(input())
    if s_pe in coprimes(pie):
        print(f"--------------Public Key({s_pe},{n})--------------")
        d=modinv(s_pe,pie)
        print(f"--------------Private Key({d},{n})--------------")
        print("Enter Ur Message : ",end='')
        plain_text = input()
        encrypt=rsa_encryption(plain_text,s_pe,n)
        encrypted_mssg=[]
        for i in encrypt:
            encrypted_mssg.append(chr(i))
        print("------------Encrypting Message------------")
        print(f"Encrypted Messaege = {encrypted_mssg}")

        decrypted_mssg=rsa_decryptrion(encrypt,d,n)
        print("------------Decrypting Message------------")
        print(f"Decrypted Messaege = {decrypted_mssg}")


    else:
        print("invalid public exponent selection")


else:
    print('both are not prime')

print("Press Key To Terminate The Program : ",end='')
press=input()

