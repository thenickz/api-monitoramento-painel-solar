from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from infra.connection import DBConnectionHandler
from datetime import datetime
from pytz import timezone


Base = declarative_base()


# get the datetime moment
def dt_moment():
    return str(datetime.now(tz=timezone('America/Sao_Paulo')))


# painel_solar_data's table class
class Solar_Panel_Data(Base):
    __tablename__ = 'painel_solar_data'

    # Columns and Columns Configs
    # ATTENTION: Column name in SQL is not case sensitive, all table names must be the same
    id = Column(Integer, primary_key=True)
    datetime = Column(String)
    current = Column(Float)
    irradiance = Column(Float)
    

    # insert data
    def insert(self):
        with DBConnectionHandler() as db:
            try:
                db.session.add(self)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    
    # makes class printable (single line)
    def __repr__(self):
        return f'\
            Painel_Solar_Data[\
            id={self.id},\
            date_time={self.datetime},\
            current={self.current},\
            irradiance={self.irradiance}]'
    
    
    # class str() method  (single line)
    def __str__(self):
        return {'Painel_Solar_Data': 
                    {'id':self.id,
                     'date':self.datetime,
                     'current':self.current,
                     'irradiance':self.irradiance
                    }
                }
