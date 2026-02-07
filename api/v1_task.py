from fastapi import APIRouter
from schemas import ResponseModel, OrderTaskCreate
from repository import db_task
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/tasks", tags=["抢票任务管理"])

@router.post("/create", response_model=ResponseModel)
async def create_task(task: OrderTaskCreate):
    result = db_task.create_task(task.model_dump())
    return ResponseModel(data=result)
    

@router.get("/list", response_model=ResponseModel)
async def list_tasks():
    """获取所有抢票任务列表"""
    data = db_task.get_all_tasks()
    return ResponseModel(data=data)


@router.delete("/{task_id}", response_model=ResponseModel)
async def delete_task(task_id: int):
    """删除指定抢票任务（按 ID）"""
    res = db_task.delete_task(task_id)
    affected = 0
    if isinstance(res, dict):
        affected = res.get("affected", 0)
    if affected > 0:
        return ResponseModel(msg="任务已删除")
    return ResponseModel(code=404, msg="未找到该任务或已删除")


