import requests    # module that makes http requests
import json # module for JavaScript Object Notation
import csv

jan2015_current = requests.get('https://domain.com/rest/api/2/search?jql=project%20=%20IR%20AND%20created%20%3E=%202015-01-01%20AND%20created%20%3C=%20now()%20&maxResults=1000', auth=('username', 'password'))

def janToCurrent():
	
	with open('/Users/directory/Desktop/Python_OutPut/jan2015_current.txt', 'w+') as fileOut:   # dumps the information into a text file on local machine
		fileOut.write(json.dumps(jan2015_current.json(), indent = 4 ))  # prints the API JSON request informaton with formatting in python
		fileOut.close()

	return janToCurrent

def list_info():   #function containing the search fields and appending them to the list infoIWant
	
	#Key | Summary | Affected Systems | Severity | Assingee | Date Created | Status 

	infoIWant = []   #list with empty parameters
	for x in jan2015_current.json()['issues']:		
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
		tempInfo.append(x["fields"]["created"])           #Date created
		tempInfo.append(x["fields"]["status"]["name"])    #Status
		infoIWant.append(tempInfo)

	return infoIWant 

def janToCurrentCSV(): # function that opens up a csv file to put the filtered data into

	with open('/Users/directory/Desktop/Python_OutPut/jan2015_current.csv', 'w+') as csvFileOut:  #prints the information from list_info into a csv file
		wr = csv.writer(csvFileOut, quoting=csv.QUOTE_ALL)
		for row in list_info():
			wr.writerow([w.encode('utf-8') for w in row])
		csvFileOut.close()

	return janToCurrentCSV

janToCurrent()

print u'\n'.join([','.join(y) for y in list_info()]).encode('utf-8')

janToCurrentCSV()
