class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums) #We can access elements in O(1)
        greatest = 0

        for num in nums:
            curr_length = 0
            if num - 1 not in nums_set: #THIS WILL LOOK AT EVERYTHING, VERY REDUNDANT
                curr_length = 1
                while num + curr_length in nums_set:
                    nums_set.remove(num + curr_length) # After seeing a value remove it from the set to avoid redundent checks.
                    curr_length += 1

            if curr_length > greatest:
                greatest = curr_length

        return greatest

            


        