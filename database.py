from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# SQLALCHEMY_DATABASE_URL = "sqlite:///todosapp.db"
# engine = create_engine(SQLALCHEMY_DATABASE_URL,  connect_args={"check_same_thread": False})

SQLALCHEMY_DATABASE_URL = 'postgresql://production_database_iwj2_user:GdmlR3O6znJSOA0lvfc8JChSsA7JoVXq@dpg-daplc0gu01pc73d25il0-a/production_database_iwj2'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:ryu1234@127.0.0.1:3306/todoapplicationdatabase'
# engine = create_engine(SQLALCHEMY_DATABASE_URL)



SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()







