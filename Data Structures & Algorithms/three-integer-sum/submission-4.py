class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n= len(nums)
        ans = []
        nums.sort()
        for i in range(n-2):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            c = nums[i]
            target = -c
            left = i + 1
            right = n - 1
            while left < right:
                curr = nums[left] + nums[right]
                if curr == target:
                    ans.append([nums[left],nums[right],nums[i]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left +=1
                    right -=1
                elif curr > target:
                    right -= 1
                else:
                    left += 1
                
        return ans 