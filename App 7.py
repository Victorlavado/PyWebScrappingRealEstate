#!/usr/bin/env python
# coding: utf-8

# In[45]:


import requests
from bs4 import BeautifulSoup
# Import requests and BeautifulSoup libraries to grab data from the website

r = requests.get("https://www.realestate.com/rock-springs-wy--homes?view=list")
# Get the source code from Real Estate website
# The realestate data comes from Rock Springs in Wyoming
c = r.content
# Store the source code into c variable


soup = BeautifulSoup(c, "html.parser")
# Use BeautfilSoup to structure html code and store into soup variable

all = soup.find_all("div",{"class":"PropertyTableData__row"})
# Store the div tag concerning the data for the list of properties
# From this div tag you can grab data like price, area...and so on

page_num = soup.find("div",{"class":"Paginator__content"}).text
# Extract the number of pages that result from looking properties
# In Rock Spring (Wyoming) at realestate.com


# Let´s create a list of dictonaries with the data that we want to grab:
# Address, City, Price, Bedrooms, Bathrooms, Area and Lot Size

l = []
# Create an empty list that will be stored into l variable
base_url = "https://www.realestate.com/rock-springs-wy--homes?view=list&p="
# Url that links to page number 1 of properties in Rock Springs
# By adding numbers at the end of the string you navitage to different pages
for page in range(1,int(page_num[-1])+1,1):
# For loop to iterate through the pages when looking for properties
# page variable acquires values from 1 to the end of the range
    print(base_url+str(page))
    # Print the url after the number of the page is added at the end
    # of base_url
    r = requests.get(base_url+str(page))
    c = r.content
    soup = BeautifulSoup(c,"html.parser")
    # requests and BeautifulSoup libraries that grab the source data
    # in every iteration for every page
    all = soup.find_all("div",{"class":"PropertyTableData__row"})
    # Store the div tag information for properties in all variable
    for item in all[1:len(all)]:
    # This for loop iterates within each page through all the properties
        d = {}
        # Create an empty dictionary that will be stores in d variable
        try:
            d["Address"] = item.find("span",{"class": "PropertyTableData__address"}).text
            # Create Address column and store the text information in it
        except:
            d["Address"] = None
            # If there is no Address available pass None
        try:
            d["City"] = item.find("div",{"class":"PropertyTableData__item PropertyTableData__city"}).text
            # Create City column and store the text information in it
        except:
            d["City"] = None
            # If there is no City available pass None
        try:
            d["Price"] = item.find("div",{"class":"PropertyTableData__item PropertyTableData__price PropertyTableData__sortable"}).text
            # Create Price column and store the text information in it
        except:
            d["Price"] = None
            # If there is no Price available pass None
        try:
            d["Bedrooms"] = item.find("div",{"class":"PropertyTableData__item PropertyTableData__bedrooms PropertyTableData__sortable"}).text
            # Create Bedrooms column and store the text information (number of bedrooms) in it
        except:
            d["Bedrooms"] = None
            # If there is no Bedrooms available pass None
        try:
            d["Bathrooms"] = item.find("div",{"class":"PropertyTableData__item PropertyTableData__bathrooms PropertyTableData__sortable"}).text
            # Create Bathrooms column and store the text information (number of bathrooms) in it
        except:
            d["Bathrooms"] = None
            # If there is no Bathrooms available pass None
        try:
            d["Area"] = item.find("div",{"class":"PropertyTableData__item PropertyTableData__sqft"}).text
            # Create Area column and store the text information in it
        except:
            d["Area"] = None
            # If there is no Area available pass None
        try:
            d["Lot Size"] = item.find("div",{"class":"PropertyTableData__item PropertyTableData__lot_size"}).text
            # Create Lot Size column and store the text information in it
        except:
            d["Lot Size"] = None
            # If there is no Lot Size available pass None
        l.append(d)
        # Append the dictonary for every iteration to list


# In[49]:


import pandas
df = pandas.DataFrame(l)
# Import pandas library and create DataFrame from l list

df.to_csv("Output.csv")
# Turn the created DataFrame into an Output file
