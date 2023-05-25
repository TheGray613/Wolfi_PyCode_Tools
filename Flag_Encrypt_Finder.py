import requests
import base64

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
