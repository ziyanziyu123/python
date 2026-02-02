from fastapi import FastAPI, Path, Query, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse, FileResponse
from pathlib import Path as SysPath
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse
import time

app = FastAPI()

# 中间件示例：演示多个中间件的执行顺序（与截图一致）
@app.middleware("http")
async def middleware2(request: Request, call_next):
    print("中间件2 start")
    response = await call_next(request)
    print("中间件2 end")
    return response


@app.middleware("http")
async def middleware1(request: Request, call_next):
    print("中间件1 start")
    response = await call_next(request)
    print("中间件1 end")
    return response

@app.get("/")
def read_root():
    return {"hello": "world222"}

# 我的第一个api路由
@app.get("/hello")
async def hello():
    return {"message": "Hello, FastAPI!"}   

@app.get("/user/hello")
async def user_hello():
    return {"message": "Hello, User!"}  

@app.get("/book/{id}")
async def get_book(id: int = Path(..., title="The ID of the book to retrieve", ge=1)):
    return {"book_id": id, "title": f"Book {id} Title"}

# Path 参数示例：限制长度、设置描述和示例
@app.get("/items/{item_id:int}")
async def get_item(
    item_id: int = Path(
        ...,
        title="Item ID",
        description="Item identifier, must be >= 1",
        ge=1,
        examples={"default": {"value": 100}},
    )
):
    return {"item_id": item_id}

# Query 参数示例：分页与关键字搜索
@app.get("/search")
async def search_items(
    q: str = Query(..., min_length=1, max_length=50, description="Search keyword"),
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(10, ge=1, le=100, description="Page size"),
):
    return {"q": q, "page": page, "size": size}


# 请求体示例：创建数据
class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Item name")
    price: float = Field(..., gt=0, description="Item price, must be > 0")
    in_stock: bool = Field(True, description="Is the item in stock")


# 响应模型示例：自定义返回数据结构
class ItemOut(BaseModel):
    id: int
    name: str
    price: float


@app.post("/items")
async def create_item(item: ItemCreate):
    return {"item": item}


@app.get("/items/detail/{item_id}", response_model=ItemOut)
async def get_item_by_id(item_id: int):
    return {"id": item_id, "name": f"Item {item_id}", "price": 9.9}


# 指定响应类型示例：返回 HTML
@app.get("/html", response_class=HTMLResponse)
async def read_html():
    return "<h1>Hello, FastAPI (HTML)</h1>"


# 响应文件示例：返回图片
@app.get("/image")
async def get_image():
    img_path = SysPath(__file__).parent / "images" / "img-2026-01-31-11-07-10.png"
    return FileResponse(img_path)


# 异常处理示例：自定义异常与统一响应
class ItemNotFoundError(Exception):
    def __init__(self, item_id: int):
        self.item_id = item_id


@app.exception_handler(ItemNotFoundError)
async def item_not_found_handler(request: Request, exc: ItemNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"code": "ITEM_NOT_FOUND", "message": f"Item {exc.item_id} not found"},
    )


@app.get("/items/error/{item_id}")
async def get_item_or_404(item_id: int):
    if item_id == 0:
        # 方式 1：直接抛出 HTTPException
        raise HTTPException(status_code=400, detail="item_id must be greater than 0")
    if item_id > 1000:
        # 方式 2：抛出自定义异常，走统一异常处理
        raise ItemNotFoundError(item_id)
    return {"item_id": item_id}


# 依赖注入示例：公共参数与简单校验
def common_params(
    q: str | None = None,
    limit: int = Query(10, ge=1, le=100),
):
    return {"q": q, "limit": limit}


@app.get("/items/dep")
async def read_items_dep(params: dict = Depends(common_params)):
    return {"params": params}
