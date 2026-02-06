from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional

class OrderTask(BaseModel):
    id: Optional[int] = None
    city: str
    artist: str
    target_date: Optional[date] = None
    target_price: Optional[float] = None
    customer_info: Optional[str] = Field(None, description="实名人信息(姓名+身份证)")
    priority_order: Optional[str] = None
    bounty: Optional[float] = None
    contact_phone: Optional[str] = None
    status: int = 0
    created_at: Optional[datetime] = None

class Config:
    from_attributes = True

class OrderTaskCreate(BaseModel):
    city: str = Field(..., description="抢票目标城市")
    artist: str = Field(..., description="艺人或演出名称")
    target_date: Optional[date] = Field(None, description="目标演出日期")
    target_price: Optional[float] = Field(None, description="目标票价")
    customer_info: str = Field(..., description="实名人信息(姓名+身份证)")
    priority_order: Optional[str] = Field(None, description="优先顺序，如：看台优先")
    bounty: Optional[float] = Field(0.0, description="红包金额")
    contact_phone: Optional[str] = Field(None, description="联系电话")

