
from datetime import datetime, timedelta
from app.database.models import async_session, User
from sqlalchemy import select


# Создание пользователя, если его нет в базе
async def set_user(tg_id: int, username: str = None) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            session.add(User(tg_id=tg_id, username=username))
            await session.commit()


# Регистрация покупки подписки
async def register_purchase(tg_id: int, amount: int):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if user:
            user.amount = amount
            user.purchase_date = datetime.now()

            # Если подписка на месяц, добавляем 30 дней к дате окончания
            if amount == 650:
                user.end_date = user.purchase_date + timedelta(days=30)
            # Если разовая покупка, дата окончания не нужна
            elif amount == 6000:
                user.end_date = None

            await session.commit()


# Получение всех пользователей
async def get_all_users():
    async with async_session() as session:
        result = await session.scalars(select(User))
        return result.all()
