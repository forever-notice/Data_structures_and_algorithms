"""
class 和 self 完全教程
======================
让我们从零开始，彻底搞懂 class 和 self！
"""

# ==========================================
# 第一部分：class 是什么？
# ==========================================

"""
🏠 用造房子来理解 class

想象一下：
- class 是「房子的设计图纸」
- 根据图纸可以建造「真实的房子」
- 每个房子都有自己的「家具、颜色、主人」

class = 设计图纸
对象(object) = 根据图纸建造的真实房子
"""

# 最简单的 class 例子
class Dog:
    """这是狗的设计图纸"""
    pass  # pass 表示暂时什么都不写

# 根据设计图纸，造两只真实的狗
dog1 = Dog()  # 创建第一只狗
dog2 = Dog()  # 创建第二只狗

print("="*50)
print("第一部分：理解 class")
print("="*50)
print(f"dog1 是一个对象: {dog1}")
print(f"dog2 是一个对象: {dog2}")
print(f"它们是同一只狗吗? {dog1 == dog2}")  # False，是两只不同的狗
print()


# ==========================================
# 第二部分：self 是什么？
# ==========================================

"""
🤔 self 的本质：self 就是「我自己」

当你创建一只狗，狗需要知道：
- 「我」叫什么名字？
- 「我」多大了？
- 「我」是什么颜色？

self 就是这个「我」！
"""

class Dog2:
    """带有属性的狗"""
    
    def __init__(self, name, age):
        """
        __init__ 是「初始化方法」（构造函数）
        当你创建狗时，这个方法会自动运行
        
        参数说明：
        - self: 代表「这只狗自己」
        - name: 你给狗起的名字
        - age: 狗的年龄
        """
        self.name = name  # 把名字存到「我自己」身上
        self.age = age    # 把年龄存到「我自己」身上

# 创建两只不同的狗
dog_a = Dog2("小白", 3)  # Python 自动把 dog_a 传给 self
dog_b = Dog2("小黑", 5)  # Python 自动把 dog_b 传给 self

print("="*50)
print("第二部分：理解 self")
print("="*50)
print(f"狗A的名字: {dog_a.name}, 年龄: {dog_a.age}")
print(f"狗B的名字: {dog_b.name}, 年龄: {dog_b.age}")
print()


# ==========================================
# 第三部分：self 的工作原理（重点！）
# ==========================================

"""
💡 self 是如何工作的？

当你写：
    dog_a = Dog2("小白", 3)

Python 实际上做了这些事：
    1. 创建一个新的 Dog2 对象
    2. 把这个新对象赋值给 self
    3. 调用 __init__(self, "小白", 3)
    4. 把 self 返回给 dog_a

所以：dog_a 就是 self！
"""

class DetailedDog:
    """详细展示 self 的工作过程"""
    
    def __init__(self, name):
        print(f"  → __init__ 被调用了！")
        print(f"  → self 是: {self}")
        print(f"  → 现在给 self 添加 name 属性...")
        self.name = name
        print(f"  → self.name 现在是: {self.name}")
    
    def bark(self):
        """
        这是一个「方法」（method）
        每只狗都可以调用这个方法
        """
        print(f"  → bark() 被调用了！")
        print(f"  → self 是: {self}")
        print(f"  → self.name 是: {self.name}")
        print(f"  → {self.name} 说: 汪汪汪！")

print("="*50)
print("第三部分：self 的工作原理")
print("="*50)
print("\n创建小白：")
xiaobai = DetailedDog("小白")

print("\n创建小黑：")
xiaohei = DetailedDog("小黑")

print("\n让小白叫：")
xiaobai.bark()

print("\n让小黑叫：")
xiaohei.bark()
print()


# ==========================================
# 第四部分：为什么必须写 self？
# ==========================================

"""
❓ 为什么每个方法都要写 self？

因为需要知道「是哪一只狗」！

当你写：
    xiaobai.bark()

Python 实际上会转换成：
    DetailedDog.bark(xiaobai)
    
看到了吗？xiaobai 被自动传给了 self！
"""

print("="*50)
print("第四部分：为什么要写 self")
print("="*50)

# 这两种写法完全等价：
print("\n方式1（常用）：")
xiaobai.bark()

print("\n方式2（理解原理）：")
DetailedDog.bark(xiaobai)  # 手动传入 self

print("\n看到了吗？两种方式效果一样！")
print("这就是为什么每个方法第一个参数必须是 self")
print()


# ==========================================
# 第五部分：实战案例 - 计数器
# ==========================================

