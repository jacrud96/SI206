# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

import requests 
from bs4 import BeautifulSoup 
import re
import urllib.request, urllib.parse, urllib.error
base_url = 'https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions'
html = urllib.request.urlopen(base_url).read() 
soup = BeautifulSoup(html, 'html.parser') 

#need to convert the object to string
txt = soup.prettify() 
for word in txt:
	find_string = soup.body.findAll(text=re.compile('student')
print(str.replace('student', 'AMAZING student'))


#for student in soup.find_all(class_='body-inside2'): 


#swap w pic after   .html is the webpage (chapter 7)



#theres a lot of ways to replace findall or regex

link = soup.find_all ('img')
for b in link:
href = b["src"]
if (href) == 'https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg':
print (href)
b["src"] = 'me.png'
print (b["src"])

#can you do the same thing for students?

webpage = open('file.html', 'w')
webpage.writetxt 