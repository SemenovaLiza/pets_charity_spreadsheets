from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.charity_project import charity_project_crud
from app.crud.donation import donation_crud
from app.models import User
from app.schemas.donation import DonationCreate, DonationDB, DonationBase
from app.services.investment import investing_process

router = APIRouter()


@router.post(
    '/',
    response_model=DonationCreate,
    dependencies=[Depends(current_user)],
    response_model_exclude_none=True,
)
async def create_donation(
    donation: DonationBase,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    """
    Сделать пожертвование.
    """
    new_donation = donation_crud.create_not_commit(donation, user)
    session.add(new_donation)
    fill_models = await charity_project_crud.get_not_fully_invested_objects(session)
    invested_list = investing_process(new_donation, fill_models)
    await donation_crud.commit_models(invested_list, session)
    await session.refresh(new_donation)
    return new_donation


@router.get(
    '/',
    response_model=List[DonationDB],
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session),
):
    """
    Только для суперпользователя.
    Возвращает список всех пожертвований.
    """
    all_donations = await donation_crud.get_multi(session)
    return all_donations


@router.get(
    '/my',
    response_model=List[DonationCreate],
    response_model_exclude={'user_id'},
)
async def get_my_donations(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    """Возвращает список моих пожертвований."""
    donations = await donation_crud.get_donation_by_user(
        session=session, user=user
    )
    return donations