"""
🎯 实战：用 class 做一个计数器

假设你要做一个计数器，要求：
1. 可以增加数字
2. 可以减少数字
3. 可以查看当前数字
4. 可以重置

用 class 怎么实现？
"""

class Counter:
    """一个简单的计数器"""
    
    def __init__(self):
        """初始化：计数从 0 开始"""
        self.count = 0  # 用 self.count 保存「我」的计数值
        print(f"计数器创建成功，初始值: {self.count}")
    
    def add(self, n=1):
        """增加 n（默认增加 1）"""
        self.count += n  # 修改「我自己」的 count
        print(f"  增加 {n}，当前值: {self.count}")
    
    def minus(self, n=1):
        """减少 n（默认减少 1）"""
        self.count -= n
        print(f"  减少 {n}，当前值: {self.count}")
    
    def show(self):
        """显示当前值"""
        print(f"  当前计数: {self.count}")
        return self.count
    
    def reset(self):
        """重置为 0"""
        self.count = 0
        print(f"  已重置，当前值: {self.count}")

print("="*50)
print("第五部分：实战 - 计数器")
print("="*50)

# 创建两个独立的计数器
counter1 = Counter()
counter2 = Counter()

print("\n操作计数器1：")
counter1.add()      # +1
counter1.add(5)     # +5
counter1.minus(2)   # -2
counter1.show()     # 显示: 4

print("\n操作计数器2：")
counter2.add(10)    # +10
counter2.show()     # 显示: 10

print("\n两个计数器互不影响！")
print(f"counter1: {counter1.count}")
print(f"counter2: {counter2.count}")
print()


# ==========================================
# 第六部分：LeetCode 中的 self
# ==========================================

"""
📝 LeetCode 中 self 的作用

在 LeetCode 题目中：
1. self 让你可以在方法之间共享数据
2. self 让你可以调用其他方法
"""

from typing import List

class Solution:
    """LeetCode 标准格式"""
    
    def pivotIndex(self, nums: List[int]) -> int:
        """
        主方法：寻找中心索引
        
        参数：
        - self: 代表这个 Solution 对象本身
        - nums: 输入的数组
        """
        # 调用辅助方法（通过 self 调用）
        total = self.calculate_sum(nums)
        
        curr_sum = 0
        for i in range(len(nums)):
            if curr_sum * 2 + nums[i] == total:
                return i
            curr_sum += nums[i]
        
        return -1
    
    def calculate_sum(self, nums: List[int]) -> int:
        """辅助方法：计算数组总和"""
        return sum(nums)

print("="*50)
print("第六部分：LeetCode 中的 self")
print("="*50)

sol = Solution()
result = sol.pivotIndex([1, 7, 3, 6, 5, 6])
print(f"中心索引: {result}")
print()


# ==========================================
# 第七部分：进阶 - 保存状态
# ==========================================

"""
🚀 self 的强大之处：保存状态

假设你要解决这样的问题：
- 每次调用函数时，记录调用次数
- 记录所有的历史输入
- 计算平均值

用普通函数很难做到，但 class 可以轻松实现！
"""

class SmartCalculator:
    """会记录历史的计算器"""
    
    def __init__(self):
        """初始化"""
        self.history = []     # 记录所有历史输入
        self.call_count = 0   # 调用次数
    
    def add_number(self, num):
        """添加一个数字"""
        self.history.append(num)  # 保存到历史
        self.call_count += 1      # 调用次数 +1
        print(f"第 {self.call_count} 次调用，添加了: {num}")
    
    def get_average(self):
        """计算平均值"""
        if not self.history:
            return 0
        avg = sum(self.history) / len(self.history)
        return avg
    
    def show_stats(self):
        """显示统计信息"""
        print(f"\n统计信息：")
        print(f"  调用次数: {self.call_count}")
        print(f"  历史数据: {self.history}")
        print(f"  平均值: {self.get_average():.2f}")

print("="*50)
print("第七部分：保存状态")
print("="*50)

calc = SmartCalculator()
calc.add_number(10)
calc.add_number(20)
calc.add_number(30)
calc.show_stats()
print()


# ==========================================
# 第八部分：常见错误和解决方法
# ==========================================

print("="*50)
print("第八部分：常见错误")
print("="*50)

"""
❌ 错误1：忘记写 self

class BadDog:
    def __init__(name):  # ❌ 缺少 self
        name = name

解决：第一个参数必须是 self
"""

