import requests
from time import sleep
from bs4 import BeautifulSoup


HEADERS = {"user-agent": "Fake user-agent"}


# Requisito 1
def fetch(url):
    sleep(1)
    try:
        page = requests.get(url, headers=HEADERS, timeout=3)
        if page.status_code == 200:
            return page.text
        else:
            return None
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    soup.prettify()
    array = []
    for item in soup.find_all("a", {"class": "cs-overlay-link"}):
        array.append(item['href'])
    if len(array) > 0:
        return array
    else:
        return []


# Requisito 3
def scrape_next_page_link(html_content):
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        return soup.find(
            "a",
            {"class": "next page-numbers"},
        )["href"]
    except TypeError:
        return None


# Requisito 4
def scrape_news(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    href = soup.find("link", {"rel": "canonical"})["href"]
    title = soup.find("h1", {"class": "entry-title"}).get_text().strip()
    data = soup.find("li", {"class": "meta-date"}).get_text()
    author = soup.find("a", {"class": "url fn n"}).get_text()
    time = soup.find("li", {"class": "meta-reading-time"}).get_text()
    time_temp = time[0] + time[1]
    array = soup.find_all("p")[0].get_text()
    new_array = array.replace("\xa0", "").strip()
    category = soup.find("span", {"class": "label"}).get_text()
    return {
        "url": href,
        "title": title,
        "timestamp": data,
        "writer": author,
        "reading_time": int(time_temp),
        "summary": new_array,
        "category": category,
        }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
