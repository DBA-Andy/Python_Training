# LinkedIn Learning Python course by Joe Marini
# Example file for parsing and processing JSON
#

import urllib.request
import json


# Open the URL and read the data
web_url = urllib.request.urlopen("http://uselessfacts.jsph.pl/api/v2/facts/random")
print ("Result code:", web_url.getcode())

# Read the JSON data from the source
data = web_url.read()
theJSON = json.loads(data)

# Print the content of the 'text' field
print(theJSON["text"])
