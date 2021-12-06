# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 15:13:27 2021

@author: DaviesJones
"""

import os, re, html
import pandas as pd
import win32com.client
from bs4 import BeautifulSoup
from pandas import DataFrame

#Create a list for values
df= []

#Create a path
folder_path = r'C:\Users\DaviesJones\iCloudDrive\Jobs\ASG\Emails'

# Initialise & populate list of emails
email_list = [file for file in os.listdir(folder_path) if file.endswith(".msg")]
# Connect to Outlook with MAPI
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

# Iterate through every email
for i, _ in enumerate(email_list):

    # Create variable storing info from current email being parsed
    msg = outlook.OpenSharedItem(os.path.join(folder_path,email_list[i]))
    # Search email HTML for body text
    regex = re.search(r"<body([\s\S]*)</body>", msg.HTMLBody)
    body = regex.group()
    soup = BeautifulSoup(body, features= "html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
        # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    text = text.replace("\n"," ")
    
    #select key words
    Name = re.search("Hi(.+?), Thanks", text).group(1)
    Company = re.search("Company:(.+?) Job", text).group(1)
    Role = re.search("Role:(.+?) Email", text).group(1)
    Email = re.search("Email:(.+?) Permission", text).group(1)
    
    #extract key phrase
    ab = re.search("CURRENT (.+?)\% Product", text).group(1)
    #extract digits and %
    li = re.sub("[^\d\%]", "", ab)
    #replace % with space
    li = li.replace("%"," ")
    #split the strings and place in a list
    li = li.split()
    #Change text to Integer
    li = list(map(int, li))
    #Divide all values by 100
    myInt = 100
    newList = [x / myInt for x in li]
    #create a list of values
    bb = [Name, Company, Role, Email]
    #Join both lists
    bbby = bb + newList
    df.append(bbby)

deff = DataFrame(df)
deff.columns = ['Name', 'Company', 'Role', 'Email', 'Current Product', 'Future Product', 'Current Price', 'Future Price', 'Current Package', 'Future Package']
print(deff)
deff.to_excel('test2.xlsx', sheet_name='sheet1', index=False)
