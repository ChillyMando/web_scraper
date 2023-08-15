from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=Canada').text


soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
for job in jobs:
    published_date = job.find(
        'span', class_="sim-posted").text
    if 'few' in published_date:
        company_name = job.find(
            'h3', class_='joblist-comp-name').text.replace(' ', '')
        skills = job.find(
            'span', class_="srp-skills").text.replace(' ', '').replace(',', ', ')

        print(f'''
        Comapny Name: {company_name}
        Required Skills: {skills}
        Published Date: {published_date}
        ''')
        print('-----------------------------------')
