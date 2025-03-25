from backend.models.grand_exchange import Item
from sqlmodel import Session, select

class Grand_Exchange_Store:
    def __init__(self, conn):
        self.conn = conn

    def create(self, item: Item):
        with Session(self.conn) as session:
            session.add(item) 
            session.commit()
            session.refresh(item)

        return [{"message": "item created!"}, item.dict()]

    def get(self, id: int):
        with Session(self.conn) as session:
            query = select(Item).where(Item.id == id)
            response = session.exec(query)
            return response.first()
    
    def get_all(self):
        with Session(self.conn) as session:
            query = select(Item)
            response = session.exec(query)
            items = []
            for item in response:
                items.append(item)

        return items
    
    def update(self, id: int, updated_item: Item):
        with Session(self.conn) as session:
            query = select(Item).where(Item.id == id)
            response = session.exec(query)
            item = response.one()

            for key, value in updated_item.dict().items():
                if key == "id":
                    continue
                setattr(item, key, value)

            session.add(item)
            session.commit()
            session.refresh(item)
            return [{"message": "item updated!"}, item.dict()]


def delete(self, id: int):
        with Session(self.conn) as session:
            query = select(Item).where(Item.id == id)
            response = session.exec(query)
            Item = response.one()
            
            session.delete(recipe)
            session.commit()    
            return [{"message": "item successfully deleted!"}, item.dict()]