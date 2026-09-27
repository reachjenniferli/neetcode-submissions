class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        print(nums)
        setnums = set()
        ls = []

        for i in range(len(nums)-2):
            if nums[i] < 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = len(nums) - 1
            a = nums[i]
            target = 0 - a

            while L < R:
                b = nums[L]
                c = nums[R]
                if target == (b + c):
                    if (tuple([a, nums[L], nums[R]]) not in setnums):
                        setnums.add(tuple([a, nums[L], nums[R]]))
                        ls.append([a, nums[L], nums[R]])
                    L += 1
                    R -= 1
                elif (b + c) < target:
                    L += 1
                elif (b + c) > target:
                    R -= 1
                print("abc")
                print([a, b, c])

        return ls