from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # 导入 CORS 中间件
from api import v1_device, v1_task, v1_log,v1_inventory

app = FastAPI(title="Ticket Cluster System")

# 定义允许访问的前端源
origins = [
    "http://localhost:5173",    # 你的 Vite 前端默认地址
    "http://127.0.0.1:5173",
]

# 配置中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # 允许跨域的源列表
    allow_credentials=True,          # 允许携带 Cookie
    allow_methods=["*"],             # 允许所有的请求方法 (GET, POST, PUT, DELETE 等)
    allow_headers=["*"],             # 允许所有的请求头
)


# 像拼积木一样把各模块插入
app.include_router(v1_device.router, prefix="/api/v1")
app.include_router(v1_task.router, prefix="/api/v1")
app.include_router(v1_log.router, prefix="/api/v1")

app.include_router(v1_inventory.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"status": "running", "service": "Ticket Cluster API"}