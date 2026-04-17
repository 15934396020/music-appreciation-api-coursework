# Next Actions

> **Last updated: 2026-04-17 (Session 3 — 部署未完成)**
> **Deadline: 21 April 2026 (via Minerva)**
> **Assessment: 10-minute Oral Examination (5 min presentation + 5 min Q&A)**

---

## What the User Should Send to a New Account

复制粘贴以下消息即可：

```
这是我们的课程项目仓库：https://github.com/15934396020/music-appreciation-api-coursework  。请先阅读仓库里的 handover/FOR_NEXT_ACCOUNT.md，再查看 handover/CURRENT_STATUS.md 和 handover/NEXT_ACTIONS.md。这个项目是 Music Appreciation and Discovery API，目前已经完成可运行原型、25个API接口、55个自动化测试、API Key认证、结构化错误处理、技术报告（PDF）、API文档（PDF）、12页PPTX演示幻灯片、GenAI对话日志、交接文档和 GitHub 同步。**唯一剩余的关键工作是：部署到外部平台（不部署只能拿 Pass 分数 40-49）。** 请不要重做已经完成的部分，而是直接按照 NEXT_ACTIONS.md 继续推进；本轮结束前，请同步更新交接文件，方便下一个账号继续接力。
```

附件说明：
- `handover-for-next-account.zip` — 完整项目代码（含 .git 历史和所有交接文档），解压后可直接运行和开发
- `coursework-submission.zip` — 当前已完成的作业提交材料（技术报告 PDF、API文档 PDF、演示幻灯片），请在此基础上继续完善，不要重做
- `XJCO3011_Coursework1_Brief__2025_2026(1).pdf` — 课程要求原文，请仔细对照 deadline（4月21日）和评分标准来推进剩余工作

---

## ⚠️ CRITICAL: Priority 1 — 部署到外部平台

**这是拿 50+ 分的硬性要求。** 课程评分标准明确规定：

| 分数段 | 部署要求 |
|---|---|
| 40-49 (Pass) | "server-side code **not deployed** on an external platform" |
| 50-59 (Satisfactory) | "Hosted on an external web server, e.g. PythonAnywhere" |
| 70-79 (Very Good) | "Professional deployment" |

### 方案 A：Render.com（★ 推荐，最简单）

Render.com 免费支持 FastAPI/ASGI，步骤：

1. 注册 Render.com 账号（用 GitHub 登录最方便）
2. 在项目根目录创建部署文件：

**`render.yaml`：**
```yaml
services:
  - type: web
    name: music-appreciation-api
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn app.main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: PORT
        value: 10000
```

**或 `Procfile`（备选）：**
```
web: uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
```

3. 在 Render Dashboard → New → Web Service → 连接 GitHub 仓库
4. 等待部署完成，获取公网 URL
5. 更新文档中的 URL（见下方"部署后更新"）

### 方案 B：PythonAnywhere ASGI（已创建账号但未完成）

**重要发现：PythonAnywhere 不原生支持 FastAPI（ASGI 框架）。**

已创建的 PythonAnywhere 账号信息：
- 用户名：`weidademiaoxiao`
- 密码：`0355woDE!`
- 域名：`weidademiaoxiao.pythonanywhere.com`
- 状态：已创建 web app（Manual Configuration, Python 3.10），WSGI 文件需改为 ASGI

如果要用 PythonAnywhere，需要通过 ASGI beta API：
- 官方文档：https://help.pythonanywhere.com/pages/ASGICommandLine/
- 需要先获取 API token（Account → API Token）
- 通过 Bash 控制台 clone 代码并安装依赖
- 通过 API 配置 ASGI 站点

### 方案 C：Railway.app 或 Koyeb（备选）

都免费支持 FastAPI，步骤类似 Render.com。

---

## Priority 2: 部署后更新文档

部署成功后，需要更新以下文件中的 URL：

| 文件 | 需要更新的内容 |
|---|---|
| `README.md` | 添加 Live Demo 链接 |
| `docs/TECHNICAL_REPORT.md` → 重新生成 PDF | 添加部署 URL |
| `docs/API_DOCUMENTATION.md` → 重新生成 PDF | 添加 Base URL |
| `docs/PRESENTATION.pptx` | 添加 Live Demo 幻灯片 |

PDF 生成命令：
```bash
manus-md-to-pdf docs/TECHNICAL_REPORT.md docs/TECHNICAL_REPORT.pdf
manus-md-to-pdf docs/API_DOCUMENTATION.md docs/API_DOCUMENTATION.pdf
```

---

## Priority 3: Minerva 提交

**Action:** User needs to upload the following files to Minerva before 21 April 2026:

| 编号 | 文件 | 格式 | 状态 |
|---|---|---|---|
| 1 | Technical Report | PDF | ✅ 已就绪（部署后需更新链接） |
| 2 | Presentation Slides | PPTX | ✅ 已就绪（部署后可添加 demo 链接） |
| 3 | GenAI Conversation Log | 在报告附录 | ✅ 已包含 |
| 4 | GitHub Repository Link | 在报告中 | ✅ 已包含 |

**Technical Report 必须包含：**
- [x] GitHub 仓库链接
- [x] API 文档链接
- [x] 演示幻灯片链接
- [x] GenAI 声明和分析
- [x] GenAI 对话日志（附录）

---

