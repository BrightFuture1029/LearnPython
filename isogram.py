from sys import argv

scriptFile,word = argv

print "Finding if ",word," is isogram"

arrayChar = list(word)
print "Length is " + str(len(arrayChar))

isIsogram = True

for	a in arrayChar:
	if(arrayChar.count(a)> 1):
		isIsogram = False
	

	
if isIsogram:
	print word," is isogram"
else:
	print word," is not isogram"

