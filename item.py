class Item:
    def __init__(self, item_id: str, name: str, category: str, price: float):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.price = price
        self.is_available = True
        
    def ti_dict(self):
        return {
            "item_id": self.item_id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "is_available": self.is_available
        }
    
    @staticmethod
    def from_dict(data: dict):
        item = Item(
            data["id"],
            data["name"],
            data["category"],
            data["price_per_day"]
        )
        item.is_available = data.get("is_available", True)
        return item
    
    
