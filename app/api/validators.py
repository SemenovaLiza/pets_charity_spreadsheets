from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.models import CharityProject


async def check_name_duplicate(
        project_name: str,
        session: AsyncSession,
) -> None:
    """
    Проверка, что новое имя проекта не принадлежит другому
    существующему в фонде проекту.
    """
    project_id = await charity_project_crud.get_project_id_by_name(project_name, session)
    if project_id is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Проект с таким именем уже существует!',
        )


async def check_charity_project_exists(
        charity_project_id: int,
        session: AsyncSession,
) -> CharityProject:
    """Проверка, что проект существует."""
    charity_project = await charity_project_crud.get(
        charity_project_id, session
    )
    if charity_project is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Проект не найдена!'
        )
    return charity_project


def check_charity_project_is_closed(charity_project: CharityProject):
    """
    Проверка, что закрытый проект нельзя редактировать.
    """
    if charity_project.fully_invested:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Закрытый проект нельзя редактировать!'
        )


def check_charity_project_invested_amount(project: CharityProject, new_amount: int):
    """
    Проверка, что новая требуемя сумму не меньше уже внесённой.
    """
    if project.invested_amount > new_amount:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Нельзя установить новую требуемую сумму, ниже уже вложенной!'
        )


def check_charity_project_is_invested(charity_project: CharityProject):
    """
    Проверка, что если в проект были внесены средства,
    то его удаление запрещено.
    """
    if charity_project.invested_amount > 0:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='В проект были внесены средства, не подлежит удалению!'
        )