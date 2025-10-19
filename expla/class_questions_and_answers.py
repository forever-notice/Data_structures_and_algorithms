"""
class 和 self 的三大核心问题 + 练习题详解
=========================================
每个问题都有详细的解释、示例和运行结果
"""

print("=" * 60)
print("问题1：为什么 self.name = name 中两个 name 不一样？")
print("=" * 60)

"""
这是新手最容易困惑的问题！
让我们一步一步拆解：
"""

class Dog:
    def __init__(self, name):
        # 等号左边的 self.name：存储在对象身上的属性
        # 等号右边的 name：方法接收到的参数
        self.name = name

# 用图解方式理解
print("\n【详细分析】")
print("""
当你写：xiaobai = Dog("小白")

步骤1：Python 调用 __init__(self, name)
       - self 变成了 xiaobai 这个对象
       - name 变成了字符串 "小白"

步骤2：执行 self.name = name
       - 右边的 name：就是参数 "小白"
       - 左边的 self.name：把 "小白" 存到 xiaobai 对象上
       
可以想象成：
       xiaobai.name = "小白"
""")

# 实际演示
class DetailedDog:
    def __init__(self, dog_name):  # 参数名改成 dog_name 更清楚
        print(f"1. 收到参数 dog_name = '{dog_name}'")
        self.name = dog_name  # 把参数保存到对象的 name 属性上
        print(f"2. 保存到 self.name = '{self.name}'")
        print(f"3. 参数 dog_name 和 self.name 现在都是: '{dog_name}' 和 '{self.name}'")

print("\n【实际运行】")
xiaobai = DetailedDog("小白")

# 更清楚的对比
print("\n【关键对比】")
class CompareExample:
    def __init__(self, x):
        # 情况1：保存到对象上（用 self）
        self.x = x  # ✅ 这样保存后，对象可以一直用
        
        # 情况2：只是局部变量（不用 self）
        y = x  # ❌ 这个 y 只在 __init__ 里有效，出了方法就没了
    
    def test(self):
        print(f"self.x 可以访问: {self.x}")  # ✅ 能访问
        # print(f"y 可以访问吗: {y}")  # ❌ 会报错！y 不存在

obj = CompareExample(100)
obj.test()

print("\n【记忆技巧】")
print("""
self.变量名 = 参数
     ↓         ↓
   存到这里   从这里拿

想象成：
- 左边是「保存的地方」（对象的属性）
- 右边是「数据来源」（参数、计算结果等）

就像：
- 书架.书 = 新买的书
  把新买的书放到书架上
""")


print("\n\n" + "=" * 60)
print("问题2：什么时候用 self，什么时候不用？")
print("=" * 60)

"""
这个问题非常重要！搞懂这个，就能避免 90% 的错误。
"""

print("\n【核心规则】")
print("""
✅ 必须用 self 的情况：
   1. 想保存数据，让其他方法也能用
   2. 想调用这个对象的其他方法
   3. 访问这个对象的属性

❌ 不用 self 的情况：
   1. 临时变量，用完就扔
   2. 方法内部的计算过程
   3. 局部的循环变量
""")

class Calculator:
    """计算器示例：什么时候用 self"""
    
    def __init__(self):
        # ✅ 用 self：需要保存历史记录
        self.history = []  # 所有方法都能访问
        self.count = 0     # 所有方法都能访问
    
    def add(self, a, b):
        # ❌ 不用 self：临时计算结果
        result = a + b  # 只在这个方法里用
        
        # ✅ 用 self：保存到历史
        self.history.append(result)
        self.count += 1
        
        # ❌ 不用 self：临时消息
        message = f"{a} + {b} = {result}"
        print(message)
        
        return result
    
    def show_history(self):
        # ✅ 用 self：访问保存的数据
        print(f"总共计算了 {self.count} 次")
        print(f"历史记录: {self.history}")
        
        # ❌ 不用 self：循环变量
        for i in range(len(self.history)):  # i 是临时变量
            print(f"  第 {i+1} 次: {self.history[i]}")

