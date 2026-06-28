def find_prefix(nums):
    prefix = [] + nums
    for i in range(1,len(nums)):
        prefix[i] = prefix[i] * prefix[i-1]
    return prefix

def find_postfix(nums):
    postfix = [] + nums
    for i in range(len(nums)-2, -1, -1):
        postfix[i] = postfix[i] * postfix[i+1]
    return postfix


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = find_prefix(nums)
        postfix = find_postfix(nums)

        ans = [] + nums
        for i in range(len(nums)):
            if i ==0:
                left = 1
            else:
                left = prefix[i-1]

            if i ==len(nums)-1:
                right = 1
            else:
                right = postfix[i+1]
            ans[i] = left * right
        return ans
        