import requests
from bs4 import BeautifulSoup

# URLs for websites
url_9to5google = 'https://9to5google.com/feed/'
url_9to5mac = 'https://9to5mac.com/feed/'

# Function to scrape RSS Feed of site and compile simple formatting of title, link, and publication date
def get9to5News(url):
    if url == url_9to5google:
        print("---Google News ---")
    elif url == url_9to5mac:
        print("---Mac News ---")
    # Scrape the content of the page and get all the [item] tags
    request = requests.get(url).content
    soup = BeautifulSoup(request, 'xml')
    news_items = soup.find_all('item')

    # Ready lists for saving each news title, link, and publication date into
    news_list = []
    links_list = []
    dates_list = []

    # Find the title, link, and date for each news item and save it into the respective list
    for item in news_items:
        title = item.find('title').text
        news_list.append(title)
        link = item.find('link').text
        links_list.append(link)
        date = item.find('pubDate').text
        dates_list.append(date)

    # Print the 5 most-recent news items
    for i in range(5):
        print(f"Title: {news_list[i]}\nPubDate: {dates_list[i]}\nLink: {links_list[i]}\n")

# Run functions to generate output of title, link, date
get9to5News(url_9to5google)
get9to5News(url_9to5mac)
