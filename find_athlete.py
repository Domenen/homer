

import sqlalchemy as sa
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"

Base = declarative_base()


class User(Base):
    """Описывает структуру таблицы user для хранения регистрационных данных пользователей
    """
    __tablename__ = "user"

    id = sa.Column(sa.INTEGER, primary_key = True, autoincrement = True)
    first_name = sa.Column(sa.TEXT)
    last_name = sa.Column(sa.TEXT)
    gender = sa.Column(sa.TEXT)
    email = sa.Column(sa.TEXT)
    birthdate = sa.Column(sa.TEXT)
    height = sa.Column(sa.REAL)




class Athelete(Base):
    """Описывает структуру таблицы athelete для хранения регистрационных данных пользователей
    """
    __tablename__ = "athelete"

    id = sa.Column(sa.INTEGER, primary_key = True, autoincrement = True)
    birthdate = sa.Column(sa.TEXT)
    gender = sa.Column(sa.TEXT)
    height = sa.Column(sa.REAL)
    name = sa.Column(sa.TEXT)
    age = sa.Column(sa.INTEGER)
    height = sa.Column(sa.REAL)
    weight = sa.Column(sa.INTEGER)
    gold_medals = sa.Column(sa.INTEGER)
    silver_medals = sa.Column(sa.INTEGER)
    bronze_medals = sa.Column(sa.INTEGER)
    total_medals = sa.Column(sa.INTEGER)
    sport = sa.Column(sa.TEXT)
    country = sa.Column(sa.TEXT)

    def __repr__(self):
        return f' {self.name} | {self.birthdate} | {self.height}'



def connect_db():
    """Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии
    """
    # создаем соединение к БД
    engine = sa.create_engine(DB_PATH)
    # Создаем описанные таблицы
    Base.metadata.create_all(engine)
    # Создаем фабрику сессию
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()

def find_user_id(id,session):
    query = session.query(User).filter(User.id == id).first()
    return query

def find_athelete_height(user, session):
    query = session.query(Athelete).filter(Athelete.height >= user.height).order_by(Athelete.height).first()
    return query

def find_birthdate_all(user, session):
    query = session.query(Athelete).filter(Athelete.birthdate >= user.birthdate).order_by(Athelete.birthdate).first()
    return query

def main():
    """
    Осуществляет взаимодействие с пользователем, обрабатывает пользовательский ввод
    """
    session = connect_db()
    id = input("введите id пользователя: ")
    find_user = find_user_id(id, session)
    if find_user is not None:
        find_height = find_athelete_height(find_user, session)
        find_birthdate = find_birthdate_all(find_user, session)
        print("Ближайший по росту: ", find_height)
        print("Ближайший по дате рождения: ", find_birthdate)
    else:
        print("Пользователя с таким id нету")

if __name__ == "__main__":
    main()