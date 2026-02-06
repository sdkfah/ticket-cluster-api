from fastapi import APIRouter
from schemas import ResponseModel, OrderTaskCreate
from repository import db_task
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/tasks", tags=["抢票任务管理"])

@router.post("/create", response_model=ResponseModel)
async def create_task(task: OrderTaskCreate):
    try:
        result = db_task.create_task(task.model_dump())
        return ResponseModel(data=result)
    except Exception as e:
        logger.exception("创建任务时发生系统异常: %s", str(e))

        return ResponseModel(code=500, msg="服务器内部错误，请稍后重试")
    