"""
❌ 错误2：忘记用 self 访问属性

class BadDog:
    def __init__(self, name):
        name = name  # ❌ 这样不会保存到对象上
        
    def bark(self):
        print(name)  # ❌ 找不到 name

解决：用 self.name
"""

"""
❌ 错误3：方法外访问 self

def bad_function():
    print(self.name)  # ❌ self 只能在 class 的方法里用

解决：self 只能在 class 内部使用
"""

class CorrectDog:
    """正确的写法"""
    
    def __init__(self, name):
        self.name = name  # ✅ 用 self 保存
    
    def bark(self):
        print(f"{self.name} 汪汪汪！")  # ✅ 用 self 访问

correct = CorrectDog("旺财")
correct.bark()
print()


# ==========================================
# 第九部分：总结和记忆口诀
# ==========================================

print("="*50)
print("第九部分：总结")
print("="*50)

"""
🎯 记忆口诀：

1. class 是图纸，对象是实物
   - class Dog: 是狗的设计图
   - dog = Dog(): 是真实的狗

2. self 就是「我自己」
   - 方法的第一个参数必须是 self
   - self 代表「这个对象本身」

3. 要保存数据用 self.xxx
   - self.name = "小白"  ← 保存到对象上
   - name = "小白"       ← 只是局部变量

4. 调用自己的方法用 self.方法名()
   - self.bark()  ← 调用自己的方法

5. Python 自动传递 self
   - 你写: dog.bark()
   - Python: Dog.bark(dog)


📝 实用建议：

1. 看到 class，想到「设计图纸」
2. 看到 self，想到「我自己」
3. 需要保存数据 → 用 self.xxx
4. 不需要保存 → 用普通变量
5. LeetCode 刷题 → 复制模板，专注算法
"""


# ==========================================
# 第十部分：练习题
# ==========================================

print("\n" + "="*50)
print("第十部分：练习题")
print("="*50)

"""
🏋️ 练习1：创建一个学生类

要求：
1. 有名字、年龄、成绩属性
2. 有一个方法显示学生信息
3. 有一个方法判断是否及格（60分及格）
"""

class Student:
    """学生类"""
    
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    
    def show_info(self):
        """显示信息"""
        print(f"姓名: {self.name}, 年龄: {self.age}, 成绩: {self.score}")
    
    def is_pass(self):
        """是否及格"""
        if self.score >= 60:
            print(f"{self.name} 及格了！")
            return True
        else:
            print(f"{self.name} 不及格...")
            return False

# 测试
print("\n练习1：学生类")
s1 = Student("小明", 18, 85)
s2 = Student("小红", 17, 55)

s1.show_info()
s1.is_pass()

s2.show_info()
s2.is_pass()


"""
🏋️ 练习2：创建一个银行账户类

要求：
1. 初始余额为 0
2. 可以存钱（deposit）
3. 可以取钱（withdraw），余额不足时提示
4. 可以查看余额（check_balance）
"""

class BankAccount:
    """银行账户"""
    
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0  # 初始余额为 0
        print(f"账户创建成功！户主: {self.owner}")
    
    def deposit(self, amount):
        """存钱"""
        self.balance += amount
        print(f"存入 {amount} 元，当前余额: {self.balance} 元")
    
    def withdraw(self, amount):
        """取钱"""
        if amount > self.balance:
            print(f"余额不足！当前余额: {self.balance} 元")
            return False
        else:
            self.balance -= amount
            print(f"取出 {amount} 元，当前余额: {self.balance} 元")
            return True
    
    def check_balance(self):
        """查看余额"""
        print(f"当前余额: {self.balance} 元")
        return self.balance

# 测试
print("\n练习2：银行账户")
account = BankAccount("张三")
account.deposit(1000)
account.withdraw(300)
account.withdraw(800)  # 余额不足
account.check_balance()


print("\n" + "="*50)
print("🎉 恭喜！你已经掌握了 class 和 self 的核心概念！")
print("="*50)

"""
📚 下一步学习建议：

1. 多练习：自己创建几个 class
   - 创建一个汽车类（Car）
   - 创建一个图书类（Book）
   - 创建一个购物车类（ShoppingCart）

2. 理解原理：
   - class 是模板/图纸
   - self 是对象本身
   - 方法是对象能做的事

3. LeetCode 刷题：
   - 遇到 class Solution 不要慌
   - 复制模板，在方法里写算法
   - self 只是格式要求，专注算法本身

4. 遇到问题：
   - 检查是否忘记写 self
   - 检查是否用 self.xxx 保存数据
   - 看看是不是拼写错误

加油！💪
"""

