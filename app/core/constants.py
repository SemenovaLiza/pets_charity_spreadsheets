from datetime import datetime

from app.core.config import settings

FORMAT = "%Y-%m-%d %H:%M:%S"
NOW_DATE_TIME = datetime.now().strftime(FORMAT)
SPREADSHEET_BODY = {
    'properties': {
        'title': f'Отчет от {NOW_DATE_TIME}',
        'locale': 'ru_RU'
    },
    'sheets': [{
        'properties': {
            'sheetType': 'GRID',
            'sheetId': 0,
            'title': 'Лист1',
            'gridProperties': {
                'rowCount': 100,
                'columnCount': 11
            }
        }
    }]
}

PERMISSIONS_BODY = {
    'type': 'user',
    'role': 'writer',
    'emailAddress': settings.email
}

TABLE_VALUES = [
    ['Отчет от', NOW_DATE_TIME],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание']
]
