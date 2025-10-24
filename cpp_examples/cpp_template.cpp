/*
 * C++ 数据结构与算法模板
 * 文件名：cpp_template.cpp
 * 编译运行：clang++ -std=c++17 cpp_template.cpp -o cpp_template && ./cpp_template
 */

#include <iostream>
#include <vector>
#include <string>
using namespace std;

// ============================================
// LeetCode 风格的解题模板
// ============================================
class Solution {
public:
    // 示例：找到数组的中心索引（LeetCode 724）
    int pivotIndex(vector<int>& nums) {
        int total = 0;
        // 计算总和
        for (int num : nums) {
            total += num;
        }
        
        int leftSum = 0;
        // 遍历数组找中心索引
        for (int i = 0; i < nums.size(); i++) {
            // 如果左边和等于右边和
            if (leftSum == total - leftSum - nums[i]) {
                return i;
            }
            leftSum += nums[i];
        }
        return -1;
    }
};

// ============================================
// 测试函数
// ============================================
void testPivotIndex() {
    Solution sol;
    
    // 测试用例1
    vector<int> nums1 = {1, 7, 3, 6, 5, 6};
    cout << "测试1：[1, 7, 3, 6, 5, 6]" << endl;
    cout << "中心索引：" << sol.pivotIndex(nums1) << endl;
    cout << "（预期：3）" << endl << endl;
    
    // 测试用例2
    vector<int> nums2 = {1, 2, 3};
    cout << "测试2：[1, 2, 3]" << endl;
    cout << "中心索引：" << sol.pivotIndex(nums2) << endl;
    cout << "（预期：-1）" << endl << endl;
    
    // 测试用例3
    vector<int> nums3 = {2, 1, -1};
    cout << "测试3：[2, 1, -1]" << endl;
    cout << "中心索引：" << sol.pivotIndex(nums3) << endl;
    cout << "（预期：0）" << endl << endl;
}

// ============================================
// 主函数
// ============================================
int main() {
    cout << "================================" << endl;
    cout << "   C++ 数据结构与算法示例" << endl;
    cout << "================================" << endl << endl;
    
    testPivotIndex();
    
    cout << "================================" << endl;
    cout << "   程序运行完毕！" << endl;
    cout << "================================" << endl;
    
    return 0;
}

/* 
 * 运行结果示例：
 * ================================
 *    C++ 数据结构与算法示例
 * ================================
 * 
 * 测试1：[1, 7, 3, 6, 5, 6]
 * 中心索引：3
 * （预期：3）
 * 
 * 测试2：[1, 2, 3]
 * 中心索引：-1
 * （预期：-1）
 * 
 * 测试3：[2, 1, -1]
 * 中心索引：0
 * （预期：0）
 * 
 * ================================
 *    程序运行完毕！
 * ================================
 */

