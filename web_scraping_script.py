import requests
from bs4 import BeautifulSoup

class WebScraper():
    def __init__ (self, scraping_url):
        self.scraping_url = scraping_url

        self.scraping_method_results = self.scraping(self.scraping_url)
        
    def scraping(self, scraping_url):
        page_request = requests.get(scraping_url, verify=False)
        soup = BeautifulSoup(page_request.text, "html.parser")

        scraped_data = {}

        post_number = 1
        
        for item in soup.find_all('div', {"class": "col-sm-12 col-md-3 pb-2"}):
            date_and_author = item.span.text.split('\xa0\xa0')

            scraped_data[f'post_{post_number}'] = {"Date": str(date_and_author[0]), "Author": ' '.join(date_and_author[1:]), "Title": item.h6.text}
            post_number += 1
        return scraped_data