from sys import argv

scriptFile,sequence = argv

print 'In sequence ' , sequence

replacements = {
'G':'C',
'C':'G',
'T':'A',
'A':'U'
}

print 'Replacements to be used ',replacements

sequenceArray = list(sequence.upper())
sequenceNewArray = []

for	a in sequenceArray:
	if(replacements.has_key(a)):
		sequenceNewArray.append(replacements.get(a))
	

print ''.join(sequenceNewArray)