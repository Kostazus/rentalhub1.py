from models.user import User
from exceptions import UserNotFoundError

class UserManadger:
    def __init__(self, storage):
        self.storage = storage
        
    def create_user(self, user_id, name):
        users = self.storage.load()
        user = User(user_id, name)
        users.append(user.to_dict())
        self.storage.save(users)
        
    def get_user(self, user_id):
        users = self.storage.load()
        for i in users:
            if i["id"] == user_id:
                return User.from_dict(i)
        raise UserNotFoundError('Пользователь не найден!')
    
    def show_users(self):
        return self.storage.load()
    
