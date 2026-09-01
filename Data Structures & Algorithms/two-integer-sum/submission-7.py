class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i,n in enumerate(nums):
            dif = target - n
            if dif in dict:
                return [dict[dif],i]
            dict[n]=i
