
from datetime import datetime
from sqlalchemy import BigInteger, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine("sqlite+aiosqlite:///db.sqlite3")
async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True, index=True)
    username: Mapped[str] = mapped_column(String, nullable=True)  # Никнейм пользователя
    purchase_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)  # Дата покупки
    end_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)  # Дата окончания подписки
    amount: Mapped[int] = mapped_column(Integer, default=0)  # Сумма покупки

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
