# GitHub 日常使用快速指南 ⚡

## 🎯 每天的标准流程

```bash
# 1️⃣ 写代码、练习算法...

# 2️⃣ 完成后保存到 GitHub
git status              # 查看改了什么
git add .               # 添加所有修改
git commit -m "描述"    # 提交到本地
git push                # 上传到 GitHub ⬆️
```

**就这么简单！** 4 个命令，让你的代码安全保存在云端。

---

## 💻 你的 GitHub 仓库地址

```
https://github.com/forever-notice/Data_structures_and_algorithms
```

### 查看你的代码：
- 打开浏览器
- 访问上面的地址
- 就能看到所有代码和提交历史！

---

## 📊 完整工作流程图

```
你的电脑                           GitHub 云端
┌─────────────────┐              ┌─────────────────┐
│ 1. 写代码       │              │                 │
│ 2. git add .    │              │                 │
│ 3. git commit   │              │                 │
│ 4. git push ────┼─────────────>│ 5. 代码已备份 ✅│
└─────────────────┘              └─────────────────┘
```

---

## 🔄 在其他电脑上工作

### 第一次（克隆仓库）：

```bash
# 克隆你的仓库到新电脑
git clone git@github.com:forever-notice/Data_structures_and_algorithms.git

# 进入文件夹
cd Data_structures_and_algorithms

# 开始工作！
```

### 之后每次：

```bash
# 开始前：拉取最新代码
git pull

# 工作...

# 结束后：推送代码
git add .
git commit -m "描述"
git push
```

---

## 📝 提交信息示例

### ✅ 好的提交信息：

```bash
git commit -m "完成冒泡排序算法"
git commit -m "修复二分查找边界问题"
git commit -m "添加链表反转练习"
git commit -m "学习快速排序的分治思想"
git commit -m "优化数组去重算法性能"
```

### ❌ 不好的提交信息：

```bash
git commit -m "修改"        # 太简单
git commit -m "update"      # 没说清楚
git commit -m "test"        # 无意义
git commit -m "aaa"         # 无意义
```

---

## 🆘 常用命令

```bash
# 查看状态（最常用！）
git status

# 查看修改内容
git diff

# 查看提交历史
git log --oneline

# 查看远程仓库信息
git remote -v

# 拉取最新代码
git pull

# 推送到 GitHub
git push
```

---

## ⚠️ 遇到问题？

### 问题 1：push 时提示 "rejected"

**原因**：GitHub 上有新内容，本地没有

**解决**：
```bash
git pull          # 先拉取
git push          # 再推送
```

### 问题 2：忘记推送了怎么办？

**不用担心**！
- 本地提交都还在
- 下次想起来再 `git push` 就行

### 问题 3：如何查看 GitHub 上的代码？

浏览器访问：
```
https://github.com/forever-notice/Data_structures_and_algorithms
```

### 问题 4：想在手机上看代码？

可以！
- 在手机浏览器访问上面的地址
- 或者下载 GitHub 手机 App

---

## 📈 GitHub 小技巧

### 1. README 文件很重要
GitHub 会自动显示 `README.md` 作为项目首页

### 2. 查看提交历史
在 GitHub 网页上点击 "Commits" 可以看到所有提交

### 3. 查看代码改动
点击任意提交，可以看到具体改了什么

### 4. 搜索代码
GitHub 上可以搜索你的所有代码

### 5. 统计信息
点击 "Insights" 可以看到：
- 提交频率
- 代码量统计
- 语言占比

---

## 🎓 进阶功能（以后可以学）

- **Issues**：记录 bug 和待办事项
- **Projects**：项目管理看板
- **Discussions**：讨论区
- **Actions**：自动化测试和部署
- **GitHub Pages**：免费托管网页

---

## 📌 记住！

### 每天的口诀：
```
写代码 → add → commit → push
```

### 在其他电脑：
```
pull → 写代码 → add → commit → push
```

### 关键点：
- ✅ **经常 commit**：每完成一个小功能就提交
- ✅ **经常 push**：每天结束前至少 push 一次
- ✅ **写清楚提交信息**：给未来的自己看
- ✅ **不要害怕**：Git 和 GitHub 很难真正搞坏代码

---

## 🎉 你已经是专业的！

现在你的工作流程和专业程序员一样：
- ✅ 使用 Git 进行版本控制
- ✅ 使用 GitHub 进行云端备份
- ✅ 每次修改都有记录
- ✅ 可以随时回退
- ✅ 代码安全可靠

**继续加油学习算法吧！** 🚀

---

## 📞 需要帮助？

- 查看 `GIT_GUIDE.md` - Git 详细指南
- 查看 `GIT_QUICK_REF.md` - Git 快速参考
- 查看 `GITHUB_SETUP.md` - GitHub 设置指南

或者随时问我！😊

