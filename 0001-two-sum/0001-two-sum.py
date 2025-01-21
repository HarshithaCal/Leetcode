class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in dic:
                return [dic[remaining], i]
            else:
                dic[nums[i]] = i
        print(dic)


                


        