import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

mypage=webdriver.Chrome()
mypage.get("https://shoplink.my/product-category/cameras-drones/?v=62d58cbe68e1")
se=WebDriverWait(mypage,10).until(EC.visibility_of_element_located((By.XPATH,"//ul[@class='products columns-3']/li")))
elems=mypage.find_elements(By.XPATH,"//ul[@class='products columns-3']/li")
for elem in elems:
   # print (elem.find_element()
   # indec=elems.index(elem)+1
    title=elem.find_element(By.XPATH,'.//h2/a').text
    if (title.find("Drone")!=-1):
        print(title)
        price=elem.find_element(By.XPATH,'.//span/ins/span/bdi').text
        print(price)
    #price=mypage.find_element(By.XPATH,f"//ul[@class='products columns-3']/li[{indec}]/span/del/span/bdi")
    #print(price.text)
