from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False

# How to call it properly:
solution = Solution()
print(solution.hasDuplicate([1, 1, 2, 3, 4]))  # Output: True