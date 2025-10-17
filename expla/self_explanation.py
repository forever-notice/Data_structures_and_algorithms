from __future__ import annotations

"""
self 的使用说明
"""

print("=" * 70)
print("1. 普通函数 - 不需要 self")
print("=" * 70)

def add(a: int, b: int) -> int:
    """普通函数：直接定义在模块中，不属于任何类"""
    return a + b

result = add(3, 5)
print(f"add(3, 5) = {result}")
print()

print("=" * 70)
print("2. 类方法 - 必须用 self")
print("=" * 70)

class Calculator:
    """计算器类 - 用类来组织相关的数据和方法"""
    
    def __init__(self, name: str):
        """构造函数：创建对象时自动调用
        self 代表这个对象本身
        """
        self.name = name      # self.name 是对象的属性
        self.result = 0       # self.result 也是对象的属性
        print(f"创建了计算器：{self.name}")
    
    def add(self, a: int, b: int) -> int:
        """类方法：第一个参数必须是 self
        self 让方法可以访问对象的属性
        """
        self.result = a + b   # 保存结果到对象的属性中
        return self.result
    
    def get_last_result(self) -> int:
        """获取上次计算的结果"""
        return self.result

# 创建两个计算器对象
calc1 = Calculator("计算器A")
calc2 = Calculator("计算器B")
print()

# 使用对象调用方法（Python 自动传入 self）
result1 = calc1.add(10, 20)
result2 = calc2.add(100, 200)

print(f"{calc1.name} 的结果: {result1}")
print(f"{calc2.name} 的结果: {result2}")
print(f"{calc1.name} 上次结果: {calc1.get_last_result()}")
print(f"{calc2.name} 上次结果: {calc2.get_last_result()}")
print()

print("=" * 70)
print("3. 静态方法 - 不需要 self（装饰器 @staticmethod）")
print("=" * 70)

class MathUtils:
    """数学工具类"""
    
    @staticmethod
    def multiply(a: int, b: int) -> int:
        """静态方法：不需要访问对象属性，所以不需要 self"""
        return a * b

# 静态方法可以直接通过类名调用
result = MathUtils.multiply(5, 6)
print(f"MathUtils.multiply(5, 6) = {result}")
print()

print("=" * 70)
print("4. 实际例子：数组类")
print("=" * 70)

class MyArray:
    """自定义数组类"""
    
    def __init__(self, data: list[int]):
        """初始化：需要 self 来保存数组数据"""
        self.data = data  # self.data 是这个对象的数据
    
    def find_element(self, val: int) -> int:
        """查找元素：需要 self 来访问 self.data"""
        for i in range(len(self.data)):
            if self.data[i] == val:
                return i
        return -1
    
    def insert(self, index: int, val: int) -> bool:
        """插入元素：需要 self 来修改 self.data"""
        if 0 <= index <= len(self.data):
            self.data.insert(index, val)
            return True
        return False
    
    def show(self):
        """显示数组：需要 self 来访问 self.data"""
        print(f"数组内容: {self.data}")

# 使用数组类
arr = MyArray([1, 2, 3, 4, 5])
arr.show()

pos = arr.find_element(3)
print(f"找到元素 3 在位置: {pos}")

arr.insert(2, 99)
arr.show()
print()

print("=" * 70)
print("总结：什么时候用 self？")
print("=" * 70)
print("""
✅ 需要 self 的情况：
   1. 定义在类里面的方法（类方法）
   2. 需要访问对象的属性（self.xxx）
   3. 需要调用对象的其他方法
   
❌ 不需要 self 的情况：
   1. 普通函数（不在类里面）
   2. 静态方法（@staticmethod）
   3. 类方法用 cls（@classmethod）
   
📌 记忆技巧：
   - self = "我自己"
   - 如果方法需要知道"我是谁"、"我的数据是什么"，就需要 self
   - 如果方法只是做个计算，不关心对象，就不需要 self
""")
print("=" * 70)

