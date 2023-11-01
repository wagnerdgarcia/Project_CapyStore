from src.database.item import ItemDB

class ItemService:
    def __init__(self):
        self.item_db = ItemDB()

    def create(self, item_data):
        return self.item_db.create(item_data)

    def get(self, item_id: int):
        return self.item_db.get(item_id)
    
    def getAll(self):
        return self.item_db.getAll()

    def update(self, item_id: int, item_data):
        return self.item_db.update(item_id, item_data)
    
    def delete(self, item_id: int):
        return self.item_db.delete(item_id)