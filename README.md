# AI Productivity Toolkit

> 🚀 **Make AI Your Super Assistant | All-in-One AI Efficiency Toolkit**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Stars](https://img.shields.io/github/stars/zhuxunyu98/ai-productivity-toolkit?style=social)](https://github.com/zhuxunyu98/ai-productivity-toolkit/stargazers)
[![Stars](https://img.shields.io/github/stars/zhuxunyu/ai-productivity-toolkit?style=social)](https://github.com/zhuxunyu/ai-productivity-toolkit/stargazers)

[🇨🇳 中文文档](README_CN.md)

---

## 📰 最新更新

- **2026-03-19**: 发布 [国产 AI 助手横向测评](https://zhuxunyu.github.io/2026/03/19/国产 AI 助手横向测评.html) - 深度对比 Kimi、文心一言、通义千问、豆包、智谱清言
- **2026-03-17**: 新增 [中国 AI 助手 Prompt 模板](templates/chinese-ai-assistants-prompts.md) - 针对主流国产 AI 优化的 Prompt 集合

---

## 🎯 Why This Toolkit?

| Pain Point | Traditional Way | With This Toolkit |
|------------|-----------------|-------------------|
| Poor Prompt Quality | Trial & error, bad results | Auto-optimized, 10x better ⚡ |
| Repetitive Office Tasks | Manual processing, time-consuming | One-click automation, 2x efficiency 🚀 |
| Data Collection | Manual copy-paste, error-prone | Legal & compliant, structured output 📊 |
| AI Workflows | Switching between tools | Unified interface, seamless integration 🔗 |

---

## ✨ Core Features

### 🧠 Prompt Optimizer
> Can't write good Prompts? Let AI optimize for you!

```python
from toolkit import PromptOptimizer

optimizer = PromptOptimizer()
optimized = optimizer.optimize("Write a Python script for me")
```

**Before**: `"Write a Python script for me"`

**After**:
```
You are a professional Python developer. Please write a Python script that:
1. Has clear functionality and follows coding standards
2. Includes necessary comments and documentation
3. Considers edge cases and error handling
4. Provides usage examples

Specific requirements: [Your requirements]
```

### 📊 Excel/Word/PDF Automation
> Batch process office documents, free your hands

```python
from toolkit import ExcelAutomation

excel = ExcelAutomation()
excel.batch_convert(folder="input/", output_format="pdf")
excel.merge_sheets(["file1.xlsx", "file2.xlsx"], output="merged.xlsx")
```

### 🕷️ Data Collection Framework
> Legal and compliant data collection with structured output

```python
from toolkit import DataCollector

collector = DataCollector()
data = collector.fetch(url="https://example.com", format="json")
data.to_excel("output.xlsx")
```

### 🔄 AI Workflow Automation
> Complete complex tasks with one click

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

## 🚀 Quick Start

### Method 1: pip install (Recommended)
```bash
pip install ai-productivity-toolkit
```

### Method 2: Source installation
```bash
# Clone the repository
git clone https://github.com/zhuxunyu98/ai-productivity-toolkit.git
cd ai-productivity-toolkit

# Install dependencies
pip install -r requirements.txt

# Run example
python examples/prompt_optimizer.py
```

### Method 3: Docker (Coming Soon)
```bash
docker run -it zhuxunyu98/ai-productivity-toolkit:latest
```

---

## 📖 Usage Examples

### Example 1: Optimize Your Prompt
```python
from toolkit import PromptOptimizer

optimizer = PromptOptimizer()

# Optimize writing task
prompt = "Help me write an article"
optimized = optimizer.optimize(prompt, task_type="writing")
print(optimized)
```

### Example 2: Batch Process Excel Files
```python
from toolkit import ExcelAutomation

excel = ExcelAutomation()

# Batch convert to PDF
excel.batch_convert(folder="reports/", output_format="pdf")

# Merge multiple sheets
excel.merge_sheets(["q1.xlsx", "q2.xlsx", "q3.xlsx"], output="yearly.xlsx")
```

### Example 3: Data Collection + Analysis
```python
from toolkit import DataCollector, AIWorkflow

# Collect data
collector = DataCollector()
data = collector.fetch(url="https://example.com/products", format="json")

# AI analysis
workflow = AIWorkflow()
result = workflow.run(task="analyze_trends", input=data)
```

More examples in [examples/](examples/) directory.

---

## 📦 Installation

```bash
# Basic dependencies
pip install -r requirements.txt

# Optional: Full features (all extensions)
pip install -r requirements-full.txt
```

---

## 🔧 Configuration

Create a `.env` file for API Keys:

```bash
# OpenAI
OPENAI_API_KEY=your-openai-key

# Anthropic (Claude)
ANTHROPIC_API_KEY=your-anthropic-key

# Other configurations
LOG_LEVEL=INFO
OUTPUT_DIR=./output
```

> ⚠️ **Security Notice**: Never commit your `.env` file to version control!

---

## 📊 Performance Comparison

| Task | Traditional | This Toolkit | Improvement |
|------|-------------|--------------|-------------|
| Prompt Optimization | 30 min/time | 30 sec/time | **60x** ⚡ |
| Excel Batch Processing | 2 hours/100 files | 5 min/100 files | **24x** 🚀 |
| Data Collection | 1 hour/website | 2 min/website | **30x** 📊 |
| AI Workflow | Manual tool switching | One-click completion | **10x** 🔗 |

---

## 🗺️ Roadmap

### v1.0 (Current)
- ✅ Prompt Optimizer
- ✅ Excel/Word/PDF Automation
- ✅ Data Collection Framework
- ✅ AI Workflows

### v1.1 (In Development)
- 🔄 MCP Protocol Support
- 🔄 Multi-LLM Provider Switching
- 🔄 Local Knowledge Base / RAG

### v2.0 (Planned)
- ⏳ Graphical User Interface (GUI)
- ⏳ Browser Extension
- ⏳ Team Collaboration Features

View full roadmap: [ROADMAP.md](ROADMAP.md)

---

## 🤝 Contributing

Contributions welcome! Bug reports, feature requests, and code contributions!

### Quick Contribution Guide

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Need Help?
- 📖 [Contributing Guidelines](CONTRIBUTING.md)
- 💬 [Discord Community](https://discord.gg/xxxxx) (Coming Soon)
- 📧 Email: zhuxunyu98@gmail.com

---

## 💰 Sponsorship & Support

If this project helps you, please Star ⭐ or sponsor!

### Sponsorship Channels
- [GitHub Sponsors](https://github.com/sponsors/zhuxunyu98)
- [爱发电](https://afdian.com/a/zhuxunyu98)

### Sponsor Benefits
| Tier | Price | Benefits |
|------|-------|----------|
| 🥉 Supporter | ¥50/month | Priority support |
| 🥈 Collaborator | ¥200/month | 30-min 1v1 consultation |
| 🥇 Sponsor | ¥500/month | Custom tool development |

---

## 🔒 Security

This toolkit follows security best practices:

- ✅ No hardcoded API keys in source code
- ✅ Environment variable configuration
- ✅ `.env` file in `.gitignore`
- ✅ Regular security audits
- ✅ Dependency vulnerability scanning

**Report a vulnerability**: zhuxunyu98@gmail.com

---

## 📬 Contact

- 📧 Email: zhuxunyu98@gmail.com
- 🐦 Twitter: [@zhuxunyu98](https://twitter.com/zhuxunyu98) (Coming Soon)
- 💼 LinkedIn: [zhuxunyu98](https://linkedin.com/in/zhuxunyu98) (Coming Soon)
- 📱 WeChat Official Account: AI Efficiency Lab (In Preparation)

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=zhuxunyu98/ai-productivity-toolkit&type=Date)](https://star-history.com/#zhuxunyu98/ai-productivity-toolkit&Date)

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details.

---

<div align="center">

**If this project helps you, please give it a Star ⭐!**

Made with ❤️ by [zhuxunyu98](https://github.com/zhuxunyu98)

</div>

## 📝 新增工具：ADHD 自救指南

- **添加**: 心理健康工具推荐清单
- **来源**: [博客文章](https://zhuxunyu.github.io/_posts/2026-03-18-ADHD-自救指南.md)
- **工具列表**:
  - 两分钟法则
  - 番茄工作法（ADHD 改良版）
  - 身体倍增法
  - 视觉化待办清单
  - 即时奖励系统

## 📝 产业观察：中国厨房进入"智驾"时代

- **添加**: 智能家居 2026 趋势分析
- **来源**: [博客文章](https://zhuxunyu.github.io/_posts/2026-03-20-中国厨房智驾时代.md)
- **核心洞察**:
  - 市场规模：2026 年预计 1800 亿元，年复合增长 35%+
  - 三阶段演进：L1 单品智能→L2 场景联动→L3 决策智能
  - 四大驱动：技术成熟、消费认知、产业协同、生态竞争
  - 未来趋势：AI 大模型集成、厨房机器人、健康管理、订阅制
- **相关工具**: 智能家居选购指南（开发中）

