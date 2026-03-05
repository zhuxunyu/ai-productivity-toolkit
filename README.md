# AI Productivity Toolkit

🤖 一站式 AI 效率工具库 | 让 AI 成为你的超级助手

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Sponsor](https://img.shields.io/badge/-Sponsor-f44336?logo=GitHub-Sponsors)](https://github.com/sponsors/zhuxunyu98)

---

## 🌟 功能亮点

- ✅ **Prompt 优化器** - 自动优化你的 AI 提示词，效果提升 10 倍
- ✅ **批量处理工具** - Excel/Word/PDF 自动化，效率翻倍
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

## 📦 工具列表

### 1. Prompt 优化器
自动优化你的 ChatGPT/Claude 提示词。

```python
from toolkit import PromptOptimizer

optimizer = PromptOptimizer()
optimized = optimizer.optimize("帮我写一个 Python 脚本")
print(optimized)
```

**输出：**
```
你是一位专业的 Python 开发者。请编写一个 Python 脚本，要求：
1. 功能明确，代码规范
2. 包含必要的注释和文档
3. 考虑边界情况和错误处理
4. 提供使用示例

具体需求：[你的需求]
```

### 2. Excel 自动化工具
批量处理 Excel 文件。

```python
from toolkit import ExcelAutomation

excel = ExcelAutomation()
excel.batch_convert(folder="input/", output_format="pdf")
excel.merge_sheets(["file1.xlsx", "file2.xlsx"], output="merged.xlsx")
```

### 3. 数据爬取框架
合法合规的数据采集。

```python
from toolkit import DataCollector

collector = DataCollector()
data = collector.fetch(url="https://example.com", format="json")
data.to_excel("output.xlsx")
```

### 4. AI 工作流自动化
一键完成复杂任务。

```python
from toolkit import AIWorkflow

workflow = AIWorkflow(api_key="your-key")
result = workflow.run(
    task="analyze_sentiment",
    input="data/reviews.csv",
    output="results/sentiment.xlsx"
)
```

---

## 💰 赞助与支持

如果你觉得这个工具库有帮助，欢迎赞助！

### 微信赞助
<img src="payment/wechat_qr.jpg" alt="微信收款码" width="200"/>

### 支付宝赞助
<img src="payment/alipay_qr.jpg" alt="支付宝收款码" width="200"/>

**赞助福利：**
- 🥉 ¥50+ ：优先回答问题
- 🥈 ¥200+ ：1v1 咨询 30 分钟
- 🥇 ¥500+ ：定制工具开发

> 💡 赞助后请发邮件到 zhuxunyu98@gmail.com 说明需求，我会尽快联系你！

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

## ⭐ Star History

如果这个项目对你有帮助，请给个 Star！

[![Star History Chart](https://api.star-history.com/svg?repos=zhuxunyu98/ai-productivity-toolkit&type=Date)](https://star-history.com/#zhuxunyu98/ai-productivity-toolkit&Date)

---

*Made with ❤️ by AI Research Assistant*
