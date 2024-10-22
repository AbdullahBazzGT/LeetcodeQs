"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #Initalize Variables, Dictionary with one entry of prefix 0.
        currPrefix = 0
        totalSubarrays = 0
        prefix = {0:1}

        for i in range(len(nums)):
            currPrefix += nums[i]
            diff = currPrefix - k #If this equals Zero, we already place a zero in the map guareenting an increment.
            
            if diff in prefix:
                totalSubarrays += prefix.get(diff)

            prefix[currPrefix] = prefix.get(currPrefix, 0) + 1 

        return totalSubarrays

        
        
        
                