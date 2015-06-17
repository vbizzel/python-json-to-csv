import requests    # module that makes http requests
import json # module for JavaScript Object Notation
import csv

last_week = requests.get('https://domain.com/rest/api/2/search?jql=project=IR%20and%20created%20%3E=%20startOfWeek(-1w)%20and%20created%20%3C=%20endOfWeek(-1w)', auth=('username', 'password'))


def lastWeek():
	
	with open('/Users/directory/Desktop/Python_OutPut/lastWeek.txt', 'w+') as fileOut:   # dumps the information into a text file on local machine
		fileOut.write(json.dumps(last_week.json(), indent = 4 ))  # prints the API JSON request informaton with formatting in python
		fileOut.close()

	return lastWeek

def list_info():   #function containing the search fields and appending them to the list infoIWant
	
	#Key | Summary | Affected Systems | Severity | Assingee | Date Created | Status 

	infoIWant = []   #list with empty parameters
	for x in last_week.json()['issues']:		
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

def lastWeekCSV(): # function that opens up a csv file to put the filtered data into

	with open('/Users/directory/Desktop/Python_OutPut/lastWeek.csv', 'w+') as csvFileOut:  #prints the information from list_info into a csv file
		wr = csv.writer(csvFileOut, quoting=csv.QUOTE_ALL)
		for row in list_info():
			wr.writerow([w.encode('utf-8') for w in row])
		csvFileOut.close()

	return lastWeekCSV

lastWeek()

print u'\n'.join([','.join(y) for y in list_info()]).encode('utf-8')

lastWeekCSV()
