import datetime
import dataset
import sqlite3

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
    def save_data(cls, table, data, update_keys=None):
        """
        Store data on the table that is given by params
        :param table: table where store the data
        :type table: str
        :param data: data to store on database
        :type data: dict
        :param update_keys: keys for update if the instance exists
        :type update_keys: list
        :return: None
        """
        db = dataset.connect('sqlite:///{}'.format(database))
        table = db[table]
        try:
            table.insert(data)
        except sqlite3.IntegrityError as e:
            print e
            data.pop('creation_date')
            table.update(data, update_keys)
