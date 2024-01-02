# use the req model
import requests

url = 'https://jsonplaceholder.typicode.com/users'
res = requests.get(url)

print(res) # <class name and status code>
print(res.status_code)# get the status code of the http res

if 200 <=res.status_code <400: # check if the status code is valid or not
    print('healthy api')
else:
    print('ooooooo failue')

# print(res.text) # return the HTML page
page_content = res.text # return the HTML page

# print(type(page_content))

# print(page_content)

data = res.json() # new variable -> list of dict
print(type(data)) # data
print(type(data[0])) # dict

# print(data[0]['name'])
# print(data[1]['name'])
# print(data[2]['name'])
# print(data[3]['name'])
# print(data[4]['name'])
# print(data[5]['name'])

for user in data: # iterate over the list and user will be the alias for each dict
    print(user['name'])

for user in data:
    for k,v in user.items():
        if k in ['name', 'email']:
            print(f'{k}==> {v}' )
    print('----------new user----------\n')