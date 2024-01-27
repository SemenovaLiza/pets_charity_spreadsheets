from typing import List, Optional

from sqlalchemy import extract, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(
        self,
        project_name: str,
        session: AsyncSession
    ) -> Optional[int]:
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        return db_project_id.scalars().first()

    async def get_charity_project_by_id(
        self,
        project_id: int,
        session: AsyncSession,
    ) -> Optional[CharityProject]:
        db_project = await session.execute(
            select(CharityProject).where(
                CharityProject.id == project_id
            )
        )
        return db_project.scalars().first()

    async def get_by_completion_rate(self) -> List[CharityProject]:
        """
        Сортировка списка со всеми закрытыми благотворительными проектами
        по количеству времени, которое понадобилось на сбор средств,
        — от меньшего к большему.
        """
        completion_rate = extract("epoch", self.model.close_date) - extract(
            "epoch", self.model.create_date
        )
        async with self.session as session:
            projects = await session.execute(
                select(self.model)
                .filter(self.model.close_date.isnot(None))
                .order_by(completion_rate)
            )
            return projects.scalars().all()


charity_project_crud = CRUDCharityProject(CharityProject)