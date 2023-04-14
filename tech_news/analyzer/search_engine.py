from tech_news.database import (
    search_news
)
from datetime import datetime


# Requisito 7
def search_by_title(title):
    response = search_news({"title": {"$regex": title.lower()}})
    list_result = [(item["title"], item["url"]) for item in response]
    return list_result


# Requisito 8
def search_by_date(date):
    try:
        date_format = datetime.strptime(date, "%Y-%m-%d")
        new_format = date_format.strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")

    response = search_news({"timestamp": new_format})
    list_result = [(item["title"], item["url"]) for item in response]
    return list_result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
