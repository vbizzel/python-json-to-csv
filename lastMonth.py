import requests    # module that makes http requests
import json # module for JavaScript Object Notation
import csv

last_month = requests.get('https://domain.com/rest/api/2/search?jql=project=IR%20and%20created%20%3E=%20startOfMonth(-1M)%20and%20created%20%3C=%20endOfMonth(-1M)', auth=('username', 'password'))

def lastMonth():
	
	with open('/Users/directory/Desktop/Python_OutPut/lastMonth.txt', 'w+') as fileOut:   # dumps the information into a text file on local machine
		fileOut.write(json.dumps(last_month.json(), indent = 4 ))  # prints the API JSON request informaton with formatting in python
		fileOut.close()

	return lastMonth

def list_info():   #function containing the search fields and appending them to the list infoIWant
	
	#Key | Summary | Affected Systems | Severity | Assingee | Date Created | Status 

	infoIWant = []   #list with empty parameters
	for x in last_month.json()['issues']:		
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

def lastMonthCSV(): # function that opens up a csv file to put the filtered data into

	with open('/Users/directory/Desktop/Python_OutPut/lastMonth.csv', 'w+') as csvFileOut:  #prints the information from list_info into a csv file
		wr = csv.writer(csvFileOut, quoting=csv.QUOTE_ALL)
		for row in list_info():
			wr.writerow([w.encode('utf-8') for w in row])
		csvFileOut.close()

	return lastMonthCSV

lastMonth()

print u'\n'.join([','.join(y) for y in list_info()]).encode('utf-8')

lastMonthCSV()
