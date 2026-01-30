class User:
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name
        self.activity_rentals = []
        
    def to_dict(self):
        return {
            "id": self.user_id,
            "name": self.name,
            "activity_rentals": self.activity_rentals
        }
        
    @staticmethod
    def from_dict(data: dict):
        user = User(data["id"], data["name"])
        user.activity_rentals = data.get("activity_rentals", [])
        return user
