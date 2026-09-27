class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        i = int(r / 2)
        count = 0

        for count in range(int(len(nums)/2)+1):
            print("__")
            print(nums[i])
            print(nums[r])
            print(nums[l])
            if nums[r] == target:
                return r
            elif nums[l] == target:
                return l
            if nums[i] > target:
                r = i
                i = int((r-l) / 2) + l
                #count += 1
            elif nums[i] < target:
                l = i
                i = int((r-l) / 2) + l
                #count += 1        
            else:
                return i
        
        return -1