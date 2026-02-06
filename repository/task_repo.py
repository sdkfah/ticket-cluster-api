from .base_repo import BaseRepository
from loguru import logger


class TaskRepository(BaseRepository):
    def __init__(self, mapper_dir):
        super().__init__(mapper_dir)

    def get_all_tasks(self):
        """
        管理后台获取所有任务列表
        """
        return self.execute("task_mapper", "get_all_tasks", {})
    
    def update_task_status(self, task_id: int, status: int):
        """
        更新任务状态 (例如: 1-成功, 2-失败)
        """
        task_data = {
            "id": task_id,
            "status": status
        }
        return self.execute("task_mapper", "update_task_status", task_data)
 


    def create_order_task(self, task_data: dict):
        """
        创建抢票订单任务
        :param task_data: 包含表结构的字典数据
        """
        return self.execute("task_mapper", "create_order_task", task_data)
