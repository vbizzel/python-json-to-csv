import requests    # module that makes http requests
import json # module for JavaScript Object Notation
import csv

# this http request to JIRA will get the IR and by the date it was created. This one fetches all IR's created in the last 7 days.
this_week = requests.get('https://work.corp.dyndns.com/rest/api/2/search?jql=project=IR%20and%20created%20%3E=%20startOfDay(-7d)', auth=('jvandenbussche', 'o7rLiWSAO0sIYFsd1bpfEI77A'))    #access to the url, needs username and password to JIRA

this_week = requests.get('https://work.corp.dyndns.com/rest/api/2/search?jql=project=IR%20and%20created%20%3E=%20startOfDay(-7d)', auth=('jvandenbussche', 'o7rLiWSAO0sIYFsd1bpfEI77A'))

last_week = requests.get('https://work.corp.dyndns.com/rest/api/2/search?jql=project=IR%20and%20created%20%3E=%20startOfDay(-7d)', auth=('jvandenbussche', 'o7rLiWSAO0sIYFsd1bpfEI77A'))

this_month = requests.get('https://work.corp.dyndns.com/rest/api/2/search?jql=project=IR%20and%20created%20%3E=%20startOfDay(-7d)', auth=('jvandenbussche', 'o7rLiWSAO0sIYFsd1bpfEI77A'))

last_month = requests.get('https://work.corp.dyndns.com/rest/api/2/search?jql=project=IR%20and%20created%20%3E=%20startOfDay(-7d)', auth=('jvandenbussche', 'o7rLiWSAO0sIYFsd1bpfEI77A'))

jan2015_current = requests.get('https://work.corp.dyndns.com/rest/api/2/search?jql=project=IR%20and%20created%20%3E=%20startOfDay(-7d)', auth=('jvandenbussche', 'o7rLiWSAO0sIYFsd1bpfEI77A'))

july2014_dec2014 = requests.get('https://work.corp.dyndns.com/rest/api/2/search?jql=project=IR%20and%20created%20%3E=%20startOfDay(-7d)', auth=('jvandenbussche', 'o7rLiWSAO0sIYFsd1bpfEI77A'))



#need to put in a range function and error check while if/else to verify url exists
#current_week.status_code    #status code refers to whether I have access, or if that link exists in the API

################################################################################################

def thisWeek():
	
	with open('/Users/jvandenbussche/thisWeek.txt', 'w+') as fileOut:   # dumps the information into a text file on local machine
		fileOut.write(json.dumps(this_week.json(), indent = 4 ))  # prints the API JSON request informaton with formatting in python
		fileOut.close()

	return thisWeek

def lastWeek():
	
	with open('/Users/jvandenbussche/lastWeek.txt', 'w+') as fileOut:   # dumps the information into a text file on local machine
		fileOut.write(json.dumps(last_week.json(), indent = 4 ))  # prints the API JSON request informaton with formatting in python
		fileOut.close()

	return lastWeek

def thisMonth():
	
	with open('/Users/jvandenbussche/thisMonth.txt', 'w+') as fileOut:   # dumps the information into a text file on local machine
		fileOut.write(json.dumps(this_Month.json(), indent = 4 ))  # prints the API JSON request informaton with formatting in python
		fileOut.close()

	return thisMonth

def lastMonth():
	
	with open('/Users/jvandenbussche/lastMonth.txt', 'w+') as fileOut:   # dumps the information into a text file on local machine
		fileOut.write(json.dumps(last_month.json(), indent = 4 ))  # prints the API JSON request informaton with formatting in python
		fileOut.close()

	return lastMonth

def janToCurrent():
	
	with open('/Users/jvandenbussche/jan2015_current.txt', 'w+') as fileOut:   # dumps the information into a text file on local machine
		fileOut.write(json.dumps(jan2015_current.json(), indent = 4 ))  # prints the API JSON request informaton with formatting in python
		fileOut.close()

	return janToCurrent

