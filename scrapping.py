import requests
from bs4 import BeautifulSoup


def scrape(url_base):
    response = requests.get(url_base)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        text = '\n'.join([p.text for p in paragraphs])
        return text
    else:
        print(f"Failed to fetch data for Status code: {response.status_code}")
        return None


def scrape_and_save_data(urls):
    for i, url in enumerate(urls):
        raw_text = scrape(url)
        if raw_text:
            word_count = len(raw_text.split())
            file_name = f"data_{i}.txt"
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(raw_text)
                print(f"Scraped data from {url} and saved to {file_name} and word count is {word_count}")


travel_url = ['https://www.nytimes.com/international/section/travel', 'https://en.wikipedia.org/wiki/travel',
       'https://blog.google/products/search/google-summer-travel-tips-2024/', 'https://time.com/5166659/how-to-travel-the-world/',
       'https://blog.ricksteves.com/', 'https://www.wildfrontierstravel.com/en_GB/blog/guide-to-travelling-in-pakistan',
       'https://www.lonelyplanet.com/articles/things-to-know-before-traveling-to-pakistan',
       'https://www.intrepidtravel.com/adventures/reasons-to-travel-to-pakistan/',
       'https://www.nomadicmatt.com/travel-guides/europe-travel-tips/',
       'https://expatexplore.com/blog/10-of-the-best-reasons-to-travel-to-europe/',
       'https://www.eurotravelcoach.com/blog/how-to-plan-a-great-trip-to-europe',
       'https://www.joaoleitao.com/europe-travel-blogs/', 'https://www.wanderlustchloe.com/europe/',
       'https://www.nomadicmatt.com/travel-blogs/cheap-ways-to-travel-across-europe-2/',
       'https://www.worldpackers.com/articles/australia-travel-tips']

fashion_url = [
    'https://fashionunited.com/news/fashion/tracing-a-trend-serving-tenniscore-with-tiktok-miu-miu-and-zendaya/2024042559585',
    'https://fashionunited.com/news/fashion/report-shines-light-on-next-gen-fur-posing-the-question-what-makes-fur-fur/2024042559562',
    'https://www.fashionstudiesjournal.org/',
    "https://www.whowhatwear.com/",
    "https://www.vogue.com/magazine",
    "https://www.harpersbazaar.com/",
    'https://fashionunited.com/news/fashion/mango-launches-victoria-beckham-collaboration/2024042359539',
    "https://www.bustle.com/",
    "https://intothegloss.com/",
    "https://stylecaster.com/",
    "https://www.thezoereport.com/",
    "https://fashionunited.com/news/fashion/fw24-fashion-months-top-influencers-include-k-pop-stars/2024041859475",
    "https://www.puttingmetogether.com/",
    'https://fashionunited.com/news/fashion/behind-the-veil-with-brenna-simmons-founder-creative-director-of-nordeen/2024041759466',
    "https://studioquirk.com/whatiwore/tag/What+I+Wore+blog"
]

disease_url = [
    "https://www.everydayhealth.com/infectious-diseases/what-bacterial-infection-sent-madonna-to-the-hospital/",  
    "https://www.everydayhealth.com/infectious-diseases/food-borne-diarrheal-illness-cyclosporiasis-reported/", 
    "https://www.patient.co.uk/",
    "https://everydayhealth.com/infectious-diseases/new-studies-confirm-mpox-vaccine-effectiveness/", 
    "https://www.everydayhealth.com/coronavirus/the-ultimate-guide-to-cleaning-and-disinfecting-surfaces-in-covid-19-times/", 
    "https://wwwnc.cdc.gov/eid/article/30/5/23-1273_article", 
    'https://wwwnc.cdc.gov/eid/article/30/5/23-1646_article',
    'https://wwwnc.cdc.gov/eid/article/30/5/23-1130_article',
    'https://www.medicalnewstoday.com/articles/237191',
    'https://my.clevelandclinic.org/health/articles/7040-gastrointestinal-diseases',
    'https://en.wikipedia.org/wiki/Disease',
    'https://www.who.int/news/item/26-04-2024-statement-on-the-antigen-composition-of-covid-19-vaccines',
]
#scrape_and_save_data(travel_url)
#scrape_and_save_data(fashion_url)
scrape_and_save_data(disease_url)
print("Data saved successfully.")
