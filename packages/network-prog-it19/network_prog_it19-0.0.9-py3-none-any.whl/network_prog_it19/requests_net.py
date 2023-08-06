import requests

base = 'http://127.0.0.1:23456/'

pc_data = {'cpu': 'AMD Ryzen',
           'ram': 16, 'ssd': 512, 'price': 1000}

response = requests.post(base + 'pcs/1', pc_data)
print(response.json())


# response = requests.delete(base + 'clients/2')
# print(response.json())