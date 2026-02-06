from fastapi import APIRouter
from schemas import ResponseModel, OrderTaskCreate
from repository import db_task


router = APIRouter(prefix="/tasks", tags=["抢票任务管理"])

@router.post("/create", response_model=ResponseModel)
async def create_task(task: OrderTaskCreate):
    try:
        result = db_task.create_order_task(task.model_dump())
        return ResponseModel(data=result)
    except Exception as e:
        return ResponseModel(code=500, msg=f"创建失败: {str(e)}")
    

