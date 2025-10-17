# 算法学习环境使用指南

## 📦 环境信息

- **环境名称**: `algo`
- **Python 版本**: 3.10.19
- **用途**: 专门用于算法和数据结构学习

---

## 🚀 如何使用环境

### 1. 激活环境

在终端中运行：

```bash
conda activate algo
```

激活后，你的终端提示符前面会显示 `(algo)`，表示环境已激活。

### 2. 验证 Python 版本

```bash
python --version
# 应该显示: Python 3.10.19
```

### 3. 运行 Python 文件

```bash
# 激活环境后，直接用 python 命令（不需要 python3）
python array_practice.py
```

### 4. 退出环境

```bash
conda deactivate
```

---

## 📚 已重命名的文件

- ❌ `array.py` → ✅ `array_practice.py`

**为什么要重命名？**
- `array` 是 Python 的内置模块名
- 用内置模块名命名文件会导致导入冲突
- **避免使用的文件名**: `list.py`, `dict.py`, `str.py`, `sys.py`, `os.py` 等

---

## 💡 常用命令速查

| 命令 | 说明 |
|------|------|
| `conda activate algo` | 激活 algo 环境 |
| `conda deactivate` | 退出当前环境 |
| `conda env list` | 查看所有环境 |
| `conda list` | 查看已安装的包 |
| `conda install 包名` | 安装包 |
| `pip install 包名` | 用 pip 安装包 |

---

## 📦 安装常用算法库（可选）

激活环境后，可以安装一些常用的库：

```bash
conda activate algo

# 安装 numpy（数组运算）
pip install numpy

# 安装 matplotlib（画图）
pip install matplotlib

# 安装 jupyter（笔记本）
pip install jupyter

# 安装 pytest（测试）
pip install pytest
```

---

## 🎯 学习建议

1. **每次练习前先激活环境**：
   ```bash
   conda activate algo
   cd /Users/fgg/Library/CloudStorage/SynologyDrive-SerendiFuFu/code/Data_structures_and_algorithms
   ```

2. **文件命名规范**：
   - ✅ `array_practice.py`, `linked_list.py`, `tree_exercise.py`
   - ❌ `array.py`, `list.py`, `dict.py`

3. **代码组织**：
   - 每个数据结构一个文件
   - 使用注释记录学习笔记
   - 保留测试用例

---

## 📝 示例：完整工作流程

```bash
# 1. 打开终端，激活环境
conda activate algo

# 2. 进入学习目录
cd /Users/fgg/Library/CloudStorage/SynologyDrive-SerendiFuFu/code/Data_structures_and_algorithms

# 3. 运行练习文件
python array_practice.py

# 4. 完成后退出环境
conda deactivate
```

---

## ⚠️ 注意事项

1. **环境隔离**：在 `algo` 环境中安装的包不会影响其他环境
2. **始终激活**：运行算法代码前记得激活环境
3. **避免冲突**：不要用 Python 内置模块名命名文件

---

## 🆘 常见问题

### Q: 忘记是否激活了环境？
**A**: 看终端提示符，有 `(algo)` 就是激活了

### Q: 想删除环境怎么办？
**A**: `conda env remove -n algo`

### Q: 如何查看环境的 Python 路径？
**A**: `which python`（激活环境后）

---

Happy Coding! 🎉

