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


base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
req = requests.get(base_url)
soup = BeautifulSoup(req.text, 'html.parser')

wd = soup.find_all('p')
for each in wd:
	elt = each.text
	total = re.findall('\\bstudent\\b', elt)
	print (total)
	elt = re.sub('\\bstudent\\b', 'AMAZING student', elt)
	print (elt)



#swap w pic after   .html is the webpage (chapter 7)



#theres a lot of ways to replace findall or regex

link = soup.find_all('img')
for b in link:
	href = b["src"]
	if href == 'https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg':
		b['src'] = 'https://s-media-cache-ak0.pinimg.com/avatars/jaclynrudolf_1330556638_140.jpg'
		

for b in link:
	href = b['src']
	if not href.startswith("https:"):
		print ('pre', b['src'])
		b['src'] = 'https://raw.githubusercontent.com/cvanlent/SI206/master/HW3-StudentCopy/media/logo.png'
		print (b['src'])

ending = str(soup)

f= open('project.html', 'w')
f.write(ending)
f.close()

#can you do the same thing for students?

