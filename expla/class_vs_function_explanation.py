"""
为什么有时候用 class，有时候用 function？
让我们对比三种写法！
"""

# ==========================================
# 写法1：LeetCode 标准格式（用 class）
# ==========================================
from typing import List

class Solution:
    """
    这是 LeetCode 的标准格式
    为什么要用 class？因为 LeetCode 平台规定必须这样写！
    """
    def pivotIndex(self, nums: List[int]) -> int:
        """寻找数组的中心索引"""
        total_sum = sum(nums)  # 计算总和
        curr_sum = 0
        
        for i in range(len(nums)):
            # 如果左边和 == 右边和，那么 i 就是中心索引
            if curr_sum * 2 + nums[i] == total_sum:
                return i
            curr_sum += nums[i]
        
        return -1  # 没找到返回 -1

# LeetCode 平台会这样调用你的代码：
solution = Solution()  # 创建一个 Solution 对象
result = solution.pivotIndex([1, 7, 3, 6, 5, 6])
print(f"LeetCode 格式结果: {result}")  # 输出: 3


# ==========================================
# 写法2：普通函数（自己练习时可以这样写）
# ==========================================

def find_pivot_index(nums):
    """
    这是普通函数写法
    自己练习算法时，这样写更简单！
    """
    total_sum = sum(nums)
    curr_sum = 0
    
    for i in range(len(nums)):
        if curr_sum * 2 + nums[i] == total_sum:
            return i
        curr_sum += nums[i]
    
    return -1

# 普通函数直接调用，更简单
result = find_pivot_index([1, 7, 3, 6, 5, 6])
print(f"普通函数结果: {result}")  # 输出: 3


# ==========================================
# 写法3：直接写脚本（最简单的练习方式）
# ==========================================

# 直接写代码，不用函数也不用类
nums = [1, 7, 3, 6, 5, 6]
total_sum = sum(nums)
curr_sum = 0
pivot = -1

for i in range(len(nums)):
    if curr_sum * 2 + nums[i] == total_sum:
        pivot = i
        break
    curr_sum += nums[i]

print(f"直接脚本结果: {pivot}")  # 输出: 3


# ==========================================
# 总结：什么时候用哪种写法？
# ==========================================

"""
✅ 用 class（写法1）的情况：
   - 在 LeetCode、牛客网等刷题平台（平台要求）
   - 需要保存状态的复杂算法
   - 写大型项目时

✅ 用普通函数（写法2）的情况：
   - 自己练习算法时（最推荐！）
   - 写工具函数
   - 代码需要重复调用

✅ 直接写脚本（写法3）的情况：
   - 快速测试一个想法
   - 一次性任务
   - 学习基础语法时

对于学习算法的你，建议：
1. LeetCode 刷题 → 必须用 class（复制题目模板）
2. 自己练习 → 用普通函数（更简单）
3. 快速测试 → 直接写（最快）
"""


# ==========================================
# 实战示例：看看你的 test.py 可以怎么改
# ==========================================

print("\n" + "="*50)
print("实战对比：三种写法的效果完全一样！")
print("="*50)

# 测试数据
test_nums = [1, 7, 3, 6, 5, 6]

# 方法1：LeetCode 格式
sol = Solution()
result1 = sol.pivotIndex(test_nums)

# 方法2：普通函数
result2 = find_pivot_index(test_nums)

# 方法3：直接写
result3 = pivot

print(f"LeetCode 格式: {result1}")
print(f"普通函数:     {result2}")
print(f"直接脚本:     {result3}")
print(f"\n三个结果一样吗？{result1 == result2 == result3}")  # True


# ==========================================
# 为什么 LeetCode 要用 class？
# ==========================================

"""
技术原因：

1. 统一格式：
   所有人的代码格式一样，方便自动测试

2. 面向对象：
   - self 参数可以让你保存中间结果
   - 可以有多个相关的方法
   
3. 企业面试：
   很多公司面试也用这种格式，提前适应

4. 自动测试：
   LeetCode 的测试系统是这样写的：
   
   solution = Solution()  # 创建对象
   result = solution.方法名(测试数据)  # 调用你的方法
   if result == 期望结果:
       print("通过！")
"""


# ==========================================
# class 有什么好处？
# ==========================================

class AdvancedSolution:
    """
    用 class 的好处：可以保存状态！
    """
    def __init__(self):
        """初始化时可以设置一些变量"""
        self.count = 0  # 记录调用次数
        self.history = []  # 记录历史结果
    
    def pivotIndex(self, nums: List[int]) -> int:
        """每次调用都会记录"""
        self.count += 1  # 调用次数 +1
        
        result = -1
        total_sum = sum(nums)
        curr_sum = 0
        
        for i in range(len(nums)):
            if curr_sum * 2 + nums[i] == total_sum:
                result = i
                break
            curr_sum += nums[i]
        
        self.history.append(result)  # 记录结果
        return result
    
    def get_stats(self):
        """查看统计信息"""
        return {
            "调用次数": self.count,
            "历史结果": self.history
        }

# 测试 class 的好处
print("\n" + "="*50)
print("class 的好处：可以保存状态")
print("="*50)

adv_sol = AdvancedSolution()
adv_sol.pivotIndex([1, 7, 3, 6, 5, 6])
adv_sol.pivotIndex([1, 2, 3])
adv_sol.pivotIndex([2, 1, -1])

stats = adv_sol.get_stats()
print(f"调用了 {stats['调用次数']} 次")
print(f"历史结果: {stats['历史结果']}")


# ==========================================
# 给你的建议
# ==========================================

"""
🎯 学习算法时的建议：

1. 刷 LeetCode？
   ✅ 复制题目的 class 模板，在里面写代码
   ✅ 不要自己改成函数（会报错）

2. 自己练习？
   ✅ 用普通函数就行，简单明了
   
3. 快速测试想法？
   ✅ 直接写脚本，最快

4. array_practice.py 那种？
   ✅ 用普通函数，因为是你自己练习用的

5. test.py 这种？
   ✅ 用 class，因为是从 LeetCode 复制的题目


📝 记住：
- class 不是必需的
- 只是 LeetCode 平台的格式要求
- 自己练习时，怎么简单怎么来！
- 理解算法思想最重要，格式不重要
"""

