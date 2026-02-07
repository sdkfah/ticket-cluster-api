from fastapi import FastAPI, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware  # 导入 CORS 中间件
from api import v1_device, v1_task, v1_ticket
import logging
from schemas import ResponseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

app.include_router(v1_ticket.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"status": "running", "service": "Ticket Cluster API"}


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.warning("HTTPException: %s %s", exc.status_code, exc.detail)
    payload = ResponseModel(code=exc.status_code or 400, msg=str(exc.detail)).model_dump()
    return JSONResponse(status_code=exc.status_code or 400, content=payload)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.warning("Request validation error: %s", exc)
    payload = ResponseModel(code=422, msg="参数校验失败", data=exc.errors()).model_dump()
    return JSONResponse(status_code=422, content=payload)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled exception: %s", exc)
    payload = ResponseModel(code=500, msg="服务器内部错误，请稍后重试").model_dump()
    return JSONResponse(status_code=500, content=payload)