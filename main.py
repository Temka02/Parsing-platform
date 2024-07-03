import requests
import fake_useragent
import time
from bs4 import BeautifulSoup

ua = fake_useragent.UserAgent()
# req = input('Введите название вакансии: ').replace(' ', '+')
# experience = input('Выберите ваш опыт работы: ')
# salary = int(input('Введите предполагаемую зарплату: '))
# onlyWithSalary = input('Показать только объявления с указанной зарплатой? ')
req = 'frontend-стажер'
experience = ''
salary = 0
onlyWithSalary = ''
inputEducation = ['not_required_or_not_specified','higher']
education = ''
if inputEducation != []:
    for el in inputEducation:
        education += 'education='+el+'&'
    education = education[:-1]
    searchEducation = True
else:
    searchEducation = False




def getLinksOfVacancies(inputText):
    hhHeaders = {
        "user-agent": ua.random
    }
    
    if searchEducation:
        if onlyWithSalary == 'Да' or onlyWithSalary == 'Yes' or onlyWithSalary == '+':
            if salary != '0' or salary != '':
                if (experience == '1-3' or experience == '1 -3' or experience == '1- 3' or experience == '1 - 3)'):
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between1And3&only_with_salary=true&salary={salary}&{education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                    
                elif experience == '3-6' or experience == '3 -6' or experience == '3- 6' or experience == '3 - 6':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between3And6&only_with_salary=true&salary={salary}&{education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '0':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=noExperience&only_with_salary=true&salary={salary}&{education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '>6':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=moreThan6&only_with_salary=true&salary={salary}&{education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                else:
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&only_with_salary=true&salary={salary}&{education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
            else:
                if (experience == '1-3' or experience == '1 -3' or experience == '1- 3' or experience == '1 - 3)'):
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between1And3&only_with_salary=true&{education}'    
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '3-6' or experience == '3 -6' or experience == '3- 6' or experience == '3 - 6':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between3And6&only_with_salary=true&{education}'    
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '0':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=noExperience&only_with_salary=true&{education}'    
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '>6':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=moreThan6&only_with_salary=true&{education}'    
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                else:
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&only_with_salary=true&{education}'        
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
        else:
            if salary != '0' or salary != '':
                if (experience == '1-3' or experience == '1 -3' or experience == '1- 3' or experience == '1 - 3)'):
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between1And3&only_with_salary=false&salary={salary}&{education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '3-6' or experience == '3 -6' or experience == '3- 6' or experience == '3 - 6':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between3And6&only_with_salary=false&salary={salary}&{education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '0':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=noExperience&only_with_salary=false&salary={salary}&{education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '>6':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=moreThan6&only_with_salary=false&salary={salary}&{education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                else:
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&only_with_salary=false&salary={salary}&{education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
            else:
                if (experience == '1-3' or experience == '1 -3' or experience == '1- 3' or experience == '1 - 3)'):
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between1And3&only_with_salary=false&{education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '3-6' or experience == '3 -6' or experience == '3- 6' or experience == '3 - 6':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between3And6&only_with_salary=false&{education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '0':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=noExperience&only_with_salary=false&{education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '>6':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=moreThan6&only_with_salary=false&{education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                else:
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&only_with_salary=false&{education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)                   
    else:
        if onlyWithSalary == 'Да' or onlyWithSalary == 'Yes' or onlyWithSalary == '+':
            if salary != '0' or salary != '':
                if (experience == '1-3' or experience == '1 -3' or experience == '1- 3' or experience == '1 - 3)'):
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between1And3&only_with_salary=true&salary={salary}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '3-6' or experience == '3 -6' or experience == '3- 6' or experience == '3 - 6':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between3And6&only_with_salary=true&salary={salary}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '0':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=noExperience&only_with_salary=true&salary={salary}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '>6':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=moreThan6&only_with_salary=true&salary={salary}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                else:
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&only_with_salary=true&salary={salary}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
            else:
                if (experience == '1-3' or experience == '1 -3' or experience == '1- 3' or experience == '1 - 3)'):
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between1And3&only_with_salary=true'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '3-6' or experience == '3 -6' or experience == '3- 6' or experience == '3 - 6':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between3And6&only_with_salary=true'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '0':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=noExperience&only_with_salary=true'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '>6':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=moreThan6&only_with_salary=true'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                else:
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&only_with_salary=true'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
        else:
            if salary != '0' or salary != '':
                if (experience == '1-3' or experience == '1 -3' or experience == '1- 3' or experience == '1 - 3)'):
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between1And3&only_with_salary=false&salary={salary}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '3-6' or experience == '3 -6' or experience == '3- 6' or experience == '3 - 6':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between3And6&only_with_salary=false&salary={salary}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '0':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=noExperience&only_with_salary=false&salary={salary}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '>6':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=moreThan6&only_with_salary=false&salary={salary}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                else:
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&only_with_salary=false&salary={salary}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
            else:
                if (experience == '1-3' or experience == '1 -3' or experience == '1- 3' or experience == '1 - 3)'):
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between1And3&only_with_salary=false'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '3-6' or experience == '3 -6' or experience == '3- 6' or experience == '3 - 6':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between3And6&only_with_salary=false'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '0':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=noExperience&only_with_salary=false'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '>6':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=moreThan6&only_with_salary=false'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                else:
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&only_with_salary=false'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
    
    if hhRequest.status_code !=200:
        return
    
    hhSoup = BeautifulSoup(hhRequest.content, 'lxml')

    hhPager = hhSoup.find('div', {'class': 'pager'})
    if hhPager == None:
        numberOfPages = 1
    else:
        numberOfPages = int(hhSoup.find('div', {'class': 'pager'}).find_all('span', recursive=False)[-1].find('a').find('span').text)
    print(f'numberOfPages - {numberOfPages}')
    count = numberOfPages

    for page in range(numberOfPages):
        try:
            print(f"Осталость страниц - {count}")

            hhLinkRequest = requests.get(
                url = f'{hhUrl}&page={page}', 
                headers = hhHeaders
            )

            if hhLinkRequest.status_code != 200:
                return
            
            hhLinkSoup = BeautifulSoup(hhLinkRequest.content, 'lxml')
            # hhLinks = hhLinkSoup.find_all('a', {'class': 'bloko-link'})
            hhLinks = []
            spans = hhLinkSoup.find_all('span', {'class': 'serp-item__title-link-wrapper'})
            for span in spans:
                hhLinks.append(span.find('a', {'class': 'bloko-link'}).get('href'))

            for link in hhLinks:
                # if link.get('href') == None or (link.get('href')[0] == '/') or not ('vacancy' in link.get('href')):
                #     continue
                # else:
                yield link
            count -= 1
        except Exception as e:
            print(f'{e}')
        time.sleep(0.5)

def getInfoFromVacancies(link):
    print(link)
    hhHeaders = {
        "user-agent": ua.random
    }

    hhRequest = requests.get(
        url = link, 
        headers = hhHeaders
    )

    if hhRequest.status_code != 200:
        return
    
    hhSoup = BeautifulSoup(hhRequest.content, 'lxml')

    curNameOfVacancy = hhSoup.find('div', {'class': 'wrapper-flat--H4DVL_qLjKLCo1sytcNI'}).find('div', {'class': 'vacancy-title'}).find('h1', {'class': 'bloko-header-section-1'}).text
    curSalary = hhSoup.find('div', {'class': 'vacancy-title'}).find('span', {'class': 'magritte-text___pbpft_3-0-9'}).text
    curEmployer = hhSoup.find('div', {'class': 'vacancy-company-details'}).find('span', {'class': 'vacancy-company-name'}).find('a', {'class':'bloko-link'}).find('span', {'class': 'bloko-header-section-2'}).text
    curWorkAddress = hhSoup.find('div', {'class': 'vacancy-company-redesigned'}).select('div', class_=False).find({'class': 'magritte-text___pbpft_3-0-9'}).text
    curExperience = hhSoup.find('div', {'class': 'wrapper-flat--H4DVL_qLjKLCo1sytcNI'}).find('p', {'class': 'vacancy-description-list-item'}).find('span').text
# except:
#         curNameOfVacancy = 'Не найдена информация о названии вакансии'
#         curSalary = 'Не найдена информация о доходе'
#         curEmployer = 'Не найдена информация о работодателе'
#         curExperience = 'Не найдена информация о требуемом опыте работы'
#         curWorkAddress = 'Не найдена информация о требуемом адресе работы'

    vacancy = {
        'name': curNameOfVacancy,
        'salary': curSalary.replace('\xa0', ''),
        'experience': curExperience,
        'employer': curEmployer.replace('\xa0', ''),
        'curWorkAddress': curWorkAddress
        # 'link': link,
    }

    return vacancy


if __name__ == '__main__':
    k = 1
    print('--------------------------------------------------->')
    print(f'Ваша запрошенная вакансия - {req}')
    print(f'Ваша ожидаемая зарплата - {salary}')
    print(f'Ваш опыт работы - {experience}')
    print(f'Показать только объявления с указанной зарплатой? {onlyWithSalary}')
    print(f'Ваше образование - {education}')
    for a in getLinksOfVacancies(req):
        print(f'{k} - {getInfoFromVacancies(a)}')
        k += 1

        time.sleep(0.5)
    

