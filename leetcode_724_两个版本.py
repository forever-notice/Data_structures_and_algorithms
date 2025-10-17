"""
LeetCode 724: 寻找数组的中心索引
展示两种写法的区别
"""

from __future__ import annotations
from typing import List

print("="*60)
print("LeetCode 724: 寻找数组的中心索引")
print("="*60)

# ============================================
# 版本1：LeetCode 提交格式（必须这样写）
# ============================================
print("\n【版本1：LeetCode 格式】")
print("这是提交到 LeetCode 时必须用的格式\n")

class Solution:
    """
    LeetCode 要求的格式：
    1. 必须有 class Solution
    2. 方法必须有 self 参数
    3. 不能改变类名和方法名
    """
    def pivotIndex(self, nums: List[int]) -> int:
        """
        寻找中心索引：
        中心索引左侧所有元素和 = 右侧所有元素和
        """
        total_sum = sum(nums)  # 总和
        curr_sum = 0  # 当前左侧和
        
        for i in range(len(nums)):
            # 左侧和 = curr_sum
            # 右侧和 = total_sum - curr_sum - nums[i]
            # 如果左侧和 == 右侧和，即：
            # curr_sum == total_sum - curr_sum - nums[i]
            # 化简为：curr_sum * 2 + nums[i] == total_sum
            if curr_sum * 2 + nums[i] == total_sum:
                return i
            curr_sum += nums[i]
        
        return -1  # 没找到返回 -1

# LeetCode 会这样测试你的代码：
solution = Solution()  # 创建 Solution 对象
test1 = solution.pivotIndex([1, 7, 3, 6, 5, 6])
test2 = solution.pivotIndex([1, 2, 3])
test3 = solution.pivotIndex([2, 1, -1])

print(f"测试1: [1, 7, 3, 6, 5, 6] → 中心索引是 {test1}")
print(f"测试2: [1, 2, 3]           → 中心索引是 {test2}")
print(f"测试3: [2, 1, -1]          → 中心索引是 {test3}")


# ============================================
# 版本2：自己练习格式（简单明了）
# ============================================
print("\n" + "="*60)
print("【版本2：普通函数格式】")
print("自己练习时可以这样写，更简单！\n")

def find_pivot_index(nums: list[int]) -> int:
    """
    普通函数版本：
    1. 不需要 class
    2. 不需要 self
    3. 直接调用，简单明了
    
    算法思想完全一样！
    """
    total_sum = sum(nums)
    curr_sum = 0
    
    for i in range(len(nums)):
        if curr_sum * 2 + nums[i] == total_sum:
            return i
        curr_sum += nums[i]
    
    return -1

# 直接调用，不需要创建对象
test1 = find_pivot_index([1, 7, 3, 6, 5, 6])
test2 = find_pivot_index([1, 2, 3])
test3 = find_pivot_index([2, 1, -1])

print(f"测试1: [1, 7, 3, 6, 5, 6] → 中心索引是 {test1}")
print(f"测试2: [1, 2, 3]           → 中心索引是 {test2}")
print(f"测试3: [2, 1, -1]          → 中心索引是 {test3}")


# ============================================
# 对比总结
# ============================================
print("\n" + "="*60)
print("【对比总结】")
print("="*60)

print("""
┌─────────────────┬──────────────────┬──────────────────┐
│     特点        │  LeetCode 格式   │   普通函数格式   │
├─────────────────┼──────────────────┼──────────────────┤
│ 需要 class？    │  ✅ 必须有       │  ❌ 不需要       │
│ 需要 self？     │  ✅ 必须有       │  ❌ 不需要       │
│ 调用方式        │  先创建对象      │  直接调用函数    │
│ 使用场景        │  LeetCode 提交   │  自己练习        │
│ 代码复杂度      │  稍复杂          │  简单            │
│ 算法思想        │  完全一样！      │  完全一样！      │
└─────────────────┴──────────────────┴──────────────────┘

🎯 核心要点：
1. 算法思想完全相同，只是格式不同
2. LeetCode 刷题 → 必须用 class（平台要求）
3. 自己练习 → 用普通函数（更简单）
4. 不要纠结格式，理解算法才是关键！

📝 你的文件应该这样：
- test.py          → LeetCode 格式（因为是从题目复制的）
- array_practice.py → 普通函数（因为是自己练习）

✅ 你现在的写法是正确的！
""")


# ============================================
# 算法原理讲解
# ============================================
print("\n" + "="*60)
print("【算法原理】寻找中心索引")
print("="*60)

print("""
题目：找到数组的中心索引，使得左侧元素和 = 右侧元素和

例子: [1, 7, 3, 6, 5, 6]
       ↓  ↓  ↓  ↓  ↓  ↓
索引:  0  1  2  3  4  5

索引3 是中心：
左侧: 1 + 7 + 3 = 11
右侧: 5 + 6 = 11  ✅ 相等！

算法思路：
1. 先算出总和 total_sum = 28
2. 遍历数组，维护当前左侧和 curr_sum
3. 对于索引 i：
   - 左侧和 = curr_sum
   - 右侧和 = total_sum - curr_sum - nums[i]
   - 如果相等，返回 i

数学推导：
   左侧和 == 右侧和
   curr_sum == total_sum - curr_sum - nums[i]
   curr_sum * 2 == total_sum - nums[i]
   curr_sum * 2 + nums[i] == total_sum  ← 这就是代码中的判断条件！

时间复杂度: O(n) - 只遍历一次数组
空间复杂度: O(1) - 只用了几个变量
""")

