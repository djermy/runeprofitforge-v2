from sqlmodel import Field, SQLModel

class Item(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    members: bool = Field(index=True)
    description: str
    type: str = Field(index=True)
    type_icon: str
    icon: str
    icon_large: str
    current: dict = Field(index=True)
    today: dict = Field(index=True)