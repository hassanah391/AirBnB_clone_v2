#!/usr/bin/python3
"Database storage"

from sqlalchemy import create_engine
from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class_dict = {
    'User': User,
    'State': State,
    'City': City,
    'Review': Review,
    'Amenity': Amenity,
    'Place': Place
}


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
        """Initialize database connection"""
        username = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db_name = getenv("HBNB_MYSQL_DB")
        envv = getenv("HBNB_ENV", "none")

        self.__engine = create_engine(
            f"mysql+mysqldb://{username}:{password}@{host}/{db_name}",
            pool_pre_ping=True
        )
        if envv == "test":
            Base.metadata.drop_all(self.__engine)

        Session = sessionmaker(bind=self.__engine)
        self.__session = scoped_session(Session)

    def all(self, cls=None):
        '''
            Query current database session
        '''
        db_dict = {}

        if cls != "":
            objs = self.__session.query(models.class_dict[cls]).all()
            for obj in objs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                db_dict[key] = obj
            return db_dict
        else:
            for k, v in models.class_dict.items():
                if k != "BaseModel":
                    objs = self.__session.query(v).all()
                    if len(objs) > 0:
                        for obj in objs:
                            key = "{}.{}".format(obj.__class__.__name__,
                                                 obj.id)
                            db_dict[key] = obj
            return db_dict

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
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes the current SQLAlchemy session.

        This method removes the current SQLAlchemy session, ensuring that
        all pending transactions are either committed or rolled back and
        the session is properly closed.
        Then creates a new session for the next operations.
        """
        self.__session.remove()
