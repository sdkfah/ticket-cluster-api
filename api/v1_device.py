from fastapi import APIRouter, HTTPException
from schemas import ResponseModel, Device, GroupCreate, MigrateRequest
from repository import db_device

router = APIRouter(prefix="/devices", tags=["设备与分组管理"])

