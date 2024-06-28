import requests, fake_useragent, json, time, re
from bs4 import BeautifulSoup

ua = fake_useragent.UserAgent()
req = input().replace(' ', '+')

def getLinksOfVacancies(inputText):
    
    hhHeaders = {
        "user-agent": ua.random
    }
    hhRequest = requests.get(
        url = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20', 
        headers = hhHeaders
    )

    if hhRequest.status_code != 200:
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
                url = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&page={page}', 
                headers = hhHeaders
            )

            if hhLinkRequest.status_code != 200:
                return
            
            hhLinkSoup = BeautifulSoup(hhLinkRequest.content, 'lxml')
            # hhLinks = hhLinkSoup.find_all('a', {'class': 'bloko-link'})
            hhLinks = []
            spans = hhLinkSoup.find_all('span', {'class': 'serp-item__title-link-wrapper'})
            for span in spans:
                hhLinks.append(span.find('a', {'class': 'bloko-link'}))


            for link in hhLinks:
                if link.get('href') == None or (link.get('href')[0] == '/') or not ('vacancy' in link.get('href')):
                    continue
                else:
                    yield link.get('href')

            count -= 1
        except Exception as e:
            print(f'{e}')
        time.sleep(0.05)

def getInfoFromVacancies(link):

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
    try:
        curNameOfVacancy = hhSoup.find('div', {'class': 'vacancy-title'}).find('h1', {'class': 'bloko-header-section-1'}).text
        curSalary = hhSoup.find('div', {'class': 'vacancy-title'}).find('span', {'class': 'magritte-text___pbpft_3-0-9'}).text
    except:
        curNameOfVacancy = 'Не найдена информация о названии вакансии'
        curSalary = 'Не найдена информация о доходе'
    vacancy = {
        'name': curNameOfVacancy,
        'salary': curSalary.replace('\xa0', '')
    }
    return vacancy   
# magritte-text_style-primary___AQ7MW_3-0-9

if __name__ == '__main__':
    k = 1
    for a in getLinksOfVacancies(req):
        print(f'{k} - {getInfoFromVacancies(a)}')
        k += 1
        time.sleep(0.05)
    

