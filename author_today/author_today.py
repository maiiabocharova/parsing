from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

from tqdm.auto import tqdm
import time

from book_creation import create_book_from_chapters

from authentications import LOGIN, PASSWORD

browser = webdriver.Chrome()

BASE_URL = "https://author.today"

browser.get(BASE_URL)

# logging in
el = browser.find_element(By.XPATH,"//a[contains(text(), 'Войти')]")
el.click()
login_el = browser.find_element(By.NAME,
                                "Login")
password_el = browser.find_element(By.NAME,
                                "Password")

login_el.send_keys(LOGIN)
password_el.send_keys(PASSWORD)
xpath = "//form//button[@type='submit' and contains(text(), 'Войти')]"
submit_btn = browser.find_element(By.XPATH, xpath)
submit_btn.click()

book_url = "https://author.today/reader/80729/632313"

browser.get(book_url)

chapters_texts = []
chapters_names = []

book_url = "https://author.today/reader/80729/632313"
browser.get(book_url)

for _ in tqdm(range(14)):
    html = browser.page_source
    soup = BeautifulSoup(html)
    chapter_name = soup.find('div', attrs={'class': "text-container"}) \
        .find('h1').text

    chapter_text = "".join([str(el) for el in soup.find('div',
                                                        attrs={'class': "text-container"}) \
                           .find_all("p")])

    chapters_texts.append(chapter_text)
    chapters_names.append(chapter_name)

    next_btn = browser.find_element(By.XPATH, "//li[@class='next']/a")
    next_btn.click()
    time.sleep(5)

create_book_from_chapters(chapters_texts,chapters_names)
