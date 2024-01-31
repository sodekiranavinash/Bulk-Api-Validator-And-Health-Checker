# Bulk Api's Health Checker ( hit 1000's of api & check health of api using status code )

## Introduction
- This appplication can be used to check bulk api's status code by which we can understand health of that api and also utilize response from api's.

- You can customize this app to do various taks such as `api based web scraping`, `bulk api validator`, `production api's health checker` etc.

- This main purpose of this app is to explain how you can use grequests to hit 1000's of api's where `aiohttp & requests` cannot perform and fall behind.
- You can modify below mentioned files to your requirement or use.
  -   request_manager.py
  -   response_parser.py
  -   app.py ( little changes)

## How to run
- Install required dependencies using below command 
```
pip install -r requirements.txt

```
- Now run `python app.py` and wait for program to finish hitting api's & parsing them using data inside input file.

## Performance
- In my benchmarks , it can process upto 5k records(urls) under 5 minutes. (depends on url , network connection & what your parsing out of response)

## Notes
- aiohttp can be used for belwo 1000 api calls , after which it's session can be timed out thats why using Grequests.

## How to contributions
- Anybody who can abtract the app into some template structure for use in pthon backends is always welcomed & appreciated.
