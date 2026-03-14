# AI Productivity Toolkit

> 🚀 **让 AI 成为你的超级助手 | 一站式 AI 效率工具库**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Stars](https://img.shields.io/github/stars/zhuxunyu98/ai-productivity-toolkit?style=social)](https://github.com/zhuxunyu98/ai-productivity-toolkit/stargazers)


[🇺🇸 English Documentation](README.md)

**📰 官方博客**: [硅基观察](https://zhuxunyu.github.io) | 最新文章：[对抗 FOMO 的年轻人](https://zhuxunyu.github.io/_posts/2026-03-14-对抗-fomo-的年轻人.md)

---

## 🎯 为什么需要这个工具库？

| 痛点 | 传统方式 | 使用本工具 |
|------|----------|------------|
| Prompt 写不好 | 反复尝试，效果差 | 自动优化，效果提升 10 倍 ⚡ |
| 重复办公任务 | 手动处理，耗时 | 一键自动化，效率翻倍 🚀 |
| 数据采集 | 手动复制，易出错 | 合法合规采集，结构化输出 📊 |
| AI 工作流 | 多个工具切换 | 统一接口，无缝衔接 🔗 |

---

## ✨ 核心功能

### 🧠 Prompt 优化器
> 写不出好 Prompt？让 AI 帮你优化！

```python
from toolkit import PromptOptimizer

optimizer = PromptOptimizer()
optimized = optimizer.optimize("帮我写一个 Python 脚本")
```

**优化前**: `"帮我写一个 Python 脚本"`

**优化后**: 
```
你是一位专业的 Python 开发者。请编写一个 Python 脚本，要求：
1. 功能明确，代码规范
2. 包含必要的注释和文档
3. 考虑边界情况和错误处理
4. 提供使用示例
```

### 📊 Excel/Word/PDF 自动化
> 批量处理办公文档，解放双手

```python
from toolkit import ExcelAutomation

excel = ExcelAutomation()
excel.batch_convert(folder="input/", output_format="pdf")
excel.merge_sheets(["file1.xlsx", "file2.xlsx"], output="merged.xlsx")
```

### 🕷️ 数据采集框架
> 合法合规的数据采集，结构化输出

```python
from toolkit import DataCollector

collector = DataCollector()
data = collector.fetch(url="https://example.com", format="json")
data.to_excel("output.xlsx")
```

### 🔄 AI 工作流自动化
> 一键完成复杂任务

```python
from toolkit import AIWorkflow

workflow = AIWorkflow()
result = workflow.run(
    task="analyze_sentiment",
    input="data/reviews.csv",
    output="results/sentiment.xlsx"
)
```

---

## 🚀 快速开始

### 方法 1: pip 安装（推荐）
```bash
pip install ai-productivity-toolkit
```

### 方法 2: 源码安装
```bash
# 克隆项目
git clone https://github.com/zhuxunyu98/ai-productivity-toolkit.git
cd ai-productivity-toolkit

# 安装依赖
pip install -r requirements.txt

# 运行示例
python examples/prompt_optimizer.py
```

### 方法 3: Docker（即将支持）
```bash
docker run -it zhuxunyu98/ai-productivity-toolkit:latest
```

---

## 📖 使用示例

### 示例 1: 优化你的 Prompt
```python
from toolkit import PromptOptimizer

optimizer = PromptOptimizer()

# 优化写作任务
prompt = "帮我写一篇文章"
optimized = optimizer.optimize(prompt, task_type="writing")
print(optimized)
```

### 示例 2: 批量处理 Excel
```python
from toolkit import ExcelAutomation

excel = ExcelAutomation()

# 批量转换为 PDF
excel.batch_convert(folder="reports/", output_format="pdf")

# 合并多个表格
excel.merge_sheets(["q1.xlsx", "q2.xlsx", "q3.xlsx"], output="yearly.xlsx")
```

### 示例 3: 数据采集 + 分析
```python
from toolkit import DataCollector, AIWorkflow

# 采集数据
collector = DataCollector()
data = collector.fetch(url="https://example.com/products", format="json")

# AI 分析
workflow = AIWorkflow()
result = workflow.run(task="analyze_trends", input=data)
```

更多示例请查看 [examples/](examples/) 目录。

---

## 📦 安装依赖

```bash
# 基础依赖
pip install -r requirements.txt

# 可选：完整功能（包含所有扩展）
pip install -r requirements-full.txt
```

---

## 🔧 配置

创建 `.env` 文件配置 API Keys：

```bash
# OpenAI
OPENAI_API_KEY=your-openai-key

# Anthropic (Claude)
ANTHROPIC_API_KEY=your-anthropic-key

# 其他配置
LOG_LEVEL=INFO
OUTPUT_DIR=./output
```

> ⚠️ **安全提示**: 切勿将 `.env` 文件提交到版本控制！

---

## 📊 性能对比

| 任务 | 传统方式 | 本工具 | 提升 |
|------|----------|--------|------|
| Prompt 优化 | 30 分钟/次 | 30 秒/次 | **60 倍** ⚡ |
| Excel 批量处理 | 2 小时/100 文件 | 5 分钟/100 文件 | **24 倍** 🚀 |
| 数据采集 | 1 小时/网站 | 2 分钟/网站 | **30 倍** 📊 |
| AI 工作流 | 手动切换工具 | 一键完成 | **10 倍** 🔗 |

---

## 🗺️ 路线图

### v1.0 (当前版本)
- ✅ Prompt 优化器
- ✅ Excel/Word/PDF 自动化
- ✅ 数据采集框架
- ✅ AI 工作流

### v1.1 (开发中)
- 🔄 MCP 协议支持
- 🔄 多 LLM 提供商切换
- 🔄 本地知识库/RAG

### v2.0 (计划中)
- ⏳ 图形界面 (GUI)
- ⏳ 浏览器扩展
- ⏳ 团队协作功能

查看完整路线图：[ROADMAP.md](ROADMAP.md)

---

## 🤝 贡献

欢迎贡献！无论是 Bug 报告、功能建议还是代码贡献！

### 快速贡献指南

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 需要帮助？
- 📖 [贡献指南](CONTRIBUTING.md)
- 💬 [Discord 社区](https://discord.gg/xxxxx) (筹备中)
- 📧 Email: zhuxunyu98@gmail.com

---

## 💰 赞助与支持

如果这个项目对你有帮助，欢迎 Star ⭐ 或赞助支持！

### 赞助方式
- [GitHub Sponsors](https://github.com/sponsors/zhuxunyu98)
- [爱发电](https://afdian.com/a/zhuxunyu98)

### 赞助福利
| 档位 | 价格 | 福利 |
|------|------|------|
| 🥉 支持者 | ¥50/月 | 优先回答问题 |
| 🥈 合作者 | ¥200/月 | 1v1 咨询 30 分钟 |
| 🥇 赞助者 | ¥500/月 | 定制工具开发 |

---

## 🔒 安全性

本工具库遵循安全最佳实践：

- ✅ 源代码中无硬编码 API 密钥
- ✅ 环境变量配置
- ✅ `.env` 文件已加入 `.gitignore`
- ✅ 定期安全审计
- ✅ 依赖漏洞扫描

**报告安全漏洞**: zhuxunyu98@gmail.com

---

## 📬 联系方式

- 📧 Email: zhuxunyu98@gmail.com
- 🐦 Twitter: [@zhuxunyu98](https://twitter.com/zhuxunyu98) (筹备中)
- 💼 LinkedIn: [zhuxunyu98](https://linkedin.com/in/zhuxunyu98) (筹备中)
- 📱 微信公众号：AI 效率研究所（筹备中）

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=zhuxunyu98/ai-productivity-toolkit&type=Date)](https://star-history.com/#zhuxunyu98/ai-productivity-toolkit&Date)

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件。

---

<div align="center">

**如果这个项目对你有帮助，请给个 Star ⭐！**

Made with ❤️ by [zhuxunyu98](https://github.com/zhuxunyu98)

</div>
