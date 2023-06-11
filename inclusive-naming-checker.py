#required inputs:
	#file paths for new/changed files in form: changed-files-paths.txt
	#non-inclusive language in the form: non-inclusive-t1
	#									 non-inclusive-t2
	#									 non-inclusive-t3
	#copy of main repo to find files in

#This puts paths of files to be tested into a list adding the prefix "root/repo"
pathsLst = open("changed-files-paths.txt", "r").read().splitlines()
index = 0
for path in pathsLst:
	pathsLst[index] = "root/repo" + path
	index += 1
del index

#read replacement words into dictionary


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

	#set of found words
	foundSet = {}


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

		#This if else statement adds the current word and its positions (foundLst) to subDict as a key value pair or does nothing if no instances are found (foundLst = [])
		if foundLst != []:
			subDict.update({i:foundLst})
			foundSet.add(i)
		else:
			pass


	#output
	return subDict, foundSet


#this section needs to iterate over pathsLst applying namingcheck() and updating dictionary if not empty

def feeder(paths, non_inclusive):
	mainDict = {}
	openFile = ""
	foundSet_main = {}

	for path in paths:
		openFile = open(path, "r")

		#test
		#print("\n\n\n\n\n", path, "\n\n\n\n\n", openFile)

		ncOut = namingCheck(openFile, non_inclusive)

		foundSet_main.union(ncOut[1])

		subDict = ncOut[0]
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


def printer(testState, mainDict, foundSet_main):
    #with open("/home/r/Documents/geek.zone_coding/projects/INC-docker-action/Printer-test/inclusive-alternatives-oneline", "r") as data:
    #    altDict = ast.literal_eval(data.read())
    #data.close()
    altFile = open("inclusive-alternatives", "r")
    altDict = eval(altFile.read())
    altFile.close()


    results = open("results.md", "a")

    results.write("<h1>inclusive-naming-checker test results</h1>\n\n\n\n\n")
    if testState == True:
    	results.write("Outcome:  **Pass**\n\n\n")
    else:
    	results.write("Outcome:  **Fail**\n\n\n")

    results.write("<h2>Words found:</h2>\n\n\n")

    for word in foundSet_main:
    	results.write("**" + word + "**  -  consider replacing with:  " + altDict[word] + "\n\n")

    results.write("\n\n\n<h2>Files Checked:</h2>\n\n\n")

    #these loops write down the each file path along with non-inclusive language found and
    #the rows and columns it was found on
    for i in mainDict:
    	results.write("<h3>" + i + "</h3>\n\n")
    	for j in mainDict[i]:
            results.write("**" + j + "**\n\n")
            loop = 0
    		#loop over found positions in sub dictionaries
            for k in mainDict[i][j]:
                if loop%10 == 0:
                    results.write(k + "\n\n")
                else:
                    results.write(k + "  ")
            results.write("\n\n")
    results.close()











mainDict = feeder(pathsLst, non_inclusive_main_lst)

test = testOutcome(mainDict)

printer(testState, mainDict, foundSet_main)

print(mainDict,"\n\nTest Outcome:", test)




#To Do:
	
	#If I open any file will it be read properly by the code?

	#Allow the code to take in a file given to it by something outside of it. Github action? Another piece of code within the action? Given by the 

	#Output: Pass/Fail, Words found and alternatives, Files > Words > Where | All in markup format