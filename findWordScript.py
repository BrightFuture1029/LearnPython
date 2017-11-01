from sys import argv
argumentLength = len(argv)

if(argumentLength != 4):
	print 'Invalid number of arguments'
	print 'Usage : scriptFile,inFileName,outFileName,keyWord '
	exit()
	
scriptFile,inFileName,outFileName,keyWord = argv
print ' InFile name: ', inFileName, ' and  outFile ' , outFileName 
foundVariables = []
lineNumber = 0
lineCount = 0
linePosition = 0;
startSpacePosition = 0
endSpacePosition = 0

with open(inFileName) as inFile:
	for line in inFile:
		linePosition = line.find(keyWord)
		if(linePosition == -1):
			lineCount += 1
			continue
		#
		#print lineCount,'.......'		
		while linePosition != -1 :
				
				
				#startSpacePosition = line.rfind(' ',0,linePosition) + 1
				startSpacePosition = max(line.rfind('(',0,linePosition) + 1,line.rfind(' ',0,linePosition) + 1)
				endSpacePosition = min(line.find(')',linePosition), (line + ' ').find(' ',linePosition))
				#print lineCount,':',linePosition , ',',startSpacePosition,',',endSpacePosition
				var = line[startSpacePosition:endSpacePosition]
				#print var,'..'
				foundVariables.append(var)
				#print line[0:linePosition]
				
				linePosition = line.find(keyWord,linePosition+1)
		#		
		
		lineCount += 1
		linePosition = 0
		#break
		
print 'list count :',len(foundVariables)
foundVariables = list(set(foundVariables))

replacementDic = {}
for	var in foundVariables:
	replacementDic[var] = '_' + var.replace(keyWord,'')	

print replacementDic	

with open(inFileName) as inFile , open(outFileName,'w') as outFile:
	for line in inFile:
		for src, target in replacementDic.iteritems():
			line = line.replace(src, target)
        
		outFile.write(line)
	

with open(outFileName,'a') as outFile:
	outFile.write('\n')
	declarations = []
	for	var in foundVariables:
		dec = 'double _'  + var.replace(keyWord,'') + ';\n'
		#declarations.append(dec)
		outFile.write(dec)
		#print dec
	
	outFile.write('//////////////////////////////////////////////\n')

	
	initializations  = []	
	for	var in foundVariables:
		dec = '_'  + var.replace(keyWord,'') + ' = 0;\n'
		initializations.append(dec)
		outFile.write(dec)
		#print dec
		
	outFile.write('//////////////////////////////////////////////\n')	
	
	assignments = []	
	for	var in foundVariables:
		dec = '_' + var.replace(keyWord,'') + ' = ' + var + ';\n'
		assignments.append(dec)
		outFile.write(dec)
		#print dec
