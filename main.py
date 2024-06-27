import requests, fake_useragent, time, json, random
from bs4 import BeautifulSoup

ua = fake_useragent.UserAgent()
req = input().replace(' ', '+')

def openVacancies(inputText):
    hhURL = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=100'
    hhHeaders = {
        "user-agent": ua.random
    }
    hhRequest = requests.get(hhURL, headers=hhHeaders)
    hhSoup = BeautifulSoup(hhRequest.text, 'lxml')
    vacancies = []
    listOfSalaries = []
    namesOfVacancies = hhSoup.findAll('span', {'class':'vacancy-name--c1Lay3KouCl7XasYakLk'})
    salaries = hhSoup.findAll('span', {'class': 'compensation-text--kTJ0_rp54B2vNeZ3CTt2'})

    for salary in salaries:
        listOfSalaries.append(salary.text)

    for nameOfVacancy in namesOfVacancies:
        vacancies.append(nameOfVacancy.text)

    print(len(vacancies))
    print(len(listOfSalaries))

print(openVacancies(req))

