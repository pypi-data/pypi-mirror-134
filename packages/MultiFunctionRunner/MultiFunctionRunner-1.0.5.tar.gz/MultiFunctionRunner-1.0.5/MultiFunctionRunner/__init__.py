def multiFunctionRun2(functionsListToRun, argumentsToPass=None):
	if (argumentsToPass == None):
		for func in functionsListToRun:
			func()
	else:
		for _ in range(len(functionsListToRun)):
			if type(argumentsToPass[_]) == list:
				functionsListToRun[_](*argumentsToPass[_])
			else:
				functionsListToRun[_](argumentsToPass[_])