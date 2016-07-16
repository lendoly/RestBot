import datetime
import sqlite3
import logging

from settings import database


class DateCreationModelMixin(object):
    """An abstract model for creation date.
    This mixin add a field to the model creation_date, which contains the
    object creation datetime.
    Note: django metaclass for models requires that the inherited class must be
    a subclass of models.Model in order to create the stored fields declared
    in that class.
    Attributes:
        creation_date: A datetime that automatically stores the datetime
            of the object creation.
    """
    creation_date = None

    def __init__(self):
        self.creation_date = datetime.datetime.now()


class DateModificationModelMixin(DateCreationModelMixin):
    """An abstract model for modification date.
    This mixin add two fields (one is inherited from DateCreationModelMixin)
    to the models subsclassing it, creation_date and modification_date, which
    store datetime when the object was created or updated, respectively.
    Note: django metaclass for models requires that the inherited class must be
    a subclass of models.Model in order to create the stored fields declared
    in that class.
    Attributes:
        creation_date: A datetime that automatically stores the datetime
            of the object creation.
        modification_date: A datetime that automatically stores the datetime
            of the object creation.
    """
    modification_date = None

    def __init__(self):
        super(DateModificationModelMixin, self).__init__()
        self.modification_date = datetime.datetime.now()


class DataBaseConnection(object):
    """
    Wrapper fo connexion to Database with sqlite3
    """

    @classmethod
    def execute_create_query(cls, query):
        conn = sqlite3.connect(database)
        c = conn.cursor()
        try:
            c.execute(query)
            conn.commit()
        except sqlite3.OperationalError as e:
            logging.warning(e.message)
        conn.close()

    @classmethod
    def execute_save_query(cls, query, data):
        conn = sqlite3.connect(database)
        c = conn.cursor()
        try:
            c.execute(query, data)
            conn.commit()
        except BaseException as e:
            conn.close()
            raise

