class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outlist=[]
        n=len(nums)
        for i in range(n):
            left_side = nums[:i]
            right_side = nums[i+1:]

            prod = 1
            for num in left_side:
                prod *= num
            for num in right_side:
                prod *= num
            outlist.append(prod)
        return outlist
            
        


        