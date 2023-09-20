#!/usr/bin/python3
"""This is the db storage file"""

from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, scoped_session
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.user import User
from models.review import Review


class DBStorage():
    """This is the database storage class"""

    __engine = None
    __session = None

    def __init__(self):
        """This is the constructor"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB")
        ), pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """This is used to query from the data base"""
        objects = []
        model_names = [State, City, User]
        if cls is None:
            for i in model_names:
                if inspect(self.__engine).has_table(i.__tablename__):
                    objects.extend(self.__session.query(i).all())
        else:
            if type(cls) == str:
                try:
                    cls = eval(cls)
                except Exception:
                    pass
            objects = self.__session.query(cls).all()
        return {f"{type(i).__name__}.{i.id}": i for i in objects}

    def new(self, obj):
        """This adds obj to the database session"""
        self.__session.merge(obj)

    def save(self):
        """Save the session objects to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes obj"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """refreshes the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
