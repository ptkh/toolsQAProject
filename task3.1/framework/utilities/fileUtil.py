from framework.models.userModel import User
import os.path
import json


class JsonUtil:

    @staticmethod
    def load_data(filepath):
        with open(os.path.join(filepath), 'r') as f:
            data = json.load(f)
        return data

    @classmethod
    def load_users(cls, filepath):
        users = []
        for user in cls.load_data(filepath):
            users.append(User(f_name=user['f_name'],
                              l_name=user['l_name'],
                              email=user['email'],
                              age=user['age'],
                              salary=user['salary'],
                              dept=user['dept']))
        return users