print("\n【实际演示】")
calc = Calculator()
calc.add(10, 20)
calc.add(30, 40)
calc.show_history()

print("\n【决策流程图】")
print("""
需要保存数据吗？
    ├─ 是 → 用 self.变量名
    └─ 否 → 用 变量名

需要在其他方法用吗？
    ├─ 是 → 用 self.变量名
    └─ 否 → 用 变量名

是临时计算吗？
    ├─ 是 → 用 变量名
    └─ 否 → 用 self.变量名
""")

print("\n【常见例子对比】")

class GoodExample:
    """正确使用 self 的例子"""
    
    def __init__(self, name):
        self.name = name  # ✅ 需要保存
        self.score = 0    # ✅ 需要保存
    
    def add_score(self, points):
        old_score = self.score  # ❌ 临时变量，用完就扔
        self.score += points    # ✅ 更新保存的数据
        
        # ❌ 临时变量
        difference = self.score - old_score
        print(f"{self.name} 增加了 {difference} 分，现在是 {self.score} 分")

print("\n正确示例：")
player = GoodExample("玩家1")
player.add_score(10)
player.add_score(5)


print("\n\n" + "=" * 60)
print("问题3：LeetCode 的 self 到底有什么用？")
print("=" * 60)

"""
这是很多人刷题时的疑惑！
答案可能会让你惊讶...
"""

print("\n【真相】")
print("""
在大多数简单的 LeetCode 题目中：
self 其实没什么用！😅

为什么还要用？
→ 因为 LeetCode 平台要求统一格式！
→ 方便平台自动测试
→ 让你适应面向对象编程
""")

from typing import List

# 示例1：简单题目，self 没啥用
class Solution1:
    """简单题目：self 可有可无"""
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 这题完全不需要 self，但格式要求必须写
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

print("\n【简单题目示例】")
sol1 = Solution1()
result = sol1.twoSum([2, 7, 11, 15], 9)
print(f"两数之和: {result}")
print("↑ 这题 self 完全没用到，只是格式要求")


# 示例2：复杂题目，self 很有用
class Solution2:
    """复杂题目：self 很有用！"""
    
    def __init__(self):
        # 可以初始化一些辅助数据
        self.memo = {}  # 用于记忆化
    
    def fibonacci(self, n: int) -> int:
        """斐波那契数列（用 self 优化）"""
        # 用 self.memo 保存计算结果，避免重复计算
        if n in self.memo:
            return self.memo[n]
        
        if n <= 1:
            return n
        
        # 递归计算
        result = self.fibonacci(n - 1) + self.fibonacci(n - 2)
        
        # ✅ 用 self 保存结果
        self.memo[n] = result
        return result
    
    def helper_sum(self, nums: List[int]) -> int:
        """辅助方法"""
        return sum(nums)
    
    def main_method(self, nums: List[int]) -> int:
        """主方法：调用辅助方法"""
        # ✅ 用 self 调用其他方法
        total = self.helper_sum(nums)
        return total * 2

print("\n【复杂题目示例】")
sol2 = Solution2()
print(f"斐波那契数列第10项: {sol2.fibonacci(10)}")
print(f"使用了 self.memo 来优化性能")
print(f"调用其他方法: {sol2.main_method([1, 2, 3])}")

print("\n【LeetCode 的 self 使用场景】")
print("""
❌ 简单题目（90%）：
   - self 基本用不到
   - 只是格式要求
   - 专注算法本身就行
   
✅ 复杂题目（10%）：
   - 需要辅助方法（self.helper()）
   - 需要记忆化（self.memo）
   - 需要保存中间状态
   
✅ 设计题（Design）：
   - 设计数据结构
   - 需要保存状态
   - self 非常重要！
""")

print("\n【实战建议】")
print("""
刷 LeetCode 时：
1. 复制题目的 class 模板
2. 在方法里写你的算法
3. 不用想 self 是什么，自动忽略它
4. 只有需要辅助方法或保存数据时才用 self

比如：
class Solution:
    def solve(self, nums: List[int]) -> int:
        # 在这里写你的算法
        result = 0
        for num in nums:
            result += num
        return result
        
就这么简单！
""")


