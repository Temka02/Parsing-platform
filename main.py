import requests, fake_useragent, time, json, random
from bs4 import BeautifulSoup

ua = fake_useragent.UserAgent()
req = input().replace(' ', '+')

def getLinksOfVacancies(inputText):
    
    hhHeaders = {
        "user-agent": ua.random
    }
    hhRequest = requests.get(
        url = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=100', 
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
        print(f"Осталость страниц - {count}")
        hhLinkRequest = requests.get(
            url = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=100&page={page}', 
            headers = hhHeaders
        )
        if hhLinkRequest.status_code != 200:
            return
        hhLinksHref = []
        hhLinkSoup = BeautifulSoup(hhLinkRequest.content, 'lxml')
        hhLinks = hhLinkSoup.find_all('a', {'class': 'bloko-link'})
        for link in hhLinks:
            if link.get('href') == None or (link.get('href')[0] == '/') or not ('vacancy' in link.get('href')):
                continue
            else:
                hhHref = link.get('href')
                hhLinksHref.append(hhHref)
        # print(hhLinksHref)
        count -= 1
        # print(f'Всего вакансий на этой странице {len(hhLinksHref)}')

if __name__ == '__main__':
    getLinksOfVacancies(req)


