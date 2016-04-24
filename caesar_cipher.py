def caesarcipher(b,s):
        a="abcdefghijklmnoprstuvwxyz"
        x=""
        for i in range(len(s)):
                for j in range(len(a)):
                        if s[i] is a[j]:
                                break
                x+=b[j]        
                        
        return x

def makeitnormal(b,s):
        a="abcdefghijklmnoprstuvwxyz"
        x=""       
        for i in range(len(s)):
                for j in range(len(a)):
                        if s[i] is b[j]:
                                break
                x+=a[j]        
                
        return x

def changekey(b):
        inp=input("please enter a number for change the key: ")
        for i in inp:
                temp=b[0]
                b=b.replace(b[0],"")
                b+=temp
        return b

def editor(s):
        x=""
        for i in s:
                if i.isalpha():
                        if i.isupper():
                                x+=i.lower()
                        else:
                                x+=i
        return x

def checkfile():
        file=open("caesar.txt","r")
        key=file.readline()
def caesarmenu():
        

a="abcdefghijklmnoprstuvwxyz"
b="abcdefghijklmnoprstuvwxyz"
