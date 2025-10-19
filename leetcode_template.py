"""
LeetCode 快速测试模板
===================
复制这个模板，改一下就能测试任何 LeetCode 题目
"""

from typing import List

# ==========================================
# 1. 把 LeetCode 的 class 复制到这里
# ==========================================

class Solution:
    def yourFunction(self, nums: List[int]) -> int:
        """把 LeetCode 的方法复制到这里"""
        # 你的算法代码
        pass


# ==========================================
# 2. 写测试（只需要 3 行！）
# ==========================================

# 创建对象
sol = Solution()

# 测试 1
result1 = sol.yourFunction([1, 2, 3])  # 调用函数
print("测试1:", result1, "预期:", 6)
print("✅" if result1 == 6 else "❌")

# 测试 2
result2 = sol.yourFunction([])
print("\n测试2:", result2, "预期:", 0)
print("✅" if result2 == 0 else "❌")


# ==========================================
# 💡 不同类型题目的测试示例
# ==========================================

"""
【示例 1】返回数字的题目（如：两数之和）
"""
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # 你的代码
#         pass

# sol = Solution()
# result = sol.twoSum([2, 7, 11, 15], 9)
# print("结果:", result, "预期:", [0, 1])
# print("✅" if result == [0, 1] else "❌")


"""
【示例 2】原地修改的题目（如：旋转矩阵）
"""
# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         # 你的代码
#         pass

# sol = Solution()
# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# sol.rotate(matrix)  # 注意：原地修改，没有返回值
# print("结果:", matrix)
# print("预期:", [[7,4,1], [8,5,2], [9,6,3]])
# print("✅" if matrix == [[7,4,1], [8,5,2], [9,6,3]] else "❌")


"""
【示例 3】返回布尔值的题目（如：验证回文串）
"""
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # 你的代码
#         pass

# sol = Solution()
# result = sol.isPalindrome("A man a plan a canal Panama")
# print("结果:", result, "预期:", True)
# print("✅" if result == True else "❌")


"""
【示例 4】返回字符串的题目（如：最长公共前缀）
"""
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         # 你的代码
#         pass

# sol = Solution()
# result = sol.longestCommonPrefix(["flower","flow","flight"])
# print("结果:", result, "预期:", "fl")
# print("✅" if result == "fl" else "❌")


# ==========================================
# 📝 使用说明
# ==========================================

"""
使用步骤：

1. 从 LeetCode 复制题目的 class Solution 代码
2. 粘贴到上面的「1. 把 LeetCode 的 class 复制到这里」
3. 创建对象：sol = Solution()
4. 测试：
   - 有返回值：result = sol.函数名(参数)
   - 原地修改：sol.函数名(参数)，然后直接检查参数
5. 对比结果：print("✅" if result == 期望值 else "❌")

就这么简单！
"""

