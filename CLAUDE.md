# Python FastAPI 学习项目

## 项目概述

这是一个 FastAPI 学习项目，主要用于学习和实践 FastAPI 框架及相关技术栈。

**主要技术栈：**
- FastAPI 0.128.0 - 现代化的 Python Web 框架
- SQLAlchemy 2.0.46 - ORM 框架（支持异步）
- aiomysql 0.3.2 - 异步 MySQL 驱动
- Pydantic 2.12.5 - 数据验证
- Uvicorn 0.40.0 - ASGI 服务器

## Python 环境配置

### 虚拟环境

**重要：** 本项目使用虚拟环境，但 Claude Code 可以直接使用，无需手动激活！

- **虚拟环境路径**: `.venv/`
- **Python 版本**: 3.13.0
- **Python 可执行文件**: `.venv/Scripts/python.exe` (Windows)

### 执行 Python 命令

Claude Code 会自动使用虚拟环境中的 Python：

```bash
# 运行主应用
.venv/Scripts/python.exe my_fastApi/main.py

# 使用 uvicorn 启动（推荐）
.venv/Scripts/python.exe -m uvicorn my_fastApi.main:app --reload

# 安装新包
.venv/Scripts/python.exe -m pip install <package>

# 更新 requirements.txt
.venv/Scripts/python.exe -m pip freeze > my_fastApi/requirements.txt
```

## 项目结构

```
D:\codes\study\python\
├── .venv/                    # Python 虚拟环境
├── .claude/                  # Claude Code 配置
│   └── settings.local.json   # 本地权限配置
├── my_fastApi/              # FastAPI 应用主目录
│   ├── main.py              # 应用入口文件
│   ├── requirements.txt     # 项目依赖
│   ├── .env                 # 环境变量配置（不提交到 git）
│   ├── 教材.md              # 学习笔记
│   └── images/              # 文档图片
├── CLAUDE.md               # 本文件（项目说明）
└── claude code使用说明.md  # Claude Code 使用文档
```

## 数据库配置

### MySQL 连接

项目使用异步 MySQL 连接，配置通过环境变量管理：

**环境变量（在 `.env` 文件中配置）：**
- `MYSQL_USER` - 数据库用户名
- `MYSQL_PASSWORD` - 数据库密码
- `MYSQL_HOST` - 数据库主机地址
- `MYSQL_PORT` - 数据库端口
- `MYSQL_DB` - 数据库名称

**连接字符串格式：**
```
mysql+aiomysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4
```

### ORM 模型

使用 SQLAlchemy 2.0 的新式声明语法：
- 基类 `Base(DeclarativeBase)` 包含通用字段（创建时间、更新时间）
- 使用 `Mapped` 和 `mapped_column` 进行类型注解
- 支持异步操作（`AsyncSession`）

## 开发规范

### 编码风格

- 遵循 PEP 8 规范
- 使用类型注解（Type Hints）
- 异步函数使用 `async/await` 语法

### API 开发

- 使用 Pydantic 模型进行请求/响应验证
- 路径参数使用 `Path()` 进行验证
- 查询参数使用 `Query()` 进行验证
- 使用依赖注入（`Depends`）管理数据库会话

### 错误处理

- 使用 `HTTPException` 抛出 HTTP 错误
- 自定义异常处理器处理特定错误

## 常见任务

### 启动开发服务器

```bash
# 方式 1：直接使用 uvicorn（推荐）
.venv/Scripts/python.exe -m uvicorn my_fastApi.main:app --reload --host 0.0.0.0 --port 8000

# 方式 2：如果 main.py 中有 if __name__ == "__main__"
.venv/Scripts/python.exe my_fastApi/main.py
```

### 安装依赖

```bash
# 安装所有依赖
.venv/Scripts/python.exe -m pip install -r my_fastApi/requirements.txt

# 安装单个包
.venv/Scripts/python.exe -m pip install <package-name>
```

### 数据库操作

```bash
# 创建表（如果使用 Alembic 迁移）
.venv/Scripts/python.exe -m alembic upgrade head

# 如果直接使用 SQLAlchemy
# 在代码中调用: await Base.metadata.create_all(bind=async_engine)
```

## 重要提示

### 敏感信息

- `.env` 文件包含数据库凭据，**不要提交到 git**
- 已在 `.gitignore` 中排除 `.env` 文件

### Claude Code 权限

当前配置允许 Claude Code 执行所有 Python 相关命令：
```json
{
  "permissions": {
    "allow": ["Bash(python:*)"]
  }
}
```

### 学习资源

- 项目学习笔记：`my_fastApi/教材.md`
- Claude Code 使用说明：`claude code使用说明.md`

## 当前学习进度

根据 git 提交历史：
- ✅ FastAPI 基础
- ✅ FastAPI 进阶
- ✅ ORM（SQLAlchemy）基础和进阶
- 🔄 持续学习中...

## 注意事项

1. **虚拟环境**：Claude Code 会自动使用 `.venv/` 中的 Python，无需手动激活
2. **数据库连接**：确保 `.env` 文件配置正确
3. **异步操作**：所有数据库操作都是异步的，需要使用 `await`
4. **依赖管理**：新增依赖后记得更新 `requirements.txt`
