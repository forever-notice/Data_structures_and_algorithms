# Git 使用指南 - 算法学习项目版本管理

## 📖 基础概念

### Git 是什么？
Git 是一个版本控制系统，就像是代码的"时光机"，可以：
- ✅ 记录每次修改的历史
- ✅ 随时回退到之前的版本
- ✅ 对比不同版本的差异
- ✅ 创建分支进行实验

### 三个重要区域
```
工作区（你看到的文件）
    ↓ git add
暂存区（准备提交的修改）
    ↓ git commit
仓库（所有历史记录）
```

---

## 🎯 日常使用的命令（按使用频率排序）

### 1. 查看状态 ⭐⭐⭐⭐⭐
```bash
git status
```
**用途**：查看哪些文件被修改了，哪些在暂存区
**使用时机**：任何时候都可以用，不会改变任何东西

---

### 2. 添加文件到暂存区 ⭐⭐⭐⭐⭐
```bash
# 添加所有修改的文件
git add .

# 添加指定文件
git add array_practice.py

# 添加多个文件
git add array_practice.py test.py
```
**用途**：告诉 Git 哪些修改准备提交
**使用时机**：修改文件后，准备保存版本前

---

### 3. 提交修改 ⭐⭐⭐⭐⭐
```bash
git commit -m "描述你做了什么修改"
```
**用途**：保存一个版本快照
**使用时机**：完成一个小功能或修复一个问题后

**提交信息的写法示例**：
- ✅ `git commit -m "完成数组插入算法"`
- ✅ `git commit -m "修复二分查找的边界问题"`
- ✅ `git commit -m "添加链表练习题"`
- ❌ `git commit -m "修改"`（太简单，以后看不懂）
- ❌ `git commit -m "aaa"`（没有意义）

---

### 4. 查看提交历史 ⭐⭐⭐⭐
```bash
# 简洁查看
git log --oneline

# 详细查看
git log

# 查看最近 5 次提交
git log --oneline -5

# 查看某个文件的修改历史
git log --oneline array_practice.py
```
**用途**：查看所有的历史版本
**使用时机**：想知道之前做了什么，或需要回退时

---

### 5. 查看修改内容 ⭐⭐⭐⭐
```bash
# 查看工作区的修改（还没 add 的）
git diff

# 查看暂存区的修改（已经 add 但没 commit 的）
git diff --staged

# 查看某个文件的修改
git diff array_practice.py
```
**用途**：详细查看你改了什么
**使用时机**：提交前检查，或者想知道自己改了什么

---

### 6. 撤销修改 ⭐⭐⭐
```bash
# 撤销工作区的修改（还没 add）
git checkout -- array_practice.py

# 从暂存区移除（已经 add 但想撤回）
git reset HEAD array_practice.py

# 撤销上一次提交（保留修改）
git reset --soft HEAD~1

# 撤销上一次提交（删除修改，危险！）
git reset --hard HEAD~1
```
**用途**：改错了想恢复
**使用时机**：发现修改有问题时

---

### 7. 回到历史版本 ⭐⭐⭐
```bash
# 查看历史提交
git log --oneline

# 回到某个版本（假设版本号是 7a6f8d8）
git checkout 7a6f8d8

# 回到最新版本
git checkout main
```
**用途**：查看或恢复历史版本
**使用时机**：想看之前的代码是什么样子

---

## 🌳 分支管理（进阶）

### 什么时候用分支？
- 想尝试新算法，但不确定是否有效
- 想同时进行多个练习，互不干扰
- 想保留主分支的稳定代码

### 常用分支命令
```bash
# 查看所有分支
git branch

# 创建新分支
git branch feature-quicksort

# 切换到分支
git checkout feature-quicksort

# 创建并切换（合并上面两步）
git checkout -b feature-quicksort

# 合并分支到当前分支
git merge feature-quicksort

# 删除分支
git branch -d feature-quicksort
```

---

## 📝 推荐的工作流程

### 每天开始学习时：
```bash
git status          # 检查状态
```

### 完成一个小练习后：
```bash
git status          # 查看修改了什么
git add .           # 添加所有修改
git commit -m "完成XX算法练习"  # 提交
```

