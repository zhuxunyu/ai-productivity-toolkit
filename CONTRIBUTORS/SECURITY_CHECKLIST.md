# 代码提交安全检查清单

**目标**: 确保每次提交都不泄露敏感信息，遵循安全最佳实践

---

## 🔒 提交前检查（必须执行）

### 1. 敏感信息扫描
```bash
# API Keys / Secrets
grep -riE "(sk-|api[_-]?key|password|secret|token)[\s]*[=:]['\"]?[a-zA-Z0-9]" \
  --include="*.py" --include="*.md" --include="*.txt" --include="*.js" .

# 邮箱地址（确认是公开的）
grep -riE "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" \
  --include="*.py" --include="*.md" .

# 私有 URL / 内部地址
grep -riE "(localhost|192\.168\.|10\.|internal|private)" \
  --include="*.py" --include="*.md" --include="*.yml" .
```

### 2. 占位符规范化
- ❌ `api_key="demo-key"` → 可能被误用
- ✅ `api_key="YOUR_API_KEY_HERE"` → 明显是占位符
- ✅ `api_key="your-openai-key"` → 清楚说明用途

### 3. .gitignore 检查
确认以下文件**不会**被提交：
- `.env`
- `.env.local`
- `*.key`
- `*.pem`
- `secrets/`
- `credentials/`
- `output/` (可能含敏感数据)

### 4. 提交大小检查
- ✅ 单次提交 ≤ 5 个文件
- ✅ 单次提交 ≤ 500 行代码
- ❌ 避免一次性提交大量文件（触发通知轰炸）

---

## 📝 提交规范

### Commit Message 格式
```
<type>(<scope>): <description>

[optional body]

Principle: <相关原则>
```

**Types:**
- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `style`: 代码风格
- `refactor`: 重构
- `security`: 安全修复 ⚠️
- `chore`: 日常维护

### 示例
```
security: 规范化占位符，避免误用

- workflow.py: 占位符改为 'YOUR_API_KEY_HERE'
- automation_scripts.md: 占位符改为 'YOUR_SMTP_PASSWORD_HERE'

Principle: 安全性优先
```

---

## 🚀 推送策略

### 本地开发
- 频繁提交（每完成一个小功能）
- 使用 descriptive commit messages

### 推送到远程
- 累积 3-5 个相关提交后推送一次
- 避免每个提交都推送（减少通知）
- 重要更新（security、feat）单独推送

### 推送前检查
```bash
# 查看将要推送的内容
git log origin/main..main --oneline

# 确认没有敏感文件
git status

# 推送
git push origin main
```

---

## 📧 通知管理

### 避免通知轰炸
- ❌ 每次提交都推送 → 多封邮件
- ✅ 累积相关提交后推送 → 一封邮件

### 重要更新单独通知
- Security 修复 → 立即推送
- Major features → 单独推送
- 文档更新 → 可累积推送

---

## 🔄 心跳检查

每次心跳自动检查：
- [ ] 最近提交是否有敏感信息
- [ ] .gitignore 是否完整
- [ ] 依赖是否有安全更新
- [ ] GitHub Security 警报

---

**最后更新**: 2026-03-07
**下次审查**: 每次提交前
