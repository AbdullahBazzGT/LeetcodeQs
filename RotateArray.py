class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        """
        n = LENGTH OF ARRAY

        nums[:-k]                   returns [0: n - k)
        nums[-k:]                   returns [n - k: n - 1]
        nums[:k] == nums[0: k]      returns [0,k)
        nums[k:] == nums[k: n - 1]  returns [k, n - 1]
        """

        n = len(nums)
        k = k % n

        # Step 1: Reverse the entire array. [1,2,3,4,5,6,7] = [7,6,5,4,3,2,1]
        nums.reverse()
        
        # Step 2: Reverse the first k elements. [7,6,5| 4,3,2,1] = [5,6,7| 4,3,2,1]
        nums[:k] = reversed(nums[:k])
        
        # Step 3: Reverse the remaining n-k elements. [7,6,5,4,3,2,1] = [7,6,5,1,2,3,4]
        nums[k:] = reversed(nums[k:])

        """
        In the event you need to write your own reverse function. The above code is much more readable imo so I will exlcude this.

        def reverseInPlace(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]  # Swap elements
                start += 1
                end -= 1
        """

