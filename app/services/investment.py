from datetime import datetime
from typing import List

from app.models import CharityProject
from app.models.charity_project import CharityProject


def investing_process(
    target: CharityProject,
    sources: List[CharityProject]
) -> List[CharityProject]:
    modified = []
    if not target.invested_amount and target.invested_amount != 0:
        target.invested_amount = 0
    for source in sources:
        to_invest = target.full_amount - target.invested_amount
        for obj in (target, source):
            obj.invested_amount += to_invest
            if obj.full_amount == obj.invested_amount:
                obj.close_date = datetime.now()
                obj.fully_invested = True
        modified.append(source)
        if target.fully_invested:
            break
    return modified