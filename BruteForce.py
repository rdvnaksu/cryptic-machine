PassWord=input("Enter the password: ")

password = open("dict.txt", "r")
array=[]
numbers=[]
letters="0123456789abcdefghijklmnopqrstuvwxyz"
for m in range(1000):
	numbers+=[m]


x=""
storage=""
num=""
lines = password.readlines()
for pw in lines: 
	array+=[pw.strip()]

def check(x,p):
	if(PassWord==x):
		print("Password is: "+PassWord)
		return True
	else:
		print("Wrong password: "+ x)

def checkOthers():	
	for j in range (0,36):
		for i in array:
			x=i+letters[j]
			if check(x,PassWord):
				return		
			x=letters[j]+i
			if check(x,PassWord):
				return				
	for j in range (0,36):			
		for k in range(0,36):
			if k != j:
				for i in array:
					x=i+letters[k]+letters[j]
					if check(x,PassWord):
						return		
					x=letters[k]+letters[j]+i
					if check(x,PassWord):
						return
					x=letters[j]+i+letters[k]
					if check(x,PassWord):
						return			
				

for i in array:
	a= check(i, PassWord)
if a != True:
	checkOthers()
				    


