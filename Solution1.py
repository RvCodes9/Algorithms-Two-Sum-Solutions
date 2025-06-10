# "Two Sum" Easy LeetCode Algorithms | Solution 1

class Solution:

    def two_sum(self, nums:list[int], target:int) -> list[int]:
        
        for value in nums:

            if target < value:
                continue

            for len_value in nums:

                if (value + len_value) == target:
                    return [value,len_value]
        
algorithms : Solution = Solution()
print(algorithms.two_sum([11,15,2,7],9))