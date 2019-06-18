# Importing Useful packages
import matplotlib.pyplot as plt
import pandas as pd
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
# Initializing a CSV file to store Scraped Data
filename= "products.csv"
f= open(filename, "w")
headers = "product, Price\n"
f.write(headers)
#Initializing lists for product and price
my_prod=[]
my_price=[]
#looping over 10 pages of souq.com
for i in range(1,10):
 my_url = 'https://uae.souq.com/ae-en/mobile-phone/l'
 # opening up connection, grabbing the page
 uClient=uReq(my_url)
 page_html=uClient.read()
 uClient.close()
 #html parsing
 page_soup=soup(page_html, "html.parser")
 page_soup.h1
 page_soup.body.span
 page_soup.body
 #Grab each product
 containers=page_soup.findAll('div',{"class":"column column-block block-list-large single-item"})
 length= len(containers)
  

#  looping over each container in a page
 for j in range(length):
      
              product=containers[j].find("div",{"class":"col col-info item-content"}).a["title"]
              
              price=containers[j].find("h3",{"class":"itemPrice"}).text.strip()
              #replacing , in price
              price=price.replace(",","")
              #replacing AED in price
              price=price.replace('AED','')
              #Changing price from text to float to be able to do analytics
              price=float(price)
               
              print("product: " + str(product))
              print("price: "+ str(price))
              #storing price and products in list
              my_prod.append(product)
              my_price.append(price)
              #storing price and prodict values in csv file
              f.write(product.replace(",","|") + "," + str(price) + "\n")
              print(my_prod)
              print(my_price)


#Storing product and price in a dataframe
my_portfolio_df=pd.DataFrame({'Mobiles': my_prod, 'Price': my_price})
print(my_portfolio_df)
#calculating mean of prices 
Mean_price=my_portfolio_df['Price'].mean()
print(Mean_price)
#calculating max product price
Max_Price=my_portfolio_df['Price'].max()
#calculating max product price
Min_Price=my_portfolio_df['Price'].min()
print(Max_Price)
print(Min_Price)
#creating dataframe for mobiles less than mean value
Less_Than_mean_price=my_portfolio_df[my_portfolio_df.Price<= Mean_price]
#creating dataframe for mobiles greater than mean value
Greater_than_equal_Mean_price=my_portfolio_df[my_portfolio_df.Price>= Mean_price]
#boxplot for all mobile prices
my_portfolio_df.boxplot()

#boxplot for less than mean price mobiles
Less_Than_mean_price.boxplot()

#boxplot for greater than mean price mobiles
Greater_than_equal_Mean_price.boxplot()

#closing csv file
f.close()



