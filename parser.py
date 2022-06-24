import requests, os, sqlite3
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

db = sqlite3.connect('compliment.db')
cursor = db.cursor()


URL = os.getenv('URL')


def parsing():
    page_number = 1
    for storage in range(97):
        html = requests.get(f'{URL}/{page_number}').text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find_all('div', class_='post-card__title')
        for t in title:
            article = t.get_text(strip=True)
            print(article)


            cursor.execute('''
            INSERT OR IGNORE INTO compliment(compliment_description) VALUES (?);
            ''', (article, ))
            db.commit()


            cursor.execute('''
            SELECT compliment_id FROM compliment WHERE compliment_description = ?;
            ''', (article, ))
            db.commit()

        page_number += 1

parsing()


