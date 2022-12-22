import requests

"""
Usage: python3 spyPlane.py
Finds location of IP address
"""

ipFile = input('IP Address File: ')

params = ['query', 'status', 'country', 'countryCode', 'city', 'timezone', 'mobile']

if ipFile.strip('1234567890. ') == 'IP':
    resp = requests.get('http://ip-api.com/json/' + ipFile.strip('IP '), params={'fields': ','.join(params)})
    info = resp.json()
    print(info)
    quit()

ipFileTxt = open(ipFile)
ips = ipFileTxt.readlines()

num_lines = len(ipFile)

for i in range(num_lines):
    resp = requests.get('http://ip-api.com/json/' + ips[i].strip('\n'), params={'fields': ','.join(params)})
    info = resp.json()
    print(info)
    print('==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==')
    if i == num_lines:
        quit()
