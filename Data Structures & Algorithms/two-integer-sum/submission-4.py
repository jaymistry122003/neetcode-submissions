class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i,num in enumerate(nums):
            for j,num in enumerate(nums):
                if nums[i] + nums[j] == target and i!=j:
                    output.append(i)
                    output.append(j)
                    return output     
        return False
                
        