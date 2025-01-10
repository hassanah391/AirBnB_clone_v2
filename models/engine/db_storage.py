#!/usr/bin/python3
"Database storage"

from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models import class_dict
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage:
    """
    DBStorage class for interacting with the MySQL database using SQLAlchemy.

    Attributes:
        __engine (sqlalchemy.engine.Engine): The SQLAlchemy engine.
        __session (sqlalchemy.orm.scoped_session): The SQLAlchemy session.
    """
    __engine = None
    __session = None
    
    def __init__(self):
        """
        Initializes the DBStorage instance.

        Sets up the SQLAlchemy engine and session. If the environment variable
        'HBNB_ENV' is set to 'test', it drops all tables in the database.

        Environment Variables:
            HBNB_MYSQL_USER (str): MySQL username.
            HBNB_MYSQL_PWD (str): MySQL password.
            HBNB_MYSQL_HOST (str): MySQL host.
            HBNB_MYSQL_DB (str): MySQL database name.
            HBNB_ENV (str): Environment type (e.g., 'test').
        """
        username = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db_name = getenv("HBNB_MYSQL_DB")
        envv = getenv("HBNB_ENV", "none")

        self.__engine = create_engine(f"mysql+mysqldb://{username}:\
            {password}@{host}/{db_name}", pool_pre_ping=True)
        
        if envv == "test":
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        '''
            query all types of objects
            or a specific class objects
            on the current database session
        '''
        db_dic = {}
        if cls != "":
            objs = self.__session.query(class_dict).all()
            for obj in objs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                db_dic[key] = obj
            return db_dic
        else:
            for k, v in class_dict.items():
                if k != "BaseModel":
                    objs = self.__session.query(v).all()
                    if len(objs) > 0:
                        for obj in objs:
                            key = "{}.{}".format(obj.__class__.__name__,
                                                 obj.id)
                            db_dic[key] = obj
            return db_dic

    def new(self, obj):
        """
        Add object to current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete obj from the current database session if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database and initialize a new session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
