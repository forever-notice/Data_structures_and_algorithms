# Git 快速参考卡片 ⚡

## 💡 每天必用的 5 个命令

```bash
# 1️⃣ 查看状态（随时都可以用）
git status

# 2️⃣ 添加修改到暂存区
git add .                    # 添加所有修改
git add 文件名.py            # 添加指定文件

# 3️⃣ 提交保存版本
git commit -m "完成XX算法"

# 4️⃣ 查看历史
git log --oneline

# 5️⃣ 查看修改内容
git diff
```

---

## 📋 标准工作流程

```bash
# 每次开始工作时
git status                           # 检查状态

# 修改代码后...

# 准备提交
git status                           # 再次检查
git add .                            # 添加修改
git commit -m "描述你做了什么"      # 提交

# 查看结果
git log --oneline                    # 查看历史
```

---

## 🌳 分支操作

```bash
# 创建并切换到新分支（尝试新算法时）
git checkout -b 分支名

# 查看所有分支
git branch

# 切换回主分支
git checkout main

# 合并分支（成功后）
git merge 分支名

# 删除分支（不需要时）
git branch -d 分支名
```

---

## 🔄 撤销操作

```bash
# 撤销工作区的修改（还没 add）
git checkout -- 文件名

# 从暂存区移除（已 add 但想撤回）
git reset HEAD 文件名

# 修改上一次提交信息
git commit --amend -m "新信息"
```

---

## 📝 好的提交信息示例

```bash
✅ git commit -m "完成冒泡排序算法"
✅ git commit -m "修复二分查找边界问题"
✅ git commit -m "优化快速排序性能"
✅ git commit -m "添加链表反转练习"

❌ git commit -m "修改"
❌ git commit -m "test"
❌ git commit -m "update"
```

---

## ⚠️ 记住！

1. **经常 commit**：每完成一个小功能就提交
2. **写清楚信息**：让未来的你看懂
3. **有疑问先 status**：90% 的问题都能找到答案
4. **实验用分支**：不确定的代码别直接写在 main

---

## 🆘 遇到问题？

1. **先冷静，执行** `git status` **看看状态**
2. **查看** `GIT_GUIDE.md` **了解详细说明**
3. **记住：Git 很难真正搞坏代码！**

