import requests
from bs4 import BeautifulSoup
url='https://en.wikipedia.org/wiki/List_of_Eurovision_Song_Contest_winners'

import pandas as pd 

page= requests.get(url)

soup=BeautifulSoup(page.content,"html.parser")
Results=soup.find(id="ResultsContainer")
print(Results.prettify)

jobelements=Results.find_all("div",class_="card-content")
data={}

for job in jobelements:
    title=job.find("h2",class_="title")

    location=job.find("p",class_="location")

    data[title.text.strip()]=location.text.strip()

    df= pd.DataFrame(data=data,index=[0])

    print(df.T)

   # saving the dataframe
df.to_csv('file1.csv')
