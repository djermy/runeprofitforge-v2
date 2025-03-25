import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine
from .substores.grand_exchange_store import Grand_Exchange_Store

load_dotenv()

class Store:
    def __init__(self):
        self.db_url = os.getenv("DB_URL")
        self.conn = create_engine(self.db_url, echo=True)
        
        # substores
        self.grand_exchange_store = Grand_Exchange_Store(self.conn)

    def create_db_and_tables(self):
        SQLModel.metadata.create_all(self.conn)

store = Store()