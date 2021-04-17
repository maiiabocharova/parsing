#bbc business news scraping
all_pages = requests.get('https://www.bbc.com/news/business')
all_soup = BeautifulSoup(all_pages.text)
hrefs = []
bbc = []
for href in all_soup.find_all('a', attrs={'class': 'gs-c-promo-heading'}):
    hrefs.append(href['href'])
main_link = 'https://www.bbc.com'

for href in hrefs:
    link = main_link + href  # href -> '/news/business-56671638'
    try:
        soup = BeautifulSoup(requests.get(link).text)
        for div in soup.find_all('div', attrs={'data-component': 'text-block'}):
            bbc.append(div.text)
    except Exception:
        print(link)
        
all_text_list += bbc
all_text_list = list(set(all_text_list))
