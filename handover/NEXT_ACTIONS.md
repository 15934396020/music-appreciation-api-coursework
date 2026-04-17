# Next Actions

> **Deadline: 21 April 2026 (via Minerva)**
> **Assessment: 10-minute Oral Examination (5 min presentation + 5 min Q&A)**

---

## What the User Should Send to a New Account

复制粘贴以下消息即可：

```
这是我们的课程项目仓库：https://github.com/15934396020/music-appreciation-api-coursework
请先阅读仓库里的 handover/FOR_NEXT_ACCOUNT.md，再查看 handover/CURRENT_STATUS.md 和 handover/NEXT_ACTIONS.md。
这个项目是 Music Appreciation and Discovery API，目前已经完成可运行原型、25个API接口、55个自动化测试、API Key认证、结构化错误处理、技术报告（PDF）、API文档（PDF）、12页PPTX演示幻灯片、GenAI对话日志、交接文档和 GitHub 同步。
请不要重做已经完成的部分，而是直接按照 NEXT_ACTIONS.md 继续推进。
本轮结束前，请同步更新交接文件，方便下一个账号继续接力。
```

---

## All Core Deliverables Are Complete

| 编号 | 文件 | 状态 | 位置 |
|---|---|---|---|
| 1 | Technical Report (PDF) | DONE | `docs/TECHNICAL_REPORT.pdf` |
| 2 | API Documentation (PDF) | DONE | `docs/API_DOCUMENTATION.pdf` |
| 3 | Presentation Slides (PPTX) | DONE | `docs/PRESENTATION.pptx` (12 slides) |
| 4 | GenAI Conversation Log | DONE | `docs/GENAI_CONVERSATION_LOG.pdf` |
| 5 | GitHub Repository | DONE | `https://github.com/15934396020/music-appreciation-api-coursework` |
| 6 | Source Code + Tests | DONE | 25 endpoints, 55 tests, API key auth |

---

## Remaining Tasks (Priority Order)

### Priority 1: Minerva Submission

**Action:** User needs to upload the following files to Minerva before 21 April 2026:

1. `docs/TECHNICAL_REPORT.pdf`
2. `docs/API_DOCUMENTATION.pdf`
3. `docs/PRESENTATION.pptx`
4. `docs/GENAI_CONVERSATION_LOG.pdf`
5. GitHub repository link

### Priority 2: Oral Examination Preparation

The oral exam is 10 minutes: 5 minutes presentation + 5 minutes Q&A.

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

### Priority 3 (Optional): Further Improvements

以下改进可以帮助项目冲击更高分数：

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

---

## Priority Principle

**不要重建项目。** 所有核心交付物已完成。剩余工作集中在：
1. Minerva 提交（用户操作）
2. 口头答辩准备
3. 可选的进一步改进

## If Time Is Limited

如果会话即将结束，优先做以下事情：

1. 更新 `handover/CURRENT_STATUS.md`
2. 更新 `handover/NEXT_ACTIONS.md`
3. 更新 `handover/SESSION_LOG.md`
4. 推送到 GitHub
5. 保持仓库状态干净可解释
