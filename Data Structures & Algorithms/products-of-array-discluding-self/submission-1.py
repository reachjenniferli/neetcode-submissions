class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        total = 1

        for i in nums: 
            total *= i

        output = []

        for i, n in enumerate(nums): 

            if n == 0:
                zerototal = 1
                for x in range(len(nums)):
                    if x == i:
                        continue
                    zerototal *= nums[x]
                output.append(int(zerototal))

            else:
                output.append(int(total/n))

        return output
        