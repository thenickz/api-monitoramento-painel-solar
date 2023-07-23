from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from os import getenv




class DBConnectionHandler:



    def __init__(self) -> None:
        load_dotenv()
        USER = getenv('USER')
        PW = getenv('PW')
        HOST = getenv('HOST')
        PORT = getenv('PORT') # MUST BE INT
        DB = getenv('DB')
        print(USER, PW, HOST, PORT, DB)
        self.__connection_string = 'mysql+pymysql://root:lkjasd@localhost:3306/aprendendo'
        #self.__connection_string = f'mysql+pymysql://{USER}:{PW}@{HOST}:{PORT}/{DB}'
        self.__engine = self.__create_database_engine()
        self.session = None


    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine


    def get_engine(self):
        return self.__engine


    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
    

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
