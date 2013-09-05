varA = 5
varB = 'sweet'
if isinstance(varA, basestring) or isinstance(varB, basestring):
    print('string involved')
elif int(varA) > int(varB):
	print("bigger")
elif int(varA) == int(varB):
	print("equal")
elif int(varA) < int(varB):
	print("smaller")
