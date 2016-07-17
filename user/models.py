from util.models import DateModificationModelMixin, DataBaseConnection


class User(DateModificationModelMixin):
    first_name = None
    last_name = None
    username = None
    id = None
    _table = 'user'

    def __init__(self, first_name, last_name, username, id_user):
        super(User, self).__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.id = id_user

    @property
    def to_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'id': self.id,
            'modification_date': self.modification_date,
            'creation_date': self.creation_date,
        }

    @property
    def table(self):
        return self._table

    @property
    def update_keys(self):
        return ['id']

    def save(self):
        DataBaseConnection.save_data(self.table, self.to_dict, self.update_keys)
