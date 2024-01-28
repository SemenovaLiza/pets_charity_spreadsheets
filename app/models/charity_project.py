from sqlalchemy import Column, String, Text

from .abstract import Abstract


class CharityProject(Abstract):
    """
    Модель для представления проектов в БД.
    """
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self):
        return (
            f'CharityProject(name={self.name}, '
            f'description={self.description}), '
            f'full_amount={self.full_amount}), '
            f'invested_amount={self.invested_amount})'
        )

    def __str__(self):
        return (
            f'Благотворительный проект: {self.name}, '
            f'описание проекта: {self.description}, '
            f'необходимая сумма: {self.full_amount}, '
            f'внесенная сумма: {self.invested_amount})'
        )
