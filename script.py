import requests    # module that makes http requests
import json # module for JavaScript Object Notation
import csv
#from pprint import pprint # is the module to format print statements more clearly

r = requests.get('https://domain.com/rest/api/2/search?jql=project=IR&maxResults=150', auth=('username', 'password'))    #access to the url, needs username and password to JIRA

#need to put in a range function and error check while if/else to verify url exists
r.status_code    #status code refers to whether I have access, or if that link exists in the API

################################################################################################

def open_text_file():
	
	with open('/Users/Home/example_1.txt', 'w+') as fileOut:   # dumps the information into a text file on local machine
		fileOut.write(json.dumps(r.json(), indent = 4 ))  # prints the API JSON request informaton with formatting in python
		fileOut.close()

	return open_text_file
	
################################################################################################
	
def list_info():   #function containing the search fields and appending them to the list infoIWant
	
	#Key | Summary | Affected Systems | Severity | Assingee | Date Created | Status 

	infoIWant = []   #list with empty parameters
	for x in r.json()['issues']:		
		tempInfo = []
		tempInfo.append(x["key"]) #key
		tempInfo.append(x["fields"]["summary"])    #summary		
		tempInfo.append(x["fields"]["customfield_10201"][0]["value"]) #Affected Systems
		tempInfo.append(x["fields"]["customfield_10204"]["value"])   #Severity		
		try:
			#safeget(example_dict, 'key1', 'key2')
			tempInfo.append(x["fields"]["assignee"]["displayName"])  # Assignee
		except TypeError as e:
			tempInfo.append('None')
		tempInfo.append(x["fields"]["created"])
		tempInfo.append(x["fields"]["status"]["name"])    #Status
		infoIWant.append(tempInfo)

	# if x in tempInfo['issues'][0]['fields']['assignee']['displayName'] is not None:
	# 	return infoIWant
	# else:
	# 	print null

	return infoIWant 

def safeget(r, *keys):
    for key in keys:
        try:
            r.json = r.json[key]
        except KeyError:
            return None
    return r
################################################################################################

#listInfoIWant = list_info()	#function list_info becomes list, listInfoIWant 
  #prints it to screen for verification(testing purposes only)

################################################################################################

def open_csv_file(): # function that opens up a csv file to put the filtered data into

	with open('/Users/Home/example.csv', 'w+') as csvFileOut:  #prints the information from list_info into a csv file
		wr = csv.writer(csvFileOut, quoting=csv.QUOTE_ALL)
		for row in list_info():
			wr.writerow([w.encode('utf-8') for w in row])
		csvFileOut.close()

	return open_csv_file

open_text_file()

print u'\n'.join([','.join(y) for y in list_info()]).encode('utf-8')

open_csv_file()

################################################################################################
