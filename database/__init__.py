from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Ссылка к базе данных
# SQLALCHEMY_DATABASE_URI = "sqlite:///data.db"
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@database/postgres"

# Продлючние к базе
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# Соединение с базой
SessionLocal = sessionmaker(bind=engine)

# Класс для наследования
Base = declarative_base()

# Импорт всех моделей
from database import models

# Генератор соединения с базой
def get_db():
    bd = SessionLocal()
    try:
        yield bd
    except Exception:
        bd.rollback()
        raise
    finally:
        bd.close()


