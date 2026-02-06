from .base_repo import BaseRepository
from loguru import logger
from typing import List, Dict

class TicketRepository(BaseRepository):
    def __init__(self, mapper_dir):
        super().__init__(mapper_dir)

    def upsert_ticket_items(self, items: List[Dict]):
        success_count = 0
        for item in items:
            try:
                self.execute("ticket_mapper", "upsert_ticket_item", item)
                success_count += 1
            except Exception as e:
                logger.error(f"SKU {item.get('sku_id')} 更新失败: {e}")
        return success_count
    
    def get_all_items(self):
        """获取所有票档信息"""
        return self.execute("ticket_mapper", "get_all_ticket_items")
    
    def search_projects(self, keyword):
        """用于下拉搜索演出列表"""
        return self.execute("ticket_mapper", "search_projects", {"keyword": keyword})

    def get_details_by_item(self, item_id):
        """获取选定演出的所有日期和票档"""
        return self.execute("ticket_mapper", "get_project_details", {"item_id": item_id})