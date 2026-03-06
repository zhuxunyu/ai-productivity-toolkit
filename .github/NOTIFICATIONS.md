# 🔔 GitHub 通知配置指南

**目标**: 接收必要的通知，避免邮件骚扰

---

## 📧 在 GitHub 上配置通知

### 方法 1: 仓库级别配置（推荐）

1. 进入仓库：https://github.com/zhuxunyu98/ai-productivity-toolkit
2. 点击右上角的 **Watch** 按钮
3. 选择 **Custom** → **Configure**
4. 配置如下：

| 通知类型 | 推荐设置 | 说明 |
|----------|----------|------|
| **Issues** | ✅ 订阅 | 新 issue 需要处理 |
| **Pull requests** | ✅ 订阅 | 新 PR 需要 review |
| **Releases** | ✅ 订阅 | 版本发布通知 |
| **Discussions** | ❌ 不订阅 | 暂时不需要 |
| **Security alerts** | ✅ 订阅 | 重要安全通知 |
| **Workflow runs** | ❌ 不订阅 | 避免每次 push 都通知 |
| **Workflow failures** | ✅ 订阅 | 只在失败时通知 |

### 方法 2: 全局通知配置

1. 进入 GitHub Settings → Notifications
2. 配置邮件通知：
   - ✅ **Participating** - 只通知你参与的话题
   - ❌ **All Activity** - 不要订阅所有活动
3. 配置通知方式：
   - ✅ GitHub Web 通知
   - ❌ Email（或只接收重要通知）

---

## 🛠️ 项目侧配置

### Workflow 失败通知

GitHub 默认会通知 workflow 失败，这是必要的。

### 减少推送通知

**当前策略**：
- 每次 push 会触发 CI/CD
- CI/CD 成功 → 不通知
- CI/CD 失败 → 通知

---

## ✅ 推荐配置

**订阅**：
- ✅ 新 Issues
- ✅ 新 PRs
- ✅ Workflow 失败
- ✅ 安全警报

**不订阅**：
- ❌ 每次 push 成功
- ❌ Workflow 成功运行
- ❌ Star 增长

---

## 📬 快速配置链接

- 仓库通知：https://github.com/zhuxunyu98/ai-productivity-toolkit/subscription
- 全局设置：https://github.com/settings/notifications

---

**配置完成后，你将只收到必要的通知！**
