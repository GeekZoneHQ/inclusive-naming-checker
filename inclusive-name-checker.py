

#This puts paths of files to be tested into a list
pathsStr = open("changed-files-paths.txt", "r").read().splitlines()




#This block opens non-inclusive-t1 containing our Tier 1 non-inclusive words to check for, puts it into a main list and closes the non-inclusive-t1 file
non_inclusive_file = open("non-inclusive-t1", "r")
non_inclusive_text = non_inclusive_file.read()
non_inclusive_lst = non_inclusive_text.splitlines()
non_inclusive_main_lst = non_inclusive_lst
non_inclusive_file.close()

#Same as previous block but for non-inclusive-t2 and then appending all Tier 2 words to the main list
non_inclusive_t2_file = open("non-inclusive-t2", "r")
non_inclusive_t2_text = non_inclusive_t2_file.read()
non_inclusive_t2_lst = non_inclusive_t2_text.splitlines()
non_inclusive_t2_file.close()

for i in non_inclusive_t2_lst:
	non_inclusive_main_lst.append(i)

#Same as above block but for non-inclusive-t3
non_inclusive_t3_file = open("non-inclusive-t3", "r")
non_inclusive_t3_text = non_inclusive_t3_file.read()
non_inclusive_t3_lst = non_inclusive_t3_text.splitlines()
non_inclusive_t3_file.close()

for i in non_inclusive_t3_lst:
	non_inclusive_main_lst.append(i)
#The previous 24 lines exist to create a list of all non-inclusive words to be tested taken from: non-inclusive-t1 non-inclusive-t2 and non-inclusive-t3



#opening file and searching for non-inclusive words, returning true or false and if false the column and location of the no no words

def namingCheck(file, non_inclusive):

	#initialising starting value for string search
	start = 0

	#Dictionary - Init sub dict
	subDict = {}


	#for each word in non_inclusive checks input file for instances of it
	for i in non_inclusive:

		#length of current test word
		wLen = len(i)

		file.seek(0,0)

		lNum = 1

		#Dictionary

		foundLst = []
		for line in file:

			#print("\n\n\n", line, "\n\n\n")

			start = 0

			lPos = 0

			while lPos != -1:

				#lPos contains index of noNoWord found
				lPos = line.find(i, start)

				#appends indexes of found instances of currently iterated word to foundLst
				foundLst.append('Row: ' + str(lNum) + " Column: " + str(lPos))
				

				#moves start point past detected word to avoid redetection
				start = lPos + wLen

			foundLst.pop()

			lNum += 1

		#test
		#print(foundLst)
		#test
		#print(str(lNum) + " " + i)
		#print(i)

		#This if else statement adds the current word and its positions (foundLst) to subDict as a key value pair or does nothing if no instances are found (foundLst = [])
		if foundLst != []:
			subDict.update({i:foundLst})
			print("********************************")
		else:
			print("--------------------------------")


	#output
	return subDict


#this section needs to iterate over pathsStr applying namingcheck() and updating dictionary if not empty

def feeder(paths, non_inclusive):
	mainDict = {}
	openFile = ""

	for path in paths:
		openFile = open(path, "r")

		#test
		#print("\n\n\n\n\n", path, "\n\n\n\n\n", openFile)

		subDict = namingCheck(openFile, non_inclusive)
		mainDict.update({path:subDict})

		#test
		#print(subDict)

		openFile.close()
	return mainDict




def testOutcome(mainDict):
	#causes test to fail by default
	testState = False
	for i in mainDict:
	#if instances of words found testState False else True
		if mainDict[i] != {}:
			return testState
		else:
			pass
	testState = True
	return testState






mainDict = feeder(pathsStr, non_inclusive_main_lst)

test = testOutcome(mainDict)

print(mainDict,"\n\nTest Outcome:", test)


#To Do:
	
	#If I open any file will it be read properly by the code?

	#Allow the code to take in a file given to it by something outside of it. Github action? Another piece of code within the action? Given by the 

	#Get openNCheck function to construct and output a dictionary