print("\n\n" + "=" * 60)
print("练习题1：学生类 - 详细解析")
print("=" * 60)

"""
让我们一行一行分析学生类的代码
"""

class Student:
    """学生类"""
    
    def __init__(self, name, age, score):
        """
        初始化方法：创建学生时自动调用
        
        参数分析：
        - self: 代表这个学生对象本身（Python 自动传入）
        - name: 学生姓名（你传入的）
        - age: 学生年龄（你传入的）
        - score: 学生成绩（你传入的）
        """
        # 把参数保存到对象上，这样其他方法也能用
        self.name = name    # 把姓名存到这个学生对象上
        self.age = age      # 把年龄存到这个学生对象上
        self.score = score  # 把成绩存到这个学生对象上
        
        print(f"→ 创建了学生对象：{name}")
    
    def show_info(self):
        """
        显示学生信息
        
        注意：
        - 只有一个参数 self（必须的）
        - 不需要其他参数，因为数据已经保存在 self 上了
        """
        # 用 self.xxx 访问保存的数据
        print(f"姓名: {self.name}, 年龄: {self.age}, 成绩: {self.score}")
    
    def is_pass(self):
        """
        判断是否及格
        
        返回值：
        - True: 及格
        - False: 不及格
        """
        # 用 self.score 访问这个学生的成绩
        if self.score >= 60:
            print(f"{self.name} 及格了！🎉")
            return True
        else:
            print(f"{self.name} 不及格... 😢")
            return False
    
    def improve_score(self, points):
        """
        加分方法（额外示例）
        
        参数：
        - points: 要加多少分
        """
        old_score = self.score  # 记录旧成绩（临时变量）
        self.score += points    # 更新成绩（保存到 self）
        print(f"{self.name} 的成绩从 {old_score} 提升到 {self.score}")

print("\n【使用示例】")

# 步骤1：创建两个学生对象
print("\n1. 创建学生：")
xiaoming = Student("小明", 18, 85)  # Python 自动把 xiaoming 传给 self
xiaohong = Student("小红", 17, 55)  # Python 自动把 xiaohong 传给 self

# 步骤2：显示信息
print("\n2. 显示信息：")
xiaoming.show_info()  # 等价于 Student.show_info(xiaoming)
xiaohong.show_info()  # 等价于 Student.show_info(xiaohong)

# 步骤3：检查是否及格
print("\n3. 检查是否及格：")
xiaoming.is_pass()
xiaohong.is_pass()

# 步骤4：小红努力学习，成绩提升了！
print("\n4. 小红努力学习：")
xiaohong.improve_score(10)  # 加10分
xiaohong.show_info()
xiaohong.is_pass()  # 再次检查

print("\n【关键要点】")
print("""
1. __init__ 的作用：
   - 创建对象时自动调用
   - 用来初始化（设置初始值）
   - 把数据保存到 self 上

2. 为什么用 self：
   - self.name：小明有自己的名字，小红也有自己的名字
   - self.score：每个学生都有自己的成绩
   - 用 self 保存，互不干扰！

3. 调用方法时：
   - xiaoming.show_info()
   - Python 自动把 xiaoming 传给 self
   - 所以 self.name 就是小明的名字
""")


print("\n\n" + "=" * 60)
print("练习题2：银行账户类 - 详细解析")
print("=" * 60)

"""
银行账户是理解 self 的最佳例子！
每个账户都有自己的余额，互不影响。
"""

