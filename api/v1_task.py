from fastapi import APIRouter
from schemas import ResponseModel, OrderTaskCreate
from repository import db_task


router = APIRouter(prefix="/tasks", tags=["抢票任务管理"])

@router.post("/create", response_model=ResponseModel)
async def create_task(task: OrderTaskCreate):
    """创建抢票订单任务"""
    try:
        # 使用 db_task 实例
        result = db_task.create_order_task(task.model_dump())
        return ResponseModel(data=result)
    except Exception as e:
        # 处理 uk_artist_customer 唯一索引冲突等异常
        return ResponseModel(code=500, msg=f"创建失败: {str(e)}")
    

 # --- 为 Dashboard 增加的新接口 ---

@router.get("/list", response_model=ResponseModel)
async def list_tasks():
    """管理后台获取所有任务列表"""
    # 假设你的 db_task 里有 get_all 这种方法
    tasks = db_task.get_all_tasks() 
    return ResponseModel(data=tasks)   

@router.post("/{task_id}/start", response_model=ResponseModel)
async def start_task(task_id: int):
    """启动任务"""
    # 这里的 1 代表启动状态，根据你数据库的定义来
    db_task.update_task_status(task_id, status=1) 
    return ResponseModel(msg="任务已启动")

@router.post("/{task_id}/stop", response_model=ResponseModel)
async def stop_task(task_id: int):
    """停止任务"""
    # 这里的 0 代表停止状态
    db_task.update_task_status(task_id, status=0) 
    return ResponseModel(msg="任务已停止")
