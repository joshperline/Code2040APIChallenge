# @author Joshua Perline
# 2/14/2015 (Don't judge)

import json, requests, datetime, dateutil.parser

def registerAPI():
	"""My token is "shwxakN9aj" """
	data = {'email':'joshperline@berkeley.edu',
			'github': 'https://github.com/joshperline/Code2040APIChallenge'}
	print postRequest('register', data)

def stage1():
	""" Reverse a string """
	token = postRequest('getstring')
	
	reversed_string = token[::-1]

	data = {'token': 'shwxakN9aj', 'string': reversed_string}
	postRequest('validatestring', data)

def stage2():
	""" Needle in a haystack """
	token = postRequest('haystack')

	haystack = token['haystack']
	needle = token['needle']
	needle_index = None
	for i in xrange(0, len(haystack)):
		if haystack[i] == needle:
			needle_index = i
			break

	data = {'token': 'shwxakN9aj', 'needle': needle_index}
	postRequest('validateneedle', data)

def stage3():
	""" return an array containing only the strings 
	that do not start with that prefix. """
	token = postRequest('prefix')

	prefix = token['prefix']
	array = token['array']
	new_array = []
	for string in array:
		if not string[0:len(prefix)] == prefix:
			new_array.append(string)
	
	data = {'token': 'shwxakN9aj', 'array': new_array}
	postRequest('validateprefix', data)

def stage4():
	""" The dating game """
	token = postRequest('time')

	datestamp = token['datestamp']
	interval = token['interval']
	my_date = dateutil.parser.parse(datestamp) + datetime.timedelta(0,interval)
	my_date = my_date.isoformat()

	data = {'token': 'shwxakN9aj', 'datestamp': my_date}
	postRequest('validatetime', data)


def postRequest(url, data = {'token': 'shwxakN9aj'}):
	"""Helper function to decrease redundant code."""
	data_json = json.dumps(data)
	token = requests.post('http://challenge.code2040.org/api/' + url,
						  data=data_json)
	return token.json()['result']

# registerAPI()
# stage1()
# stage2()
# stage3()
# stage4()

