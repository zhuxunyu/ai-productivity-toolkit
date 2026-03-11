# AI Productivity Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

🤖 **一站式 AI 效率工具库** - 让 AI 成为你的超级助手

---

## 🌟 核心功能

- ✅ **Prompt 优化器** - 自动优化 AI 提示词，效果提升 10 倍
- ✅ **Excel 自动化** - 批量处理、格式转换、数据合并
- ✅ **数据爬取框架** - 合法合规的数据采集工具
- ✅ **AI 工作流** - 一键自动化复杂任务

---

## 🚀 快速开始

```bash
# 克隆项目
git clone https://github.com/zhuxunyu98/ai-productivity-toolkit.git
cd ai-productivity-toolkit

# 安装依赖
pip install -r requirements.txt

# 运行示例
python examples/prompt_optimizer.py
```

---

## 📦 工具介绍

### 1. Prompt 优化器

自动优化你的 ChatGPT/Claude 提示词。

```python
from toolkit import PromptOptimizer

optimizer = PromptOptimizer()
optimized = optimizer.quick_optimize("帮我写一个 Python 脚本")
print(optimized)
```

**输出：**
```
你是一位资深 Python 开发者。请编写代码：

【代码要求】
1. 功能完整，逻辑清晰
2. 遵循最佳实践和代码规范
3. 包含必要的注释和文档字符串
4. 考虑边界情况和错误处理
5. 提供使用示例

【功能需求】
帮我写一个 Python 脚本

【技术栈】
Python（最新最佳实践）
```

### 2. Excel 自动化工具

```python
from toolkit import ExcelAutomation

excel = ExcelAutomation()

# 批量转换 PDF
stats = excel.batch_convert("input/", "pdf")

# 合并多个文件
excel.merge_sheets(["file1.xlsx", "file2.xlsx"], "merged.xlsx")
```

### 3. 数据爬取框架

```python
from toolkit import DataCollector

collector = DataCollector(delay=2.0)

# 单个 URL
data = collector.fetch("https://example.com")

# 批量抓取
urls = ["https://example.com/1", "https://example.com/2"]
stats = collector.batch_fetch(urls, "output.csv")
```

### 4. AI 工作流

```python
from toolkit import AIWorkflow

workflow = AIWorkflow(api_key="your-api-key")

# 情感分析
result = workflow.run(
    task="sentiment_analysis",
    input="data/reviews.csv",
    output="results/sentiment.xlsx"
)
```

---

## 💰 赞助与支持

如果你觉得这个工具库有帮助，欢迎赞助！

- [GitHub Sponsors](https://github.com/sponsors/zhuxunyu98) - 月赞助

- [Buy Me a Coffee](https://www.buymeacoffee.com/zhuxunyu98) - 一次性赞助

**赞助福利：**

| 赞助金额 | 福利 |
|----------|------|
| ¥50+ | 优先回答问题 |
| ¥200+ | 1v1 咨询 30 分钟 |
| ¥500+ | 定制工具开发 |
| ¥1000+ | 企业级支持 |

---

## 📖 文档

- [完整文档](docs/README.md)
- [使用教程](docs/tutorial.md)
- [API 参考](docs/api.md)
- [常见问题](docs/faq.md)

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

## 📬 联系方式

- Email: zhuxunyu98@gmail.com
- GitHub: [@zhuxunyu98](https://github.com/zhuxunyu98)
- 微信公众号：AI 效率研究所（筹备中）

---

*Made with ❤️ by AI Research Assistant*
