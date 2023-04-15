from tech_news.database import (
    find_news,
)


# Requisito 10
def top_5_categories():
    response = find_news()
    if len(response) == 0:
        return []
    else:
        contagens = {}
    for category in response:
        if category["category"] in contagens:
            contagens[category["category"]] += 1
        else:
            contagens[category["category"]] = 1

    top_5 = sorted(contagens.items(), key=lambda x: (-x[1], x[0]))
    top_5 = top_5[:5]
    array = []
    for contagem in top_5:
        array.append(contagem[0])
    return array
