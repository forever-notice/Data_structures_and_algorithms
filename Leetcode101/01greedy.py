from __future__ import annotations

# 455.Assign Cookies
# 有一群孩子和一堆饼干，每个孩子有一个饥饿度，每个饼干都有一个饱腹度。每个孩子只能吃一个饼干，
# 且只有饼干的饱腹度不小于孩子的饥饿度时，这个孩子才能吃饱。求解最多有多少孩子可以吃饱。

# class Solution:
#     def fCC(self,children:list[int],cookies:list[int]) -> int:
#         children.sort()
#         cookies.sort()
#         child_i, cookies_i = 0,0 #计数器，看是否遍历完
#         n_children, n_cookies = len(children), len(cookies) #统计小孩和饼干的个数
#         while child_i < n_children and cookies_i < n_cookies:
#             if children[child_i] <= cookies[cookies_i]:
#                 child_i += 1
#             cookies_i += 1
#         return child_i

# sol = Solution()
# result = sol.fCC([1,2],[1,2,3])
# print("结果:", result, "预期:", 2)
# print("✅" if result == 2 else "❌")


# 135 Candy
# 一群孩子站成一排，每一个孩子有自己的评分。现在需要给这些孩子发糖果，规则是如果一个孩子的评分比自己身旁的一个孩子要高，
# 那么这个孩子就必须得到比身旁孩子更多的糖果。所有孩子至少要有一个糖果。求解最少需要多少个糖果




# class Solution:
#     def candy(self,ratings_list:list[int]) -> int:
#         n = len(ratings_list) # n 是小孩儿人数
#         candies = [1] * n # 糖果数，最后再相加
#         for i in range(1,n): #为什么从第二个孩子开始？
#             if ratings_list[i] > ratings_list[i-1]:
#                 candies[i] = candies[i-1] + 1
#         for i in range(n-1,0,-1):
#             if ratings_list[i] < ratings_list[i-1]:
#                 candies[i-1] = max(candies[i-1], candies[i]+1) #max的左边保证左边规则，右边保证右边规则
#         return sum(candies)


# sol = Solution()
# result = sol.candy([1,2,2])
# print("结果:", result, "预期:", 4)
# print("✅" if result == 4 else "❌")

# 435
# 给定多个区间，计算让这些区间互不重叠所需要移除区间的最少个数。起止相连不算重叠

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1]) 
        removed, prev_end = 0, intervals[0][1] 
        for i in range(1, len(intervals)): 
            if prev_end > intervals[i][0]: removed += 1 
            else: prev_end = intervals[i][1] 
        return removed
        

# sol = Solution()
# result = sol.candy([1,2,2])
# print("结果:", result, "预期:", 4)
# print("✅" if result == 4 else "❌")