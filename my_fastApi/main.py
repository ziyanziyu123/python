from fastapi import FastAPI, Path, Query, HTTPException, Request, Depends
import os
from fastapi.responses import HTMLResponse, FileResponse
from pathlib import Path as SysPath
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse
import time
from  sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Float, DateTime, func, select, or_

app = FastAPI()

# 加载 .env 配置
try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception:
    # 未安装 python-dotenv 时忽略（仍可用系统环境变量）
    pass

# === MySQL 异步引擎配置（使用环境变量） ===
# 请在系统环境或 .env 中设置：MYSQL_USER / MYSQL_PASSWORD / MYSQL_HOST / MYSQL_PORT / MYSQL_DB
MYSQL_USER = os.getenv("MYSQL_USER", "lcy_db")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "CWrURzm0Fw9fUwta")
MYSQL_HOST = os.getenv("MYSQL_HOST", "mysql7.sqlpub.com")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3312")
MYSQL_DB = os.getenv("MYSQL_DB", "lcy_db")

ASYNC_DATABASE_URL = (
    f"mysql+aiomysql://{MYSQL_USER}:{MYSQL_PASSWORD}"
    f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset=utf8mb4"
)

# create_async_engine 示例（请确保已安装 sqlalchemy[asyncio] 和 aiomysql）
async_engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo=True,
    pool_size=10,
    max_overflow=20,
)

# 2. 定义模型类：基类 + 表对应的模型类
# 基类：创建时间、更新时间、书籍表：id、书名、作者、价格、出版社
class Base(DeclarativeBase):
    create_time: Mapped[DateTime] = mapped_column(
        DateTime, insert_default=func.now(), default=func.now(), comment="创建时间"
    )
    update_time: Mapped[DateTime] = mapped_column(
        DateTime,
        insert_default=func.now(),
        default=func.now(),
        onupdate=func.now(),
        comment="更新时间",
    )


class Book(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True, comment="书籍id")
    bookname: Mapped[str] = mapped_column(String(255), comment="书名")
    author: Mapped[str] = mapped_column(String(255), comment="作者")
    price: Mapped[float] = mapped_column(Float, comment="价格")
    publisher: Mapped[str] = mapped_column(String(255), comment="出版社")

# 请求体：新增书籍（与截图一致）
class BookBase(BaseModel):
    id: int
    bookname: str
    author: str
    price: float
    publisher: str

class BookUpdate(BaseModel):
    bookname: str
    author: str
    price: float
    publisher: str

# 3. 建表：定义创建表函数 -> FastAPI 启动时调用
async def create_tables():
    # 获取异步引擎，创建事务 -> 建表
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)  # Base 模型类的元数据创建


@app.on_event("startup")
async def startup_event():
    await create_tables()

# AsyncSessionLocal：异步会话工厂（依赖注入使用）
AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,  # 绑定数据库引擎
    class_=AsyncSession,  # 指定会话类
    expire_on_commit=False,  # 提交后不失效，避免再次查询数据库
)


# 依赖项
async def get_database():
    async with AsyncSessionLocal() as session:
        try:
            yield session  # 依赖注入给路由处理函数
            await session.commit()  # 提交事务
        except Exception:
            await session.rollback()  # 有异常，回滚
            raise
        finally:
            await session.close()  # 关闭会话

# 查询示例：查找书籍列表
@app.get("/book/books")
async def get_book_list(db: AsyncSession = Depends(get_database)):
    result = await db.execute(select(Book))
    # book = result.scalars().all() # 获取所有结果
    # book = result.scalars().first()  # 获取第一个结果
    book = await db.get(Book, 2)  # 根据主键查询
    return book


# 需求：路径参数 -> 书籍id
@app.get("/book/get_book/{book_id}")
async def get_book_list(book_id: int, db: AsyncSession = Depends(get_database)):
    result = await db.execute(select(Book).where(Book.id == book_id))
    book = result.scalar_one_or_none()
    return book

# 需求：条件 价格大于等于70
@app.get("/book/search_book")
async def get_search_book(db: AsyncSession = Depends(get_database)):
    result = await db.execute(select(Book).where(Book.price >= 70))
    books = result.scalars().all()
    return books

# 需求：模糊查询（书名包含关键字）
@app.get("/book/search_book_like")
async def get_search_book_like(
    keyword: str,
    min_price: float = 0,
    db: AsyncSession = Depends(get_database),
):
    result = await db.execute(
        select(Book).where(
            or_(
                Book.bookname.like(f"%{keyword}%"),
                Book.author.like(f"%{keyword}%"),
            ),
            Book.price >= min_price,
        )
    )
    books = result.scalars().all()
    return books

# 需求：聚合查询（按出版社统计数量与平均价格）
@app.get("/book/aggregate")
async def get_book_aggregate(db: AsyncSession = Depends(get_database)):
    result = await db.execute(
        select(
            Book.publisher,
            func.count(Book.id).label("count"),
            func.avg(Book.price).label("avg_price"),
        ).group_by(Book.publisher)
    )
    rows = result.all()
    return [
        {"publisher": r.publisher, "count": r.count, "avg_price": float(r.avg_price or 0)}
        for r in rows
    ]

# 需求：分页查询
@app.get("/book/get_book_list")
async def get_book_list(
    page: int = 1,
    page_size: int = 3,
    db: AsyncSession = Depends(get_database),
):
    # (页码 - 1) * 每页数量
    skip = (page - 1) * page_size
    stmt = select(Book).offset(skip).limit(page_size)
    result = await db.execute(stmt)
    books = result.scalars().all()
    return books


# 新增数据（与截图一致）
@app.post("/book/add_book")
async def add_book(book: BookBase, db: AsyncSession = Depends(get_database)):
    book_obj = Book(**book.__dict__)
    db.add(book_obj)
    # await db.commit()
    # 提交由 get_database() 统一处理，这里无需手动 commit
    return book


# 需求：修改图书信息：先查再改
# 设计思路：路径参数书籍id；作用是主键；请求体参数：作用是更新数据（书名、作者、价格、出版社）
@app.put("/book/update_book/{book_id}")
async def update_book(book_id: int, data: BookUpdate, db: AsyncSession = Depends(get_database)):
    db_book = await db.get(Book, book_id)
    if db_book is None:
        raise HTTPException(
            status_code=404,
            detail="暂无此书",
        )

    # 重新赋值
    db_book.bookname = data.bookname
    db_book.author = data.author
    db_book.price = data.price
    db_book.publisher = data.publisher

    # await db.commit()
    # 提交由 get_database() 统一处理，这里无需手动 commit
    return db_book


# 需求：删除图书
@app.delete("/book/delete_book/{book_id}")
async def delete_book(book_id: int, db: AsyncSession = Depends(get_database)):
    # 先查再删
    db_book = await db.get(Book, book_id)
    if db_book is None:
        raise HTTPException(
            status_code=404,
            detail="暂无此书",
        )

    await db.delete(db_book)
    # await db.commit()
    # 提交由 get_database() 统一处理，这里无需手动 commit
    return {"msg": "删除图书成功"}


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
