import random
import string

#rotates letters in alphabet by number i.e if variable rotate is 1 then cipher would be [B,C,D...,Z,A]
def make_cipher(rotate):
    alphabet = list(string.ascii_uppercase)
    cipher = alphabet[rotate:] + alphabet[:rotate]
    return cipher

#turns a normal string into a random caesars cypher
def encipher(text):
    cipher = make_cipher(random.randint(1,25))
    #cipher = make_cipher(0)
    text = text.upper()
    enciphered = ""
    alphabet = list(string.ascii_uppercase)
    for i in range(len(text)):
        for j in range(26):
            if text[i] == alphabet[j]:
                enciphered += cipher[j]
        if text[i] not in alphabet:
            enciphered += text[i]  
    return enciphered            


def decipher(text):
    alphabet = list(string.ascii_uppercase)
    final_scores = [0]*26
    deciphers = ['']*26
    for i in range(26):
        #scoring system based on how often a letter shows up in the english language
        scores = [8000,1600,3000,4400,12000,2500,1700,6400,8000,400,800,4000,3000,8000,8000,1700,500,6200,8000,9000,3400,1200,2000,400,2000,200]
        cipher = make_cipher(i)
        for j in range(len(text)): 
            for k in range(26):
                if cipher[k] == text[j]:
                    final_scores[i] += scores[k]
                    deciphers[i] += alphabet[k]
                elif text[j] not in alphabet:
                    deciphers[i] += text[j]
                    break
    highest_index = 0
    for i in range(len(deciphers)):
        if final_scores[i] > final_scores[highest_index]:
            highest_index = i      
    return deciphers[highest_index]                    

word = encipher("While at the International Computer Science Institute (ICSI), Handley co-founded the AT&T Center for Internet Research, as well as the XORP open-source router project (2000).[7] \
Handley is a contributor to Internet Engineering Task Force (IETF) standards and a member of the IETF Routing Area Directorate and the Transport Area Directorate.[8] Previously he was a member of the Internet Architecture Board (IAB)[9] and chaired the IETF Multiparty Multimedia Session Control working group[10] and the IRTF Reliable Multicast Research Group.[11] He is the author or co-author of 34 Request for Comments (RFCs), including the Session Initiation Protocol,[12] Multipath TCP[13] and a series of other network protocols.")
print("deciphered statement is:\n", decipher(word))