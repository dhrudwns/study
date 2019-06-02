import requests
from bs4 import BeautifulSoup
import re

url = input("Target URL : ")
req = requests.get(url)
header = req.headers
dic = {'server' : 'hidden', 'os' : 'hidden', 'lan' : 'hidden'}
def get_header():
    if 'Server' in header:
        server=header['Server']
        s = server.split(' ')
        for i, a in enumerate(dic.keys()):
            dic[a] = s[i]
            if (len(s) < len(dic)):
                break
        print(dic)
    else:
        print(dic)
    return dic
def check_cve(get_header):
    r = requests.get('https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword='+str(dic['server']))
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.select("#smaller"))
    target = soup.find(class_="smaller")
    count = target.find("b").text
    print('sever : ', count)
    print(soup.select("#TableWithRules"))

get_header()
check_cve(get_header)

