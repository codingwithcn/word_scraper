# type the following command in command line
#py -m pip install bs4
#py -m pip install beautifulsoup4
#py -m pip install requests
# now you are ready to start coding
from bs4.element import PageElement
import requests
from bs4 import BeautifulSoup
import time
#code to get synonyms
def synonyms(word):
  worded = []
  skipped= []
  amount = []
  URL = 'https://www.thesaurus.com/browse/'+word+"?s=t" # saves the URL
  print(URL) # this is incase you want to see what word it is searching for
  page = requests.get(URL) # saves the page contents
  soup = BeautifulSoup(page.content,'html.parser') 
  result = soup.find(class_="css-11nwwws e1gu66k41")
  n = result.text # Gets the amount of pages used for the word
  nws = n.split('S') 
  nwn = nws[1].split('N')
  amount.append(nwn[0])
  num = len(amount)
  lonwn = len(nwn[0])
  more = []
  repeat = False # Checks if a number aka string is repeated more than once.
  for i in nwn[0]:
    trial = nwn[0]
    total = len(nwn[0])
    if i not in more:
      more.append(i)
    elif i == trial[total-1:]:
      repeat = False
      break
    else:
      repeat =True
      break
  if repeat == True:
    la = lonwn-2
    gnwn = nwn[0]
    number = int(gnwn[la:])
  else:
    la = lonwn-1
    gnwn = nwn[0]
    number = int(gnwn[la:])
  
  while number != 0:
    if not ConnectionError == True:
        try:
            definition = soup.find_all("a",class_="css-1wndipq eh475bn1")
            for define in definition:
                worded.append(define.text)

        except AttributeError:
            URL ='https://www.thesaurus.com/browse/'+word+'/'+str(number)
            page= requests.get(URL)
            soup = BeautifulSoup(page.content,'html.parser')
            try:
                definition = soup.find_all("a",class_="css-1wndipq eh475bn1")
                for define in definition:
                    worded.append(define.text)
            except AttributeError:
                pass
    else:
        pass
    number-=1
    print(number)
    URL ='https://www.thesaurus.com/browse/'+word+'/'+str(number)
    if number <=1:
        break
  return worded
#code for dictionary scraping.... Gets the definition of word
def define(word):
  worded = []
  while True:
    URL = 'https://www.dictionary.com/browse/'+word+"?s=t"
    if not ConnectionError == True:
      page= requests.get(URL)
      soup = BeautifulSoup(page.content,'html.parser')
      result = soup.find(class_="css-1o58fj8 e1hk9ate4")
      try:
        definition = result.find_all("span",class_="one-click-content css-17f75g0 e1q3nk1v4")
        for define in definition:
          worded.append(define.text)
      except AttributeError:
        URL ='https://www.dictionary.com/browse/'+word
        page= requests.get(URL)
        soup = BeautifulSoup(page.content,'html.parser')
        result = soup.find(class_="css-1o58fj8 e1hk9ate4")
        try:
          definition = result.find_all("span",class_="one-click-content css-17f75g0 e1q3nk1v4")
          for define in definition:
            worded.append(define.text)
        except AttributeError:
          worded.append("continued")
    else:
      break
    break
  return worded   
if __name__ == "__main__":
    word = synonyms('food')
    print(word)
    words = define('food')
    print(words)
