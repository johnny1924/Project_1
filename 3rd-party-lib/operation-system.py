import datetime
import os

path = os.getcwd()

# os.system('mkdir johnny2 && cd python test && date > hello.txt') # we can run all terminal commands in python

url = 'https://github.com/johnny1924?tab=repositories'

folder_name= str(datetime.datetime.now().date())
print(folder_name)

commands = [f'git clone {url}', f'mv {url[url.rfind("/")+1]:} {folder_name}']

for commands in commands:
    os.system(commands)