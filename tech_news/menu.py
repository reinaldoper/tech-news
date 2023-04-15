# Requisitos 11 e 12
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title, search_by_date, search_by_category
)
from tech_news.analyzer.ratings import top_5_categories
import sys


menu = "Selecione uma das opções a seguir:\n 0 - Popular o banco com notícias"
menu1 = ";\n 1 - Buscar notícias por título;\n 2 - Buscar notícias por data;\n"
menu2 = " 3 - Buscar notícias por categoria;\n "
menu3 = "4 - Listar top 5 categorias;\n 5 - Sair."


def analyzer_menu():
    value_options = input(f"{menu}{menu1}{menu2}{menu3}")
    match value_options:
        case "0":
            value = int(input("Digite quantas notícias serão buscadas:"))
            get_tech_news(value)
        case "1":
            title = input("Digite o título:")
            search_by_title(title)
        case "2":
            data = input("Digite a data no formato aaaa-mm-dd:")
            search_by_date(data)
        case "3":
            category = input("Digite a categoria:")
            search_by_category(category)
        case "4":
            top_5_categories()
        case "5":
            print("Encerrando script\n")
        case _:
            sys.stderr.write("Opção inválida\n")
