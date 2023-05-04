import requests
import os
from bs4 import BeautifulSoup
url ="https://en.wikipedia.org/wiki/Bhagavad_Gita"

#first will send the request to the url
response = requests.get(url)
webPageContent = response.content

#now i will create  a soup object and will parse the content
soup = BeautifulSoup(webPageContent,'html.parser')
#then will find all the sections i am using the a tag

sections = soup.find_all('a')

# we shall now create a directory to store all the text file of the divided sections of the web page using os module

directoryName = 'wikipideaSections'

if not os.path.exists(directoryName):
    os.makedirs(directoryName)

#now using for loop i shall travel through all the sections and store them in text files

for section in  sections:
    section_title = section.text.strip()
    section_content=section.find_next('div',{'class': 'mw-parser-output'}).text.strip()

    fileName = f"{directoryName}/{section_title}.text"
    with open(fileName,'w',encoding='utf-8') as file:
        file.write(section_content)
    print(f"Created file{fileName}")
