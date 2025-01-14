from selenium import webdriver
from selenium.webdriver.common.by import By
import time

file=0
driver=webdriver.Chrome()
query="laptop"
for i in range(1,15):
    driver.get(f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}")
    elems=driver.find_elements(By.CLASS_NAME,"tUxRFH")
    print("item found",len(elems))
    for elem in elems: 
        d=elem.get_attribute("outerHTML")
        if file<=9:
            z=f"data/{query}00{file}.html"
        else:
            z=f"data/{query}{file}.html"

        with open(z,"w",encoding="utf-8") as f:
            f.write(d)
           
        file+=1
    time.sleep(2)
driver.close() 