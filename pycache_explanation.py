"""
__pycache__ 详解
"""

print("=" * 70)
print("什么是 __pycache__？")
print("=" * 70)
print("""
__pycache__ 是 Python 自动创建的缓存文件夹，用于存放编译后的
字节码文件（.pyc 文件）。

📊 工作原理：

  你写的代码.py    →    Python解释器    →    运行
       │                                        
       ↓ (第一次运行时编译)                     
  编译后的.pyc     →    保存到 __pycache__     
       │                                        
       ↓ (下次运行时直接用)                    
  跳过编译步骤     →    运行更快！             
""")

print("=" * 70)
print("为什么会出现？")
print("=" * 70)
print("""
Python 运行时的两个步骤：
  1. 编译：把 .py 文件编译成字节码（.pyc）
  2. 执行：运行字节码

为了提速，Python 会：
  ✅ 第一次运行：编译 .py → 保存 .pyc 到 __pycache__
  ✅ 第二次运行：直接用 .pyc，跳过编译步骤
  
这样第二次运行会更快！
""")

print("=" * 70)
print("文件命名规则")
print("=" * 70)
print("""
__pycache__/array.cpython-310.pyc
            │      │       │   │
            │      │       │   └─ 扩展名（Python compiled）
            │      │       └───── Python 版本（3.10）
            │      └───────────── CPython（Python 解释器类型）
            └──────────────────── 原文件名

所以：
  array.py → __pycache__/array.cpython-310.pyc
  test.py  → __pycache__/test.cpython-310.pyc
""")

print("=" * 70)
print("需要删除吗？")
print("=" * 70)
print("""
❌ 不需要手动删除！

理由：
  1. Python 会自动管理这些文件
  2. 删除后下次运行会重新生成
  3. 不会影响代码运行
  4. 可以提高运行速度

⚠️ 什么时候删除？
  1. 清理项目时（可选）
  2. 代码要打包分享时（.pyc 是机器码，不便阅读）
  3. 版本控制时（应该在 .gitignore 中忽略）
""")

print("=" * 70)
print("如何避免提交到 Git？")
print("=" * 70)
print("""
在项目根目录创建或编辑 .gitignore 文件，添加：

  __pycache__/
  *.pyc
  *.pyo
  *.pyd

这样 Git 就会忽略这些文件，不会提交到仓库。
""")

print("=" * 70)
print("总结")
print("=" * 70)
print("""
🎯 关键点：

1. __pycache__ 是什么？
   → Python 自动生成的缓存文件夹

2. 为什么会出现？
   → 为了提高第二次运行的速度

3. 需要关心吗？
   → 不需要，让 Python 自动管理就好

4. 要删除吗？
   → 不需要，但可以安全删除（会重新生成）

5. 要提交到 Git 吗？
   → 不要！添加到 .gitignore

📌 记忆技巧：
  __pycache__ = Python 的"工作笔记"
  就像你做数学题时的草稿纸，下次做题时可以参考，
  但不需要交给老师（不提交到 Git）
""")
print("=" * 70)

