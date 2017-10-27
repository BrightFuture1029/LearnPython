from sys import argv

scriptFile,sentence  = argv
print 'Your sentence is ',sentence
sentenceArray = list(sentence.lower())

isPanGram = True
for	i in range(ord('a'),ord('z')+1):
	if(sentenceArray.count(chr(i)) == 0):
		isPanGram = False
	

if(isPanGram):
	print sentence, ' is Pangram'
else:
	print sentence, ' is not Pangram'

