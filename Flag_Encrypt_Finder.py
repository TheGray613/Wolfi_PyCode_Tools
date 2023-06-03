import requests
# This is a Python library for making HTTP requests. It provides a simple and elegant way to interact with RESTful APIs and other web services.
# The requests library provides several methods for making HTTP requests, including get(), post(), put(), delete(), and head(). These methods return a Response object that contains the server's response to the request.
# The Response object provides several attributes and methods for accessing the response data, including status_code, headers, and text.
import base64
#This is a Python module that provides functions for encoding binary data to ASCII characters and decoding ASCII characters back to binary data.
# It is often used for encoding and decoding data in email attachments, image files, and other types of files that need to be transmitted over the internet.
# The base64 module provides two main functions: b64encode() and b64decode(). b64encode() takes a bytes-like object and returns a bytes object containing the base64-encoded data.
# b64decode() takes a bytes-like object containing base64-encoded data and returns the original binary data.


# Define the base URL
start_url = 'https://wation.cloud/cyberdev/junior/http/header/100'
end_url = 'https://wation.cloud/cyberdev/junior/http/header/150'
header_name = 'WationSecret'

# Loop example in range 100 ta 150
for i in range(100, 151):
    url = f'https://wation.cloud/cyberdev/junior/http/header/{i}'
    response = requests.get(url)
    if response.status_code == 200:
    # Loop example for     
        if header_name in response.headers:
            encoded_value = response.headers[header_name]
            decoded_value = base64.b64decode(encoded_value).decode('utf-8')
            if decoded_value.startswith('Wation'):
                print(f'Found matching header in {url}: {decoded_value}')
                break
        else:
            print(f'Header not found in {url}.')
    else:
        print(f'Failed to retrieve {url}.')
