from src.services.item import ItemService

class ItemController:
    def __init__(self):
        self.item_service = ItemService()

    def create(self, item_data):
        return self.item_service.create(item_data)

    def get(self, item_id: int):
        return self.item_service.get(item_id)
    
    def getAll(self):
        itens = self.item_service.getAll()
        print({itens})
        return itens

    def update(self, item_id: int, item_data):
        return self.item_service.update(item_id, item_data)
    
    def delete(self, item_id: int):
        return self.item_service.delete(item_id)