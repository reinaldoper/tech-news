from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
import pytest
from unittest.mock import MagicMock


def test_reading_plan_group_news():
    mock_bank = [
        {
            "url": "https://blog.betrybe.com/novidades/jaqueta",
            "title": "Jaquetas",
            "timestamp": "04/03/2022",
            "writer": "ciclano",
            "reading_time": 5,
            "summary": "Agora vai",
            "category": "Roupa",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia1",
            "title": "Notícia1",
            "timestamp": "05/09/2021",
            "writer": "Beltrano",
            "reading_time": 9,
            "summary": "Agora vai passar",
            "category": "Developend",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia4",
            "title": "Ananias",
            "timestamp": "06/04/2022",
            "writer": "Ananias",
            "reading_time": 20,
            "summary": "Furou o teto",
            "category": "Turismo",
        },
    ]

    msg_error = "Valor 'available_time' deve ser maior que zero"

    ReadingPlanService._db_news_proxy = MagicMock(return_value=mock_bank)

    with pytest.raises(ValueError, match=msg_error):

        ReadingPlanService.group_news_for_available_time(-1)

    read_response = ReadingPlanService.group_news_for_available_time(6)
    assert len(read_response["unreadable"]) == 2

    assert len(read_response["readable"]) == 1

    if len(read_response["readable"]) > 0:
        assert read_response["readable"][0]["unfilled_time"] == 1
