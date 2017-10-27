from sys import argv

scriptFile,yearInt = argv
yearInt = int(yearInt)

print "Finding if ",yearInt," is leap year."

if yearInt%4 == 0:
	print yearInt, " is leap year."
else:
	print yearInt, " is not leap year."
	
