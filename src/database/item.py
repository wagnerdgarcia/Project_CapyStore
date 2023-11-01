class ItemDB:
    def __init__(self):
        self.itens = []

    def create(self, item_data):
        item_id = len(self.itens) + 1
        item_data['id'] = item_id
        self.itens.append(item_data)
        return item_data

    def get(self, item_id: int):
        for item in self.itens:
            if item['id'] == item_id:
                return item
        return None

    def getAll(self):
        return self.itens
    
    def update(self, item_id: int, item_data):
        for item in self.itens:
            if item['id'] == item_id:
                self.itens[item_id]= item_data
                return self.itens[item_id]
        return None

    def delete(self, item_id: int):
        return None