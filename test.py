# Leetcode 048 - 旋转图像
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """原地旋转矩阵 90 度"""
        n = len(matrix)
        # 第一步：上下翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]
        # 第二步：对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# ==========================================
# 💡 最简单的测试方法（推荐！）
# ==========================================

"""
只需要 3 步：
1. 创建 Solution 对象
2. 准备测试数据和预期结果
3. 调用函数并对比结果
"""

# 创建对象（只需要一次）
sol = Solution()

# 测试 1：3x3 矩阵
matrix1 = [[1,2,3], [4,5,6], [7,8,9]]
sol.rotate(matrix1)
print("测试1:", matrix1)
print("预期:", [[7,4,1], [8,5,2], [9,6,3]])
print("通过" if matrix1 == [[7,4,1], [8,5,2], [9,6,3]] else "失败")

# 测试 2：2x2 矩阵
matrix2 = [[1,2], [3,4]]
sol.rotate(matrix2)
print("\n测试2:", matrix2)
print("预期:", [[3,1], [4,2]])
print("通过" if matrix2 == [[3,1], [4,2]] else "失败")
