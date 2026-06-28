class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
    
        for i in range(0,len(nums)):
            if nums[i] in dict1:
                dict1[nums[i]] += 1
            else:
                dict1[nums[i]] = 1

        sorted_dict1 = sorted(dict1.items(), key=lambda x:x[1], reverse = True)
        ans = []
        for i in range(k):
            ans.append(sorted_dict1[i][0])
        return ans