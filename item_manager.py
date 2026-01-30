from models.item import Item
from exceptions import ItemNotFoundError

class ItemManadger:
    def __init__(self, storage):
        self.storage = storage
        
    def add_item(self, item_id, name):
        items = self.storage.load()
        item = Item(item_id, name)
        items.append(item.to_dict())
        self.storage.save(items)
        
    def get_item(self, item_id):
        items = self.storage.load()
        for i in items:
            if i['id'] == item_id:
                return Item.from_dict(i)
        raise ItemNotFoundError("Такого товара не найдено!")
    
    def show_items(self):
        return self.storage.load()
    
    def update_item(self, item):
        items = self.storage.load()
        for i in items:
            if i["id"] == item.item_id:
                i.update(item.to_dict())
        self.storage.save(items)
        
        
