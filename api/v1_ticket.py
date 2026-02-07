from fastapi import APIRouter, Query
from schemas import ResponseModel
from repository import db_ticket

router = APIRouter(prefix="/ticket", tags=["票档管理"])

@router.get("/search", response_model=ResponseModel)
async def search_projects(keyword: str = Query(..., description="演出关键字")):
    """搜索去重后的项目列表"""
    data = db_ticket.search_projects(keyword)
    return ResponseModel(data=data)

@router.get("/skus", response_model=ResponseModel)
async def get_skus(item_id: str = Query(..., description="项目ID")):
    """获取该项目下的所有 SKU (场次+票价)"""
    data = db_ticket.get_details_by_item(item_id)
    return ResponseModel(data=data)

@router.get("/list", response_model=ResponseModel)
async def list_ticket():
    """获取所有原始票档列表"""
    data = db_ticket.get_all_items()
    return ResponseModel(data=data)