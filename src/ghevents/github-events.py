#!/usr/bin/env python3

import os
import json
import requests

GHUSER  = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'
print(GHUSER)
print(url)

def retrieve_events(url):
	"""Retrieve GitHub event data from the given URL."""
	json_text = requests.get(url).text 
	events = json.loads(json_text)
	return events 

def print_events(events,n=5):
	"""Print the type and repo name for the first n events."""
	for i in events[:n]:
		event = i['type'] + ' :: ' + i['repo']['name']
		print(event)
	

def main():
	"""Retrieve and print GitHub event information."""
	print(GHUSER)
	print(url)
	events=	retrieve_events(url)
	print_events(events)




if __name__ == "__main__":
    main()
