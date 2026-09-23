from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# SQLALCHEMY_DATABASE_URL = "sqlite:///todosapp.db"
# engine = create_engine(SQLALCHEMY_DATABASE_URL,  connect_args={"check_same_thread": False})

SQLALCHEMY_DATABASE_URL = 'postgresql://prod_db_fastapi_user:TXtW5CcCQfaX2f23gsoBsdZsuIp3r5Rb@dpg-dapqa7mgekts73eqmar0-a/prod_db_fastapi'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:ryu1234@127.0.0.1:3306/todoapplicationdatabase'
# engine = create_engine(SQLALCHEMY_DATABASE_URL)



SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()







