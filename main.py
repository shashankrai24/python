#got the idea that this is a web scraping assignment from the libraries that were present in the document provided
#where we have to scrap information without any internet connection in order to not get noticed
import requests # insatlling required dependencies
from bs4 import BeautifulSoup
url="https://dfmye9ryu8rat.cloudfront.net/orionCipherFlow.txt"
r=requests.get(url)
soup=BeautifulSoup(r.text,'html')
with open("demo.txt", "w", encoding='utf-8') as file:
    file.write(str(soup.get_text()))
f = open("demo.txt", "r") # storing the content from a url into the file and saving it as mentioned in first part

# Now Decoding part

#we have to analyize the content from the url to decipher the message
print(soup.body)# gives content of the url which is a rearranged html piece of code with message inside all div
print(soup.get_text()) # printing the entire text content gives all the sentences in the message that has to be deciphered.
#considering important piece of information from printed text we find three mail id where we have to send the repo code and our resume
#the idea of mailing came from cc part mentioned considering the three mail ids with keyword like resume git hub repository link and mention of subject of mail as "information decoded"

#Another method can be to rearrange the html text correctly and use webbrowser library to get the view of this html text in a html
#that would give a perfect html page with proper styling with clear picture of message but since we cannot use this library as it is not present in laptop (relic)