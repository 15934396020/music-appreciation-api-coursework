# Next Actions

> **Deadline: 21 April 2026 (via Minerva)**
> **Assessment: 10-minute Oral Examination (5 min presentation + 5 min Q&A)**

---

## What the User Should Send to a New Account

复制粘贴以下消息即可：

```
这是我们的课程项目仓库：https://github.com/15934396020/music-appreciation-api-coursework
请先阅读仓库里的 handover/FOR_NEXT_ACCOUNT.md，再查看 handover/CURRENT_STATUS.md 和 handover/NEXT_ACTIONS.md。
这个项目是 Music Appreciation and Discovery API，目前代码、测试、文档（LaTeX PDF）、幻灯片都已完成。
请不要重做已经完成的部分，而是直接按照 NEXT_ACTIONS.md 继续推进。
本轮结束前，请同步更新交接文件，方便下一个账号继续接力。
```

---

## Immediate Next Tasks (按优先级排序)

### Priority 1: 将演示幻灯片导出为 PPTX 格式

**原因：** 课程要求提交 PowerPoint 格式的演示文稿（PPTX），目前幻灯片是 HTML 格式。

**操作步骤：**
1. 读取 `docs/presentation/` 目录下的 10 个 HTML 幻灯片文件。
2. 将内容转换为 PPTX 格式（可使用 `python-pptx` 库）。
3. 保存为 `docs/PRESENTATION.pptx`。
4. 确保幻灯片排版美观、字体清晰、配色一致。

### Priority 2: 导出 GenAI 对话日志

**原因：** 课程要求附上 GenAI 使用的对话日志作为补充材料（"Attach examples of exported conversation logs as supplementary material"）。

**操作步骤：**
1. 整理 `handover/SESSION_LOG.md` 中的 GenAI 使用记录。
2. 创建 `docs/GENAI_CONVERSATION_LOG.md`，记录关键的 AI 辅助开发对话摘要。
3. 转换为 PDF：`docs/GENAI_CONVERSATION_LOG.pdf`。

### Priority 3: 准备 Minerva 提交材料清单

**原因：** 所有材料需要通过 Minerva 平台提交。

**提交清单：**

| 编号 | 文件 | 当前状态 | 备注 |
|---|---|---|---|
| 1 | Technical Report (PDF, LaTeX) | ✅ 已完成 `docs/TECHNICAL_REPORT.pdf` | 5 页，含封面、彩色标题、GenAI 声明 |
| 2 | API Documentation (PDF, LaTeX) | ✅ 已完成 `docs/API_DOCUMENTATION.pdf` | 8 页，含目录、HTTP 方法彩色标签 |
| 3 | Presentation Slides (PPTX) | ❌ 待完成 | 需从 HTML 转换为 PPTX |
| 4 | GitHub Repository | ✅ 已推送 | `https://github.com/15934396020/music-appreciation-api-coursework` |
| 5 | GenAI Conversation Log | ❌ 待完成 | 课程要求附上对话日志 |

### Priority 4: 准备口头答辩

**原因：** 口头答辩占总分 25%（15% 演示 + 10% Q&A）。

**演示部分（5 分钟）建议流程：**
1. 项目介绍和动机（30 秒）— Slide 1-2
2. 范围和架构设计（1 分钟）— Slide 3-4
3. 数据库设计和端点概览（1 分钟）— Slide 5-6
4. 现场演示（Swagger UI）（1.5 分钟）— Slide 7
5. 分析端点和测试（45 秒）— Slide 8-9
6. 总结和未来方向（15 秒）— Slide 10

**Q&A 常见问题准备：**
- 为什么选择 FastAPI 而不是 Flask/Django？（高性能、自动文档、类型提示）
- 为什么用 SQLite 而不是 PostgreSQL？（零配置、方便考官运行）
- 如何处理并发写入问题？（SQLite 限制，未来可迁移 PostgreSQL）
- 测试策略是什么？（48 个 pytest 测试，session-scoped fixture，lifespan 触发）
- GenAI 如何使用的？（代码重构、数据生成、测试扩展、文档撰写）
- 如何确保数据一致性？（`_refresh_track_rating` 自动重算平均分）

### Priority 5（可选）: 增强项目以冲击更高分数

以下改进可以帮助项目从 70-79 分段提升到更高：

| 改进项 | 难度 | 预期加分点 |
|---|---|---|
| 添加 CORS 中间件 | 低 | 展示对跨域请求的理解 |
| 添加请求速率限制 | 中 | 展示安全意识 |
| 添加 Docker 支持 | 中 | 展示部署能力（Version Control & Deployment 6分） |
| 添加 OpenAPI schema 自定义描述 | 低 | 提升 API 文档质量 |
| 添加更多 edge case 测试 | 低 | 提升 Testing 分数 |

---

## Completed Tasks (Do Not Repeat)

- [x] 创建 FastAPI 应用和数据库配置
- [x] 实现 6 个核心数据模型（Genre, Track, Review, UserTag, Collection, CollectionItem）
- [x] 重构 `main.py` 使用 `lifespan` 替代 deprecated `on_event("startup")`
- [x] 扩充种子数据至 25 首曲目、8 个流派
- [x] 实现 25 个 API 端点（General, Genres, Tracks, Reviews, Tags, Collections, Analytics）
- [x] 编写并通过 48 个自动化测试
- [x] 生成 `API_DOCUMENTATION.tex` 并编译为美观的 `API_DOCUMENTATION.pdf`（8 页，含目录和 HTTP 方法彩色标签）
- [x] 生成 `TECHNICAL_REPORT.tex` 并编译为美观的 `TECHNICAL_REPORT.pdf`（5 页，含封面和 GenAI 声明框）
- [x] 生成 10 页 HTML 演示幻灯片
- [x] 更新 `README.md`
- [x] 推送所有代码到 GitHub
- [x] 更新所有交接文档（CURRENT_STATUS, NEXT_ACTIONS, SESSION_LOG）

---

## Priority Principle

**不要重建项目。** 核心架构和代码已经完成且稳定。剩余工作集中在：
1. 格式转换（HTML slides → PPTX）
2. 补充材料（GenAI 对话日志）
3. 答辩准备
4. Minerva 提交

## If Time Is Limited

如果会话即将结束，优先做以下事情：

1. 更新 `handover/CURRENT_STATUS.md`
2. 更新 `handover/NEXT_ACTIONS.md`
3. 更新 `handover/SESSION_LOG.md`
4. 推送到 GitHub
5. 保持仓库状态干净可解释
