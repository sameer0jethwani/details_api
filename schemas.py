from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):

    name:str
    address:str
    phone_number: Optional[str]=None

class UpdateItem(BaseModel):

    name:Optional[str]=None
    address:Optional[str]=None
    phone_number: Optional[str]=None