from flask import Flask
from flask_cors import CORS
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title, search_by_date, search_by_category
)
from tech_news.analyzer.ratings import top_5_categories

app = Flask(__name__)
CORS(app)
""" app.config['CORS_HEADERS'] = 'Content-Type' """


@app.route('/endpoint')
def endpoint_handler():
    return top_5_categories()


@app.route('/get_news/<num>')
def get_news(num):
    return get_tech_news(int(num))


@app.route('/title/<title>')
def get_title(title):
    return search_by_title(title)


@app.route('/data')
def get_data(data):
    return search_by_date(data)


@app.route('/category/<category>')
def get_category(category):
    return search_by_category(category)
