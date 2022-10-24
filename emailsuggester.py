import requests
import html2text
import re
import os

print('Enter your targeted company (for best results use exact company name from LinkedIn):')
target = input()
if len(target) <= 0:
    exit(1)

print('Enter target domain:')
domain = input()
if len(domain) <= 0:
    exit(1)

print('Select method: 1 = [first].[last]@domain.com; 2 = [last].[first]@domain.com; (Default = 1)')

method = input()
if len(method) <= 0:
    method = 1
    
print('Select number of results options= 100; 200; 300; (Default = 100)')
resultsNumber = input()
if len(resultsNumber) <= 0:
    resultsNumber = 100

url = 'https://google.com/search?num=100&start=0&hl=en&meta=&q=site%3Alinkedin.com/in%20' + target
urlTwo = 'https://google.com/search?num=100&start=100&hl=en&meta=&q=site%3Alinkedin.com/in%20' + target
urlThree = 'https://google.com/search?num=100&start=200&hl=en&meta=&q=site%3Alinkedin.com/in%20' + target
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
headers = {'User-Agent': userAgent }
cookies = {"CONSENT": "YES+cb.20210720-07-p0.en+FX+410"}
results = str()
names = str()

if int(resultsNumber) <=100:
    r = requests.get(url, headers=headers, cookies=cookies)
    text = html2text.html2text(r.text)
elif int(resultsNumber) <=200:
    r = requests.get(url, headers=headers. ccookies=cookies)
    text = html2text.html2text(r.text)
    r = requests.get(urlTwo, headers=headers, cookies=cookies)
    text = text + html2text.html2text(r.text)
else:
    r = requests.get(url, headers=headers, cookies=cookies)
    text = html2text.html2text(r.text)
    r = requests.get(urlTwo, headers=headers, cookies=cookies)
    text = text + html2text.html2text(r.text)
    r = requests.get(urlThree, headers=headers, cookies=cookies)
    text = text + html2text.html2text(r.text)

file = open('output.txt','w+', encoding="UTF-8")
print(text, file=file)
file.close()


file = open('output.txt', encoding="UTF-8")

for line in file:
    line = line.rstrip()
    if line.startswith('###') :
        results = results + '\n' + line


results = results.lower()
results = results.replace('### ','').replace(' | linkedin',' -').replace('ě','e').replace('č','c').replace('ř','r').replace('ž','z').replace('š','s').replace('ý','y').replace('á','a').replace('í','i').replace('é','e').replace('ó','o').replace('ť','t').replace('ů','u').replace('ü','u').replace('...', '-')


file = open('output.txt','w', encoding="UTF-8")
peopleInfo = open('peopleInfo.txt','w', encoding="UTF-8")
print(results, file=file)
print(results, file=peopleInfo)

if int(method) <= 1:
    file = open('output.txt','r', encoding="UTF-8")
    for line in file:
        if line.startswith('\n') : continue
        words = line.split()
        names = names + words[0] + '.' + words[1] + '@' + domain + '\n'
else:
    file = open('output.txt','r', encoding="UTF-8")
    for line in file:
        if line.startswith('\n') : continue
        words = line.split()
        names = names + words[1] + '.' + words[0] + '@' + domain + '\n'

print(names)
file = open('output.txt', 'w').close()
file = open('output.txt','w+', encoding="UTF-8")
print(names, file=file)
