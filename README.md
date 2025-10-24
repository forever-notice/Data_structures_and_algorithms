# 数据结构与算法学习仓库

## 📦 环境信息

- **环境名称**: `algo`
- **Python 版本**: 3.10.19
- **C++ 编译器**: Apple Clang 16.0.0
- **用途**: 专门用于算法和数据结构学习（支持Python和C++）

---

## 📁 目录结构

```
Data_structures_and_algorithms/
├── 📂 ch01/              # 课程第1章练习
├── 📂 cpp_examples/      # C++示例代码
│   ├── test_hello.cpp
│   ├── cpp_template.cpp
│   └── README.md
├── 📂 leetcode/          # LeetCode刷题练习
│   ├── leetcode_template.py
│   ├── leetcode_724_两个版本.py
│   └── README.md
├── 📂 expla/             # 概念解释文件
│   ├── class_and_self_complete.py
│   ├── class_vs_function_explanation.py
│   └── ...
├── 📂 guide_md/          # 各种配置指南
│   ├── CPP_GUIDE.md      # C++配置指南
│   ├── GIT_GUIDE.md
│   ├── GITHUB_SETUP.md
│   └── ...
├── 📂 getrid/            # 待整理的代码
├── 📂 psadspy-src/       # 教材配套资源
│   ├── Figures/          # 图示资源
│   ├── Listings/         # 代码清单
│   └── Slides/           # 课件
├── 📂 贪心算法/          # 贪心算法专题
└── README.md             # 本文件
```

---

## 💡 常用命令速查

### Python 相关
| 命令 | 说明 |
|------|------|
| `python3 文件名.py` | 运行Python程序 |
| `conda env list` | 查看所有环境 |
| `conda list` | 查看已安装的包 |

### C++ 相关
| 命令 | 说明 |
|------|------|
| `clang++ 文件.cpp -o 程序名` | 编译C++程序 |
| `./程序名` | 运行编译好的程序 |
| `clang++ -std=c++17 文件.cpp -o 程序名 && ./程序名` | 编译并运行 |

### Git 相关
| 命令 | 说明 |
|------|------|
| `git status` | 查看文件状态 |
| `git add .` | 添加所有修改 |
| `git commit -m "描述"` | 提交修改 |
| `git push` | 推送到远程仓库 |

---

## 🎯 学习建议

1. **每次练习前先激活环境**：

2. **文件命名规范**：
   - ✅ `array_practice.py`, `linked_list.py`, `tree_exercise.py`
   - ❌ `array.py`, `list.py`, `dict.py`

3. **代码组织**：
   - 每个数据结构一个文件
   - 使用注释记录学习笔记
   - 保留测试用例

---

## 🆘 常见问题
### Q: 想删除环境怎么办？
**A**: `conda env remove -n algo`

### Q: 如何查看环境的 Python 路径？
**A**: `which python`（激活环境后）

---

Happy Coding! 🎉
一个半月直接拿下✊

