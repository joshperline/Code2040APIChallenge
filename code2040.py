import json
import requests
import dateutil.parser

def registerAPI():
	data = {'email':'joshperline@berkeley.edu', 'github': ''}
	data_json = json.dumps(data)
	payload = {'json_playload': data_json, 'apikey': 'YOUR_API_KEY_HERE'}
	r = requests.post('http://myserver/emoncms2/api/post', data=payload)

def stage1():
	""" Reverse a string """
	# Use "String"[::-1]


def stage2():
	""" Needle in a haystack """
	# TODO
	needle_index = None
	for i in xrange(0, len(haystack)):
		if haystack[i] == needle:
			needle_index = i
			break
	# Send needle_index

def stage3():
	""" return an array containing only the strings 
	that do not start with that prefix. """
	# TODO
	prefix = ""
	array = []
	new_array = []
	for string in array:
		if string[0:len(prefix)] == prefix:
			new_array.append(string)


def stage4():
	""" The dating game """
	# TODO
	datestamp = ""
	interval = 0
	my_date = dateutil.parser.parse(datestamp) + datetime.timedelta(0,interval)
	my_date = my_date.isoformat()







