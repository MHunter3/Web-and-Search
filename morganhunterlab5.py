#CIS 117 Python Programming Lab #5
#Web and Search
#Application to put a decision on business opertations (bizop) table
#Compute the number of instances of each topic of interest
#Print a simple and complete report of instances

import datetime
import re
from urllib.request import urlopen
from urllib.error import URLError
from html.parser import HTMLParser


def report_sum(topics):
	"""counts the number of occurrences for each word in url"""
	response = urlopen("http://www.nasonline.org")  # open url
	html = response.read()
	content = html.decode('utf-8').lower() #convert html to string using 'utf-8'

	for topic in topics:
		num = content.count(topic)
		print('{} appears {} times. ' .format(topic, num))

#begin/create list of topics
topics = ('research', 'climate', 'evolution', 'cultural', 'leadership',
		'nation', 'physical', 'science', 'biological', 'human gene', 'history',
		'membership', 'events', 'rewards', 'technology', 'policy', 'lecture series',
		'reports', 'lab')
#end list of topics

#validate error of opening url
try:
	print()
except HTTPError:



#check matched words/ignore case-sensitivity
pattern = re.compile(r'.even', re.IGNORECASE)

#iterate through list and find pattern
for topic in topics:
    if re.match(pattern, topic):
        print(f'The {topic} matches')

#print date of program run
print("Today's date is " + str(datetime.date.today()))

report_sum(topics)

""""commented out code run
Today's date is 2020-07-27
research appears 10 times. 
climate appears 4 times. 
evolution appears 4 times. 
cultural appears 8 times. 
leadership appears 5 times. 
nation appears 38 times. 
physical appears 1 times. 
science appears 59 times. 
biological appears 1 times. 
human gene appears 3 times. 
history appears 4 times. 
membership appears 11 times. 
events appears 10 times. 
rewards appears 0 times. 
technology appears 4 times. 
policy appears 10 times. 
lecture series appears 2 times. 
reports appears 9 times. 
lab appears 13 times. 

Process finished with exit code 0 """
