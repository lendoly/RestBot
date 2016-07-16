from Utils.models import DateModificationModelMixin, DataBaseConnection


class User(DateModificationModelMixin):
    first_name = None
    last_name = None
    username = None
    id = None

    def __init__(self, first_name, last_name, username, id_user):
        super(User, self).__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.id = id_user

    @classmethod
    def create_table(cls):
        query = '''CREATE TABLE User(first_name text, last_name text, username text unique, id real primary key,
                                     creation_date date, modification_date date)'''
        DataBaseConnection.execute_create_query(query)

    def save(self):
        query = '''INSERT INTO User VALUES (?, ?, ?, ?, ?, ?)'''
        data = (self.first_name, self.last_name, self.username, self.id, self.creation_date, self.creation_date)
        DataBaseConnection.execute_save_query(query, data)

    def update(self):
        query = '''UPDATE User
                   SET first_name=:first_name, last_name=:last_name, username=:username, id=:id,
                   modification_date=:modification_date
                   WHERE id =:id
                '''
        data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "id": self.id,
            "modification_date": self.modification_date
        }
        DataBaseConnection.execute_save_query(query, data)


