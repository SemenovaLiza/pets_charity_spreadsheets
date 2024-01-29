from datetime import datetime

from aiogoogle import Aiogoogle

from app.core.constants import (FORMAT, PERMISSIONS_BODY, SPREADSHEET_BODY,
                                TABLE_VALUES)


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    """Cоздаtn гугл-таблицы с отчётом на диске сервисного аккаунта."""
    now_date_time = datetime.now().strftime(FORMAT)
    service = await wrapper_services.discover('sheets', 'v4')
    SPREADSHEET_BODY['properties']['title'] = f'Отчет на {now_date_time}'
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=SPREADSHEET_BODY)
    )
    return response['spreadsheetId']


async def set_user_permissions(
        spreadsheet_id: str,
        wrapper_services: Aiogoogle
) -> None:
    """
    Выдает права личному аккаунту на документы,
    которые создадются на диске сервисного аккаунта.
    """
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=PERMISSIONS_BODY,
            fields="id"
        ))


async def spreadsheets_update_value(
        spreadsheet_id: str,
        projects: list,
        wrapper_services: Aiogoogle
) -> None:
    """
    Обновляет данные в гугл-таблице.
    """
    service = await wrapper_services.discover('sheets', 'v4')
    for project in projects:
        new_row = [
            project.name,
            str(project.close_date - project.create_date),
            project.description
        ]
        now_date_time = datetime.now().strftime(FORMAT)
        TABLE_VALUES.append(new_row)
        TABLE_VALUES[0].append(now_date_time)

    update_body = {
        'majorDimension': 'ROWS',
        'values': TABLE_VALUES
    }
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range='A1:C30',
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
