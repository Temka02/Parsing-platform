# Импортирование
import os
import requests
import fake_useragent 
import time
import mysql.connector
from flask import Flask, render_template, request, url_for, redirect, jsonify
import logging
from bs4 import BeautifulSoup



app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
app.config['DEBUG'] = True


# Создание переменной ua
ua = fake_useragent.UserAgent()

# Подключение к БД
DATABASE_HOST = os.getenv('DATABASE_HOST', 'db')
DATABASE_USER = os.getenv('DATABASE_USER', 'root')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'Fhntv1002%')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'parsed_data')

time.sleep(10)

retries = 5
while retries > 0:
    try:
        mydb = mysql.connector.connect(
            host=DATABASE_HOST,
            user=DATABASE_USER,
            passwd=DATABASE_PASSWORD,
            database=DATABASE_NAME
        )
        use_mydb = mydb.cursor()
        use_mydb.execute("CREATE TABLE IF NOT EXISTS vacancies_info (name VARCHAR(255), salary VARCHAR(255), experience VARCHAR(255), employer VARCHAR(255), workAddress VARCHAR(255))")
        break
    except mysql.connector.Error as err:
        app.logger.error(f"Error: {err}")
        retries -= 1
        time.sleep(5)  # Задержка 5 секунд перед повторной попыткой

if retries == 0:
    raise RuntimeError("Failed to connect to the database after several attempts")


@app.route("/")
def main():
    if use_mydb:
        try:
            use_mydb.execute("TRUNCATE TABLE vacancies_info")
            return render_template('main.html')
        except Exception as e:
            logging.error(f"Query failed: {e}")
            return str(e)
    else:
        return "Database connection failed"

@app.route('/process', methods=['POST'])
def process():
    req = request.form['req']
    curEducation = request.form['education']
    curSalary = request.form['salary'].replace("so'm", ' ')
    curExperience = request.form['experience']
    curOnlyWithSalary = request.form['onlyWithSalary']
    k = 1
    for a in getLinksOfVacancies(req, curEducation, curOnlyWithSalary, curSalary, curExperience):
        print(f'{k} - {getInfoFromVacancies(a)}')
        k+=1
    return redirect(url_for('vacancies', req=req, curEducation = curEducation, curSalary = curSalary, curExperience = curExperience, curOnlyWithSalary = curOnlyWithSalary))

@app.route("/", methods=['POST'])
def home():
    use_mydb.execute("TRUNCATE TABLE vacancies_info")
    return render_template('main.html')

@app.route("/vacancies", methods=['GET', 'POST'])
def vacancies():
    if use_mydb:
        try:
            use_mydb.execute("SELECT * FROM vacancies_info")
            data = use_mydb.fetchall()
            print(data)
            return render_template('index.html', data=data)

        except Exception as e:
            logging.error(f"Query failed: {e}")
            return str(e)
    else:
        return "Database connection failed"

# Получение ссылок на вакансии
def getLinksOfVacancies(inputText, education, onlyWithSalary, salary, experience, maxNumberOfVacancies = 40):
    hhHeaders = {
        "user-agent": ua.random
    }
    if education != None:
        searchEducation = True
    if searchEducation:
        if onlyWithSalary == '+':
            if salary != '0' or salary != '':
                # if (experience == '1-3' or experience == '1 -3' or experience == '1- 3' or experience == '1 - 3)'):
                if experience == '1-3':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between1And3&only_with_salary=true&salary={salary}&education={education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                    
                elif experience == '3-6':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between3And6&only_with_salary=true&salary={salary}&education={education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '0':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=noExperience&only_with_salary=true&salary={salary}&education={education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '>6':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=moreThan6&only_with_salary=true&salary={salary}&education={education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                else:
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&only_with_salary=true&salary={salary}&education={education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
            else:
                if experience == '1-3':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between1And3&only_with_salary=true&education={education}'    
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '3-6':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between3And6&only_with_salary=true&education={education}'    
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '0':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=noExperience&only_with_salary=true&education={education}'    
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '>6':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=moreThan6&only_with_salary=true&education={education}'    
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                else:
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&only_with_salary=true&education={education}'        
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
        else:
            if salary != '0' or salary != '':
                if experience == '1-3':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between1And3&only_with_salary=false&salary={salary}&education={education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '3-6':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between3And6&only_with_salary=false&salary={salary}&education={education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '0':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=noExperience&only_with_salary=false&salary={salary}&education={education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '>6':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=moreThan6&only_with_salary=false&salary={salary}&education={education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                else:
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&only_with_salary=false&salary={salary}&education={education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
            else:
                if experience == '1-3':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between1And3&only_with_salary=false&education={education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '3-6':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between3And6&only_with_salary=false&education={education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '0':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=noExperience&only_with_salary=false&education={education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '>6':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=moreThan6&only_with_salary=false&education={education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                else:
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&only_with_salary=false&education={education}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)                   
    else:
        if onlyWithSalary == '+':
            if salary != '0' or salary != '':
                if experience == '1-3':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between1And3&only_with_salary=true&salary={salary}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '3-6':
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
                if experience == '1-3':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between1And3&only_with_salary=true'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '3-6':
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
                if experience == '1-3':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between1And3&only_with_salary=false&salary={salary}'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '3-6':
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
                if experience == '1-3':
                    hhUrl = f'https://hh.ru/search/vacancy?text={inputText}&items_on_page=20&experience=between1And3&only_with_salary=false'
                    hhRequest = requests.get(
                    url = hhUrl, 
                    headers = hhHeaders)
                    print(hhUrl)
                elif experience == '3-6':
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
    vacancyCount = 0

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
                vacancyCount +=1 
                yield link
            
            count -= 1   

        except Exception as e:
            print(f'{e}')
        time.sleep(0.05)
        if vacancyCount >= maxNumberOfVacancies:
            break

# Получение информации о вакансии по ссылкам
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
    try:
        curNameOfVacancy = hhSoup.find('div', {'class': 'vacancy-title'}).find('h1', {'class': 'bloko-header-section-1'}).text
        curSalary = hhSoup.find('div', {'class': 'vacancy-title'}).find('span', {'class': 'magritte-text___pbpft_3-0-9'}).text.replace('\xa0', '').replace("so'm", '')
        curEmployer = hhSoup.find('div', {'class': 'vacancy-company-details'}).find('span', {'class': 'vacancy-company-name'}).find('a', {'class':'bloko-link'}).find('span', {'class': 'bloko-header-section-2'}).text.replace('\xa0', '')
        curWorkAddress = hhSoup.find('div', {'class': 'vacancy-company-redesigned'}).find_all('div')[-1].text
        curExperience = hhSoup.find('div', {'class': 'wrapper-flat--H4DVL_qLjKLCo1sytcNI'}).find('p', {'class': 'vacancy-description-list-item'}).find('span').text
        insertInfo = f"INSERT INTO vacancies_info (name, salary, experience, employer, workAddress) VALUES ('{curNameOfVacancy}', '{curSalary}', '{curExperience}', '{curEmployer}', '{curWorkAddress}')"
        use_mydb.execute(insertInfo)
        mydb.commit()
    except:
        pass
    #     curNameOfVacancy = 'Не найдена информация о названии вакансии'
    #     curSalary = 'Не найдена информация о доходе'
    #     curEmployer = 'Не найдена информация о работодателе'
    #     curExperience = 'Не найдена информация о требуемом опыте работы'
    #     curWorkAddress = 'Не найдена информация о требуемом адресе работы'
    

# Запуск программы
if __name__ == '__main__':
    print('--------------------------------------------------->')
    app.run()

