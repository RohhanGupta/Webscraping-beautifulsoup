from bs4 import  BeautifulSoup
import requests
import time

html = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

unfamiliar = input("Enter a skill you are not familiar with: ")

def find_job():
    for job in jobs:
        published_date = job.find('span', class_='sim-posted').text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            if unfamiliar not in skills:
                more_info = job.header.h2.a['href']
                print(f'Company Name: {company_name.strip()}')
                print(f'Skills: {skills.strip()}')
                print(f'Published Time: {published_date.strip()}')
                print(f'More Information: {more_info}')
                print("  ")

if __name__ == '__main__':
    while True:
        find_job()
        print("Plase wait for 10 minutes.....")
        time.sleep(600)