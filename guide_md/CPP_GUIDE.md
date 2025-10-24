# C++ 配置和使用指南

## 一、环境检查

你的 Mac 上已经安装了 **Apple Clang 16.0.0** 编译器，无需额外安装！

### 验证安装
```bash
# 查看编译器路径
which clang++

# 查看编译器版本
clang++ --version
```

## 二、如何编译和运行C++程序

### 方法1：最简单的方式（推荐新手）

假设你的C++文件名叫 `test.cpp`

```bash
# 1. 编译：把源代码变成可执行程序
clang++ test.cpp -o test

# 2. 运行：执行编译好的程序
./test
```

**解释：**
- `clang++`：C++编译器的名字
- `test.cpp`：你写的源代码文件
- `-o test`：`-o` 表示 output（输出），`test` 是你想要的可执行文件名
- `./test`：运行当前目录（`.`）下的 `test` 程序

### 方法2：分步编译（了解编译过程）

```bash
# 第1步：编译成目标文件（.o文件）
clang++ -c test.cpp -o test.o

# 第2步：链接成可执行文件
clang++ test.o -o test

# 第3步：运行
./test
```

### 方法3：带优化和调试信息

```bash
# 调试模式：包含调试信息，方便找bug
clang++ -g test.cpp -o test_debug

# 优化模式：运行更快，但不方便调试
clang++ -O2 test.cpp -o test_release

# C++标准版本（推荐使用C++17或C++20）
clang++ -std=c++17 test.cpp -o test
```

**常用编译选项：**
- `-g`：包含调试信息
- `-O0`：不优化（默认，编译快）
- `-O1`, `-O2`, `-O3`：不同级别的优化（运行快）
- `-std=c++17`：使用C++17标准
- `-std=c++20`：使用C++20标准
- `-Wall`：显示所有警告
- `-Werror`：把警告当作错误

## 三、完整示例演示

### 1. 创建一个简单的C++文件

创建文件 `hello.cpp`：
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, C++!" << endl;
    return 0;
}
```

### 2. 编译并运行

```bash
# 切换到文件所在目录
cd /你的文件路径/

# 编译
clang++ hello.cpp -o hello

# 运行
./hello
```

你会看到输出：
```
Hello, C++!
```

## 四、常见问题和解决方案

### Q1: 报错 "command not found: clang++"

**解决方案：** 安装 Xcode Command Line Tools
```bash
xcode-select --install
```

### Q2: 报错 "permission denied"

**原因：** 文件没有执行权限

**解决方案：**
```bash
# 给文件添加执行权限
chmod +x 你的程序名

# 然后运行
./你的程序名
```

### Q3: 中文输出乱码

**解决方案：** 确保：
1. 源文件保存为 UTF-8 编码
2. 终端支持中文显示（Mac 终端默认支持）

### Q4: 找不到头文件 (如 #include <bits/stdc++.h>)

**原因：** `bits/stdc++.h` 是 GCC 特有的，Mac 的 Clang 不支持

**解决方案：** 分别包含需要的头文件
```cpp
// 不要用
#include <bits/stdc++.h>  // ❌

// 应该用
#include <iostream>        // ✅
#include <vector>          // ✅
#include <string>          // ✅
// ... 按需包含
```

## 五、在 VSCode 中配置C++（可选）

如果你使用 VSCode 编辑器，可以安装以下插件：
1. **C/C++** (Microsoft 出品)
2. **Code Runner** (方便一键运行)

### 配置 Code Runner

在 VSCode 设置中搜索 `code-runner.executorMap`，添加：
```json
{
    "cpp": "cd $dir && clang++ -std=c++17 $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt"
}
```

这样就可以按 `Ctrl + Alt + N` (或右键选择 Run Code) 一键运行C++程序！

## 六、数据结构与算法的C++模板

### LeetCode 风格模板

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    // 在这里写你的算法
    int example(vector<int>& nums) {
        // 你的代码
        return 0;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 2, 3, 4, 5};
    int result = sol.example(nums);
    cout << "Result: " << result << endl;
    return 0;
}
```

### 编译运行命令

```bash
# 基础编译
clang++ solution.cpp -o solution && ./solution

# 带C++17标准和警告
clang++ -std=c++17 -Wall solution.cpp -o solution && ./solution

# 调试模式
clang++ -std=c++17 -g -Wall solution.cpp -o solution && ./solution
```

## 七、学习建议

1. **从简单开始**：先运行 `test_hello.cpp` 确保环境正常
2. **逐步学习**：掌握基本语法后再学数据结构
3. **多动手**：每学一个概念就写代码测试
4. **参考资料**：
   - [cppreference.com](https://zh.cppreference.com/) - C++官方参考文档（有中文）
   - [LeetCode](https://leetcode.cn/) - 刷题练习

## 八、快速命令参考

```bash
# 编译并运行（最常用）
clang++ 文件名.cpp -o 程序名 && ./程序名

# 带标准和优化
clang++ -std=c++17 -O2 文件名.cpp -o 程序名 && ./程序名

# 删除编译产物
rm 程序名

# 查看文件
ls -la
```

---

## 需要帮助？

如果遇到问题：
1. 仔细看错误信息（通常会告诉你哪一行有问题）
2. 检查语法错误（分号、括号等）
3. 确认文件路径是否正确
4. 随时问我！

