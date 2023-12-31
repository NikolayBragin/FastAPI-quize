from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey

from sqlalchemy.orm import relationship     # отношения между таблицами

from database import Base

# Таблица пользователей
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    phone_number = Column(String)

    reg_date = Column(DateTime)

# Таблица вопросов
class Question(Base):
    __tablename__ = 'Questions'
    id = Column(Integer, autoincrement=True, primary_key=True)
    q_text = Column(String, nullable=False)
    answer = Column(Integer, nullable=False)
    v1 = Column(String, nullable=False)
    v2 = Column(String, nullable=False)
    v3 = Column(String, nullable=True)
    v4 = Column(String, nullable=True)

    reg_date = Column(DateTime)

# Таблица ответов пользователей
class UserAnswer(Base):
    __tablename__ = 'user_answers'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))   # нужно связать с таблицей users
    question_id = Column(Integer, ForeignKey('Questions.id'))
    user_answer = Column(Integer)
    correctness = Column(Boolean)

    answer_date = Column(DateTime)

    users_kf = relationship(User)   # перемеенная шпион, дающая доступ ко всем колонкам класса User (имя, номер телефона, дата регстрации)
    question_kf = relationship(Question)


# Таблица подсчета очков пользователя
class Rating(Base):
    __tablename__ = 'ratings'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    user_score = Column(Integer, default=0)

    user_fk = relationship(User)

