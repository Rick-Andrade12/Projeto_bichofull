from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "mysql+pymysql://root@127.0.0.1:3307/bicho_full2"

banco = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=banco)


Base = declarative_base()