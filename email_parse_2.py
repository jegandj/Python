# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 15:13:27 2021

@author: DaviesJones
"""

import os, re, html
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
    #create a list for digits
    by = []
    #select key words
    a = re.search('Hi(.+?), Thanks', text)
    if a:
        Name = a.group(1)
    b = re.search('Company:(.+?)Job', text)
    if b:
        Company = b.group(1)
    c = re.search('Role:(.+?)Email', text)
    if c:
        Role = c.group(1)
    d = re.search('Email:(.+?)Permission', text)
    if d:
        Email = d.group(1)
    #extract key phrase
    a = "No CURRENT64% FUTURE0% CURRENT36% FUTURE9% CURRENT0% FUTURE91% Product"
    ab = re.search("No (.+?)\% Product", a).group(1)
    #extract digits and %
    li = re.sub("[^\d\%]", "", ab)
    #replace % with comma
    li = li.replace("%"," ")
    #split the strings
    li = li.split()
    #create a list of digits
    #by.append(li)
    #create a list of values
    bb = [Name, Company, Role, Email]
    #Join both lists
    bbby = bb + li
    df.append(bbby)

print(df)
deff = DataFrame(df)
print(deff)
#deff.to_excel('test2.xlsx', sheet_name='sheet1', index=False)

