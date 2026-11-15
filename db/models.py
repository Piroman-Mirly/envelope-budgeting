from sqlalchemy import BigInteger, String, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import create_engine

engine = create_engine(url='sqlite:///db.sqlite3')
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

class Bank(Base):
    __tablename__ = 'banks' # Название таблицы, которая будет отображать общее кол-во денег на балансе
    
    id: Mapped[int] = mapped_column(primary_key=True) # Айди баланса
    
    value: Mapped[int] # Кол-во денег на балансе
    
    operations: Mapped[list["Operation"]] = relationship(back_populates='bank') # Связь с пополнениями
    envelopes: Mapped[list["Envelope"]] = relationship(back_populates='bank') # Связь с конвертами

class Operation(Base):
    __tablename__ = 'operations' # Название таблицы, которая содержит данные о всех пополнениях
    
    id: Mapped[int] = mapped_column(primary_key=True) # Айди операции
    
    top_up_amount: Mapped[int] = mapped_column(nullable=False) # Сумма пополнения счёта
    
    bank_id: Mapped[int] = mapped_column(ForeignKey('banks.id'), nullable=False) # Внешний ключ - айди счёта, на который посупило пополнение

class Envelope(Base):
    __tablename__ = 'envelopes' # Название таблицы с конвертами
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    envelope_name: Mapped[str] = mapped_column(String(32), nullable=False) # Название конверта
    percent: Mapped[int] = mapped_column(nullable=False) # Проценты, которые изымает конверт
    envelope_balance: Mapped[int] # Баланс конверта
    
    bank_id: Mapped[int] = mapped_column(ForeignKey('banks.id'), nullable=False) # Определяет к какому счёту принадлежит конверт

def init_db():
    Base.metadata.create_all(engine)
    
    
    
    
    
    