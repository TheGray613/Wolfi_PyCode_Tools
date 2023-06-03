import requests
#This is a Python library for making HTTP requests. It provides a simple and elegant way to interact with RESTful APIs and other web services. 
#The requests library provides several methods for making HTTP requests, including get(), post(), put(), delete(), and head(). These methods return a Response object that contains the server's response to the request. 
#The Response object provides several attributes and methods for accessing the response data, including status_code, headers, and text.
import re
#This is a Python module for working with regular expressions.
#Regular expressions are a powerful tool for searching and manipulating text.
#The re module provides several functions for working with regular expressions, including search(), match(), findall(), and sub().
#These functions allow you to search for patterns in text, extract specific parts of the text, and replace parts of the text with other text.
#The re module also provides a syntax for defining regular expressions, which includes special characters and sequences that have special meanings in regular expressions.

# Define the base URL
base_url = 'https://wation.cloud/cyberdev/junior/http/body/'

# Define the regular expression pattern to match the flag
pattern = r'^Wation.*'

# Loop through the URLs and search for the flag in the response body
for i in range(1, 51):
    url = base_url + str(i)
    response = requests.get(url)
    if response.status_code == 200:
        if re.search(pattern, response.text):
            print(f"Flag found in {url}: {re.search(pattern, response.text).group(0)}")
            break
    else:
        print(f"Error: {response.status_code} - Could not retrieve {url}")
