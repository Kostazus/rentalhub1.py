class Rental:
    def __init__(self, rental_id, user_id, item_id, days, total_price):
        self.rental_id = rental_id
        self.user_id = user_id
        self.item_id = item_id
        self.days = days
        self.total_price = total_price
        self.status = 'Active'
        
    def to_dict(self):
        return {
            "rental_id": self.rental_id,
            "user_id": self.user_id,
            "item_id": self.item_id,
            "days": self.days,
            "total_price": self.total_price,
            "status": self.status
        }
        
    def from_dict(data: dict):
        rental = Rental(
            data["rental_id"],
            data["user_id"],
            data["item_id"],
            data["days"],
            data["total_price"]
        )
        rental.status = data.get("status", "active")
        return rental