class BankAccount:
    """银行账户类"""
    
    def __init__(self, owner):
        """
        创建账户
        
        参数：
        - owner: 账户所有人
        """
        self.owner = owner    # 账户所有人（用 self 保存）
        self.balance = 0      # 初始余额为 0（用 self 保存）
        
        # 临时消息（不用 self）
        message = f"账户创建成功！户主: {self.owner}"
        print(message)
    
    def deposit(self, amount):
        """
        存钱
        
        参数：
        - amount: 存入金额
        """
        # 更新余额（用 self 保存）
        self.balance += amount
        
        # 显示信息
        print(f"存入 {amount} 元，当前余额: {self.balance} 元")
    
    def withdraw(self, amount):
        """
        取钱
        
        参数：
        - amount: 取款金额
        
        返回值：
        - True: 取款成功
        - False: 余额不足
        """
        # 检查余额（用 self 访问）
        if amount > self.balance:
            print(f"余额不足！当前余额: {self.balance} 元，想取: {amount} 元")
            return False
        else:
            # 更新余额
            self.balance -= amount
            print(f"取出 {amount} 元，当前余额: {self.balance} 元")
            return True
    
    def check_balance(self):
        """查看余额"""
        print(f"{self.owner} 的当前余额: {self.balance} 元")
        return self.balance
    
    def transfer(self, other_account, amount):
        """
        转账（额外示例）
        
        参数：
        - other_account: 另一个 BankAccount 对象
        - amount: 转账金额
        """
        print(f"\n{self.owner} 向 {other_account.owner} 转账 {amount} 元...")
        
        # 先从自己账户取钱
        if self.withdraw(amount):
            # 再存到对方账户
            other_account.deposit(amount)
            print(f"转账成功！")
            return True
        else:
            print(f"转账失败：余额不足")
            return False

print("\n【使用示例】")

# 创建两个独立的银行账户
print("\n1. 创建账户：")
account_zhang = BankAccount("张三")
account_li = BankAccount("李四")

# 两个账户各自存钱
print("\n2. 存钱操作：")
account_zhang.deposit(1000)  # 张三存 1000
account_li.deposit(500)      # 李四存 500

# 查看余额
print("\n3. 查看余额：")
account_zhang.check_balance()
account_li.check_balance()

# 取钱
print("\n4. 取钱操作：")
account_zhang.withdraw(300)   # 张三取 300，成功
account_zhang.withdraw(800)   # 张三取 800，失败（余额不足）

# 转账
print("\n5. 转账操作：")
account_zhang.transfer(account_li, 500)  # 张三给李四转 500

# 最终余额
print("\n6. 最终余额：")
account_zhang.check_balance()
account_li.check_balance()

print("\n【关键要点】")
print("""
1. self 的威力：
   - account_zhang.balance: 张三的余额
   - account_li.balance: 李四的余额
   - 两个账户完全独立！

2. 为什么需要 self：
   - 每个账户都有自己的余额
   - 不用 self 的话，所有人共用一个余额（乱套了！）

3. 方法之间共享数据：
   - withdraw() 修改 self.balance
   - check_balance() 读取 self.balance
   - 都是操作同一个对象的数据

4. 对象交互：
   - transfer() 方法中
   - self 是自己的账户
   - other_account 是别人的账户
   - 可以访问 other_account.owner 和 other_account.balance
""")


print("\n\n" + "=" * 60)
print("总结：三个问题 + 两个练习题")
print("=" * 60)

print("""
🎯 问题1：self.name = name 的区别
   - 左边 self.name：保存的地方（对象的属性）
   - 右边 name：数据来源（参数）
   - 就像：书架.书 = 新买的书

🎯 问题2：何时用 self
   - 需要保存数据 → 用 self
   - 临时变量 → 不用 self
   - 要在其他方法用 → 用 self

🎯 问题3：LeetCode 的 self
   - 简单题：self 没用，只是格式要求
   - 复杂题：self 用于辅助方法、记忆化
   - 设计题：self 很重要！

🏋️ 练习1：学生类
   - 每个学生有自己的姓名、年龄、成绩
   - 用 self 保存，互不干扰

🏋️ 练习2：银行账户
   - 每个账户有自己的余额
   - 账户之间可以转账
   - 完美展示了 self 的作用

💡 核心思想：
   - class 是模板，对象是实例
   - self 就是「这个对象本身」
   - 用 self 保存数据，对象之间互不影响
""")

print("\n🎉 恭喜！你已经完全掌握了 class 和 self！")
print("\n下一步建议：")
print("  1. 自己动手写一个「图书类」（Book）")
print("  2. 写一个「购物车类」（ShoppingCart）")
print("  3. 去 LeetCode 找一道设计题试试")

