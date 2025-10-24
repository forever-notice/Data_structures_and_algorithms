# C++ 示例代码

这个目录存放C++学习和练习代码。

## 📁 文件说明

- `test_hello.cpp` - C++ Hello World 示例
- `cpp_template.cpp` - 数据结构与算法模板（包含LeetCode 724示例）

## 🚀 如何运行

### 编译单个文件
```bash
clang++ 文件名.cpp -o 程序名
```

### 编译并运行（推荐）
```bash
clang++ -std=c++17 文件名.cpp -o 程序名 && ./程序名
```

### 示例
```bash
# 运行 Hello World
clang++ test_hello.cpp -o test_hello && ./test_hello

# 运行算法模板
clang++ -std=c++17 cpp_template.cpp -o cpp_template && ./cpp_template
```

## 📝 注意事项

1. **编译产物不要提交到Git**：`.gitignore` 已配置忽略可执行文件
2. **推荐使用C++17或更高版本**：`-std=c++17`
3. **查看详细指南**：参考 `../guide_md/CPP_GUIDE.md`

## 🔗 相关资源

- [CPP_GUIDE.md](../guide_md/CPP_GUIDE.md) - 详细的C++配置指南
- [cppreference.com](https://zh.cppreference.com/) - C++官方参考文档

