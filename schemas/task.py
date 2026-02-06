from pydantic import BaseModel, Field


class Config:
    from_attributes = True

class OrderTaskCreate(BaseModel):
    item_id: str  
    sku_id: str
    artist: str
    city: str
    target_date: str
    target_price: str
    customer_info: str
    contact_phone: str
    bounty: float

