from bs4 import BeautifulSoup as soup  
from urllib.request import urlopen as uReq  
  
# Request from the webpage  
myurl = "https://www.zapbuild.com/holidays"  


uClient  = uReq(myurl)  
page_html = uClient.read()  
uClient.close()

page_soup = soup(page_html, features="html.parser") 

containers = page_soup.find_all("div",{"class": "holiday_contant_oth"}) 
print(containers)
for item in containers:
	print("festival name:"+item.find("h4").text)
	print("description:"+item.find("p").text)
	print("date:"+item.find("span",{"class":"day_of_holiday"}).em.text+" "+item.find("span",{"class":"day_of_holiday"}).i.text)
	print("\n")

