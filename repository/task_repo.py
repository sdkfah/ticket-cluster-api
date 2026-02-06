from .base_repo import BaseRepository
from loguru import logger

class TaskRepository(BaseRepository):
    def __init__(self, mapper_dir):
        super().__init__(mapper_dir)

    def get_all_tasks(self):
        return self.execute("task_mapper", "get_all_tasks", {})
    
    def update_task_status(self, task_id: int, status: int):
        task_data = {
            "id": task_id,
            "status": status
        }
        return self.execute("task_mapper", "update_task_status", task_data)
 
    def create_order_task(self, task_data: dict):
        return self.execute("task_mapper", "create_order_task", task_data)

   