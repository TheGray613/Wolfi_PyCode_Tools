import requests
import re

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