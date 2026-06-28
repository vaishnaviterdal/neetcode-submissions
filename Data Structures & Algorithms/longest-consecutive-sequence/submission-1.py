class Solution:
    def longestConsecutive(self, nums1 : List[int])-> int:
    
        if not nums1:
            return 0
        nums = sorted(list(set(nums1)))
        max_count = 0
        count = 1
        n = len(nums)-1
        i = 0
        while i < n:
            if nums [i] + 1 == nums[i+1]:
                count += 1  
            
            else:
                if count > max_count:
                    max_count = count
                count = 1
            i +=1
        if count > max_count:
            max_count = count
        return max_count



    
    

        

    