## Priority 4: 口头答辩准备

口头考试 10 分钟：5 分钟演示 + 5 分钟 Q&A。

**Presentation talking points (5 minutes):**
1. Problem statement and motivation (30s) — Slides 1-2
2. Architecture and technology choices (1 min) — Slides 3-4
3. Data model and relationships (30s) — Slide 5
4. Key endpoints and CRUD demo (1 min) — Slides 6-8
5. Authentication and error handling (30s) — Slide 7
6. Analytics endpoints (30s) — Slide 9
7. Testing approach and results (30s) — Slide 10
8. Conclusion and future work (30s) — Slides 11-12

**Q&A 常见问题准备：**
- 为什么选择 FastAPI 而不是 Flask/Django？（高性能、自动文档、类型提示、async 支持）
- 为什么用 SQLite 而不是 PostgreSQL？（零配置、方便考官运行、适合原型开发）
- 认证是如何实现的？（API Key via X-API-Key header, FastAPI dependency injection, 401/403 错误码）
- 如何处理并发写入问题？（SQLite 限制，未来可迁移 PostgreSQL）
- 测试策略是什么？（55 个 pytest 测试，9 个测试类，session-scoped fixture，lifespan 触发）
- GenAI 如何使用的？（架构设计、代码生成、数据生成、测试扩展、文档撰写、多账号协作）
- 如何确保数据一致性？（`_refresh_track_rating` 自动重算平均分）
- 错误处理策略？（结构化 JSON 错误响应，自定义 exception handlers，machine-readable error codes）

---

## Priority 5 (Optional): Further Improvements

| 改进项 | 难度 | 预期加分点 |
|---|---|---|
| 添加 pytest-cov 覆盖率报告 | 低 | 展示测试覆盖率 |
| 添加请求速率限制 | 中 | 展示安全意识 |
| 添加 Docker 支持 | 中 | 展示部署能力 |
| 重新用 LaTeX 编译报告 | 中 | 更精美的排版 |

---

## Completed Tasks (Do Not Repeat)

### Session 1
- [x] 创建 FastAPI 应用和数据库配置
- [x] 实现 6 个核心数据模型
- [x] 扩充种子数据至 29 首曲目、8 个流派
- [x] 实现 25 个 API 端点

### Session 2
- [x] 重构 `main.py` 使用 `lifespan` 替代 deprecated `on_event("startup")`
- [x] 编写并通过 48 个自动化测试
- [x] 生成 LaTeX 技术报告和 API 文档 PDF
- [x] 生成 10 页 HTML 演示幻灯片
- [x] 推送所有代码到 GitHub

### Session 3
- [x] 添加 API Key 认证系统 (`app/auth.py`)
- [x] 添加结构化错误处理 (`app/errors.py`)
- [x] 扩展测试至 55 个（添加 TestAuthentication 类）
- [x] 创建 12 页 PPTX 演示文稿
- [x] 创建 GenAI 对话日志 (MD + PDF)
- [x] 更新技术报告（认证章节、修正曲目数量）
- [x] 更新 API 文档（认证文档、错误格式）
- [x] 更新 README.md
- [x] 推送所有变更到 GitHub
- [x] 更新所有交接文档
- [x] 创建 PythonAnywhere 账号和 web app（但发现不原生支持 FastAPI）
- [ ] **部署到外部平台 — 未完成，需要下一个账号继续**

---

## 文件结构参考

```
music-appreciation-api-coursework/
├── app/
│   ├── main.py              # FastAPI 应用入口 (v0.3.0)
│   ├── auth.py              # API Key 认证（Session 3）
│   ├── errors.py            # 结构化错误处理（Session 3）
│   ├── database.py          # SQLAlchemy 数据库配置
│   ├── seed.py              # 种子数据（29 tracks, 8 genres）
│   ├── models/entities.py   # SQLAlchemy ORM 模型
│   ├── routers/api.py       # 25 个 API 端点
│   └── schemas/entities.py  # Pydantic 验证模型
├── tests/
│   ├── conftest.py          # pytest fixtures
│   └── test_api.py          # 55 个自动化测试
├── docs/
│   ├── TECHNICAL_REPORT.md  # 技术报告 Markdown
│   ├── TECHNICAL_REPORT.pdf # 技术报告 PDF
│   ├── TECHNICAL_REPORT.tex # 技术报告 LaTeX（Session 2）
│   ├── API_DOCUMENTATION.md # API 文档 Markdown
│   ├── API_DOCUMENTATION.pdf# API 文档 PDF
│   ├── PRESENTATION.pptx    # PowerPoint 演示（Session 3）
│   ├── GENAI_CONVERSATION_LOG.md  # GenAI 日志
│   ├── GENAI_CONVERSATION_LOG.pdf # GenAI 日志 PDF
│   └── presentation/        # HTML 演示幻灯片（Session 2）
├── handover/                # 交接文档
├── scripts/                 # 工具脚本
├── requirements.txt         # Python 依赖
└── README.md                # 项目说明
```

## 运行命令

```bash
# 安装依赖
pip install -r requirements.txt

# 运行 API
uvicorn app.main:app --reload

# 运行测试（55 个全部通过）
pytest -v

# 测试认证
curl -X POST http://localhost:8000/api/v1/genres \
  -H "X-API-Key: music-api-demo-key-2026" \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Genre"}'
```