### 想尝试新方法时：
```bash
git checkout -b experiment  # 创建实验分支
# ... 尝试新代码 ...
git add .
git commit -m "尝试新方法"

# 如果成功，合并回主分支
git checkout main
git merge experiment

# 如果失败，直接切回主分支
git checkout main
git branch -d experiment  # 删除实验分支
```

---

## ⚠️ 常见问题

### Q1: 修改了文件后忘记提交，怎么办？
```bash
git status          # 查看修改
git add .           # 添加修改
git commit -m "补充提交说明"
```

### Q2: 提交信息写错了怎么办？
```bash
# 修改最后一次提交的信息
git commit --amend -m "新的提交信息"
```

### Q3: 不小心删除了文件，如何恢复？
```bash
# 如果还没提交
git checkout -- 文件名

# 如果已经提交了
git log --oneline    # 找到删除前的版本号
git checkout 版本号 -- 文件名
```

### Q4: 想放弃所有修改，回到上次提交的状态
```bash
# 危险操作！会删除所有未提交的修改
git reset --hard HEAD
```

### Q5: 查看某个文件在某个版本的内容
```bash
git show 版本号:文件路径
# 例如：git show 7a6f8d8:array_practice.py
```

---

## 🎨 提交信息的最佳实践

### 好的提交信息格式：
```
类型: 简短描述（50字以内）

详细说明（可选）
```

### 常用类型：
- `feat:` 新功能（新算法实现）
- `fix:` 修复 bug
- `docs:` 文档修改
- `refactor:` 重构代码
- `test:` 添加测试
- `style:` 代码格式调整

### 示例：
```bash
git commit -m "feat: 实现快速排序算法"
git commit -m "fix: 修复二分查找的越界问题"
git commit -m "refactor: 优化冒泡排序的时间复杂度"
git commit -m "docs: 添加算法时间复杂度说明"
```

---

## 💡 给算法学习者的建议

### 提交频率建议：
- ✅ 每完成一个算法就提交一次
- ✅ 每修复一个 bug 就提交一次
- ✅ 每天学习结束前至少提交一次
- ❌ 不要几天的修改一次性提交
- ❌ 不要提交到一半的、不能运行的代码

### 分支使用建议：
```
main 分支：保持稳定的、已经理解的算法
├── array-algorithms：数组相关练习
├── sorting：排序算法专题
├── search：搜索算法专题
└── experiment：临时实验
```

### 提交信息建议：
```bash
# 好的示例
git commit -m "完成数组二分查找，时间复杂度O(log n)"
git commit -m "学习快速排序的分治思想"
git commit -m "优化冒泡排序，添加提前终止条件"

# 不好的示例
git commit -m "修改"
git commit -m "test"
git commit -m "aaa"
```

---

## 🚀 快速参考表

| 命令 | 作用 | 使用频率 |
|------|------|----------|
| `git status` | 查看状态 | ⭐⭐⭐⭐⭐ |
| `git add .` | 添加所有修改 | ⭐⭐⭐⭐⭐ |
| `git commit -m "说明"` | 提交 | ⭐⭐⭐⭐⭐ |
| `git log --oneline` | 查看历史 | ⭐⭐⭐⭐ |
| `git diff` | 查看修改 | ⭐⭐⭐⭐ |
| `git checkout -b 分支名` | 创建并切换分支 | ⭐⭐⭐ |
| `git merge 分支名` | 合并分支 | ⭐⭐⭐ |
| `git reset --soft HEAD~1` | 撤销提交 | ⭐⭐ |

---

## 📚 进一步学习

当你熟悉了基本操作后，可以学习：
1. **远程仓库**：GitHub / GitLab / Gitee
2. **协作开发**：pull request、code review
3. **高级操作**：rebase、cherry-pick、stash
4. **Git 图形界面工具**：SourceTree、GitKraken

---

**记住**：
- Git 不会自动保存，要主动 commit
- 提交信息要写清楚，给未来的自己看
- 遇到问题先 `git status`，90% 的问题都能找到答案
- 不要害怕尝试，Git 很难真正"搞坏"代码

**祝学习愉快！** 🎓

