# Email-Suggester

Email suggester is a python OSINT script for penetration testers. This script finds people names working for a company from LinkedIn. From these names it creates email list in desired format and puts it into text file (output.txt). It also creates a second file where are listed names of a person, position and company (peopleInfo.txt).

*Note: I created this sript as a python coding practice cos i hate "normal" excercises and wanted to create something useful for cybersec comunity. I'm still learning so the code is propably spaghetti and same result could be propably done 1000 times better. But hey it works and i will update the script as my python knowledge improves.* 


## Usage


```
python3 emailsuggester.py
```


For now script will ask you for input: 

**Targeted company:** Specify target company name - for best results find exact company name on LinkedIn

**Domain:** Company domain name used in their emails.

**Format method:** Specify method for email creation 1 = [first].[last]@domain.com; 2 = [last].[first]@domain.com;  *More methods in future versions*

**Number of results:** You can select 100, 200 or 300. *Please be aware the more results you select the higher probability of false positives. I recommend to check peopleInfo.txt for verification*

Plannig to rewrite usage to command line args in future versions when i have more time. 


## Licensing

I don't care. Do whatever you want. Just be nice and don't do stupid things. 



