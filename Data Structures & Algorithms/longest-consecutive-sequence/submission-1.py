class Solution:
    from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. Convert the list to a set. 
        # This takes O(N) time, but now lookups (checking 'if x in set') are instant O(1).
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            # 2. Check if this number is the START of a sequence.
            # We do this by checking if the number exactly 1 less than it exists.
            if (num - 1) not in num_set:
                # We found a starting number! Let's start counting.
                current_num = num
                current_streak = 1
                
                # 3. Keep checking if the next consecutive number exists in the set
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
                    
                # 4. Compare the streak we just found to our all-time longest streak
                if current_streak > longest_streak:
                    longest_streak = current_streak
                    
        return longest_streak



        
            

        