def julyToDec():
	
	with open('/Users/jvandenbussche/july2014_dec2014.txt', 'w+') as fileOut:   # dumps the information into a text file on local machine
		fileOut.write(json.dumps(july2014_dec2014.json(), indent = 4 ))  # prints the API JSON request informaton with formatting in python
		fileOut.close()

	return julyToDec
	
################################################################################################
	
def list_info():   #function containing the search fields and appending them to the list infoIWant
	
	#Key | Summary | Affected Systems | Severity | Assingee | Date Created | Status 

	infoIWant = []   #list with empty parameters
	for x in this_week.json()['issues']:		
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

	# if x in tempInfo['issues'][0]['fields']['assignee']['displayName'] is not None:
	# 	return infoIWant
	# else:
	# 	print null

	return infoIWant 

# def safeget(r, *keys):
#     for key in keys:
#         try:
#             r.json = r.json[key]
#         except KeyError:
#             return None
#     return r
################################################################################################

#listInfoIWant = list_info()	#function list_info becomes list, listInfoIWant 
  #prints it to screen for verification(testing purposes only)

################################################################################################

def thisWeekCSV(): # function that opens up a csv file to put the filtered data into

	with open('/Users/jvandenbussche/thisWeek.csv', 'w+') as csvFileOut:  #prints the information from list_info into a csv file
		wr = csv.writer(csvFileOut, quoting=csv.QUOTE_ALL)
		for row in list_info():
			wr.writerow([w.encode('utf-8') for w in row])
		csvFileOut.close()

	return thisWeekCSV

def lastWeekCSV(): # function that opens up a csv file to put the filtered data into

	with open('/Users/jvandenbussche/lastWeek.csv', 'w+') as csvFileOut:  #prints the information from list_info into a csv file
		wr = csv.writer(csvFileOut, quoting=csv.QUOTE_ALL)
		for row in list_info():
			wr.writerow([w.encode('utf-8') for w in row])
		csvFileOut.close()

	return lastWeekCSV

def thisMonthCSV(): # function that opens up a csv file to put the filtered data into

	with open('/Users/jvandenbussche/thisMonth.csv', 'w+') as csvFileOut:  #prints the information from list_info into a csv file
		wr = csv.writer(csvFileOut, quoting=csv.QUOTE_ALL)
		for row in list_info():
			wr.writerow([w.encode('utf-8') for w in row])
		csvFileOut.close()

	return thisMonthCSV

def lastMonthCSV(): # function that opens up a csv file to put the filtered data into

	with open('/Users/jvandenbussche/lastMonth.csv', 'w+') as csvFileOut:  #prints the information from list_info into a csv file
		wr = csv.writer(csvFileOut, quoting=csv.QUOTE_ALL)
		for row in list_info():
			wr.writerow([w.encode('utf-8') for w in row])
		csvFileOut.close()

	return lastMonthCSV

def janToCurrentCSV(): # function that opens up a csv file to put the filtered data into

	with open('/Users/jvandenbussche/jan2015_current.csv', 'w+') as csvFileOut:  #prints the information from list_info into a csv file
		wr = csv.writer(csvFileOut, quoting=csv.QUOTE_ALL)
		for row in list_info():
			wr.writerow([w.encode('utf-8') for w in row])
		csvFileOut.close()

	return janToCurrentCSV

def julyToDecCSV(): # function that opens up a csv file to put the filtered data into

	with open('/Users/jvandenbussche/july2014_dec2014.csv', 'w+') as csvFileOut:  #prints the information from list_info into a csv file
		wr = csv.writer(csvFileOut, quoting=csv.QUOTE_ALL)
		for row in list_info():
			wr.writerow([w.encode('utf-8') for w in row])
		csvFileOut.close()

	return julyToDecCSV




thisWeek()

print u'\n'.join([','.join(y) for y in list_info()]).encode('utf-8')

thisWeekCSV()

################################################################################################
