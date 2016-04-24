def inputText():
	"read the text file to read"
	file=open("input.txt","r")
	a = file.read()
	file.close()
	return a

def plainText(text):
	"turn all text into plain text with all upper-case and no spacing"

	text2 = ""
	for char in text:
		if char.isalpha():
			text2+=char
	text2= text2.upper()
	return text2

def analyzeFrequent(text):
	"return the analysis of frequency in text"

	alphabet = "abcdefghijklmnopqrstuvwxyz"
	freq = [8.5, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, 0.2, 0.8, 4.0, 2.4, 6.7, 7.5, 1.9, 0.1, 6.0, 6.3, 9.1, 2.8, 1.0, 2.4, 0.2, 2.0, 0.1]
	occurLetter = [0]*26
	for i in range (0,26):
		frequencyList[0][i] = alphabet[i]
		frequencyList[1][i] = str(freq[i])
		frequencyList[2][i] = alphabet[i].upper()

	for char in text:
		for i in range (0,26):
			if char == frequencyList[2][i]:
				occurLetter[i] += 1				

	lengthText = float(len(text))
	for i in range (0,26):
		frequencyList[3][i] = str(int(occurLetter[i]*1000/lengthText)/10.0)

	for i in range (0,26):
		for j in range (0, 2):
			print frequencyList[j][i],		
		print "\t",
		for j in range (2, 4):
			print frequencyList[j][i],		
		print

def topFive(text):
	"tops = ETAOI"
	tops = [[0]*5 for i in range(3)]
	tops[0] = ["E", "T", "A", "O", "I"]	
	for i in range(0,26):
		if float(frequencyList[3][i]) >= float(tops[1][0]):
			tops[2][0] = frequencyList[2][i]
			tops[1][0] = frequencyList[3][i]				
			
	for j in range(1,5):
		for i in range(0,26):
			if (float(frequencyList[3][i]) > float(tops[1][j])):
				check = False
				for k in range (0, 5):
					if frequencyList[2][i] == tops[2][k]:
						check = True
				if check == False:
					tops[2][j] = frequencyList[2][i]
					tops[1][j] = frequencyList[3][i]

	for j in range(0,5):
		print tops[2][j],
		print tops[0][j]
		print 
		
	text2 = text
	for j in range (0,5):
		text2 = text2.replace(tops[2][j], tops[0][j].lower())	
	print (text2)

frequencyList = [[0]*26 for i in range(4)]
text = plainText(inputText())
print
print (text)
inp = raw_input("Continue? ")

analyzeFrequent(text)
inp = raw_input("Continue? ")
print 
topFive(text)
	
