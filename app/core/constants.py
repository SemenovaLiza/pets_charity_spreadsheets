from app.core.config import settings

FORMAT = "%Y-%m-%d %H:%M:%S"
SPREADSHEET_BODY = {
    'properties': {
        'title': None,
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
    ['Отчет от'],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание']
]
