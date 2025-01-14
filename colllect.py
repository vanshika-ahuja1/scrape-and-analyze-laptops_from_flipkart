from bs4 import BeautifulSoup
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
di={'title':[],'actual_price':[],'dis':[],'after_dis_price':[],'link':[],'rating':[],'no_of_rating':[]}
i=1

for file in sorted(os.listdir('data')):  #it will sort the files from data folder
    try:

        print(f"data/{file}")
        if file.endswith(".html"):
            with open(f"data/{file}") as f:
                ht=f.read()
                f.close()
            soup=BeautifulSoup(ht,"html.parser")
            

            t=soup.find("div",class_="tUxRFH")
            l=t.find("a")
            link="https://www.flipkart.com"+l["href"]
            driver.get(link)
            page_source = driver.page_source
            soup=BeautifulSoup(page_source,"html.parser")

            #title finding
            t=soup.find("span",class_="VU-ZEz")
            title=t.get_text()
            

            #actual price
            ac=soup.find("div",class_="yRaY8j A6+E6v")
            acp=ac.get_text()[1:]
            #print(acp)

            #discount
            d=soup.find("div",class_="UkUFwK WW8yVX")
            dp=d.get_text()
            #print(dp)
            
            #price after discount
            ad=soup.find("div",class_="Nx9bqj CxhGGd")
            adp=ad.get_text()[1:]
            #print(adp)

            #rating
            rating=soup.find('div',class_='XQDdHH')
            r=rating.get_text()

            #no of rating
            rr=soup.find(class_="Wphh3N")
            nrr=rr.find("span").get_text()

            di["title"].append(title)
            di["actual_price"].append(acp)
            di["dis"].append(dp)
            di['after_dis_price'].append(adp)
            di["link"].append(link)
            di['rating'].append(r)
            di['no_of_rating'].append(nrr)
            break
    except Exception as e:
        print("something went wrong",e)



#print(d)

df=pd.DataFrame(data=di)
df.to_csv('_laptop_data.csv')

        
