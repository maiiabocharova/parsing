# cnbc news scraping
# target can be world / business / technology / finance
def get_cnbc_news(target, all_text_list):
    all_pages = requests.get(f'https://www.cnbc.com/{target}/')
    all_soup = BeautifulSoup(all_pages.text)
    text_cnbc = []
    for href in all_soup.find_all('a', attrs={'class': 'Card-title'}):
        link = href['href']
        try:
            soup = BeautifulSoup(requests.get(link).text)
            for div in soup.find_all('div', attrs={'class': 'group'}):
                text_cnbc.append(div.text)
        except:
            print(link)
    all_text_list += text_cnbc
for target in ['world', 'business', 'technology', 'finance']:
    get_cnbc_news(target, all_text_list)
all_text_list = list(set(all_text_list))
