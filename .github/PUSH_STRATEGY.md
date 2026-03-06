# 📅 推送策略优化

**目标**: 减少邮件通知频率，同时保持自动化

---

## ❌ 当前问题

```
每次 commit → 立即 push → 触发 workflow → 发送邮件
每次 commit → 立即 push → 触发 workflow → 发送邮件
每次 commit → 立即 push → 触发 workflow → 发送邮件
```

**结果**: 用户收到多封邮件骚扰

---

## ✅ 优化策略

### 策略 1: 定时推送（推荐）

**规则**:
- 每天固定时间推送：12:00、20:00（Asia/Shanghai）
- 本地累积多个 commit
- 一次性 push → 只触发 1 次 workflow → 1 封邮件

**示例**:
```
09:00 commit × 3 (本地)
12:00 push → 触发 workflow → 1 封邮件
15:00 commit × 2 (本地)
18:00 commit × 1 (本地)
20:00 push → 触发 workflow → 1 封邮件
```

**每日邮件数**: 2 封（而非 6+ 封）

### 策略 2: 批量提交

**规则**:
- 小改动：本地 commit，不 push
- 大功能：完成后 push
- 紧急修复：立即 push

**示例**:
```
修复 README → commit (本地)
添加功能 A → commit (本地)
添加功能 B → commit (本地)
完成阶段工作 → push (1 次)
```

### 策略 3: Workflow 优化

**配置**:
- 只在特定分支触发（main）
- 添加 [skip ci] 标签跳过 workflow
- 合并小改动为一次 workflow 运行

---

## 🤖 自动化脚本

### 定时推送脚本

```bash
#!/bin/bash
# scripts/scheduled-push.sh

# 检查是否有未推送的 commit
if git log origin/main..main --oneline | grep -q .; then
    echo "Found unpushed commits, pushing now..."
    git push origin main
else
    echo "No unpushed commits."
fi
```

### Crontab 配置

```bash
# 每天 12:00 和 20:00 推送
0 12 * * * cd /path/to/repo && ./scripts/scheduled-push.sh
0 20 * * * cd /path/to/repo && ./scripts/scheduled-push.sh
```

---

## 📊 推送频率对比

| 策略 | 每日 push 次数 | 每日邮件数 |
|------|-------------|-----------|
| ❌ 当前（每次 commit 都 push） | 6-10 次 | 6-10 封 |
| ✅ 定时推送（12:00/20:00） | 2 次 | 2 封 |
| ✅ 批量提交（阶段完成） | 1-2 次 | 1-2 封 |

---

## 🎯 执行计划

**立即生效**:
1. 本地累积 commit（不立即 push）
2. 每天 12:00、20:00 推送
3. 紧急修复除外

**Workflow 配置**:
- 保持启用（用户需要知道失败）
- 优化为只运行必要检查

---

**最后更新**: 2026-03-07
**下次审查**: 2026-03-14
