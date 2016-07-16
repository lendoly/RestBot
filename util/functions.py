from user.models import User


def initialize_database():
    User.create_table()
