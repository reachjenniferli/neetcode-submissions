class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0 
        r = len(nums)-1

        #find the pivot
        while l < r: 
            m = l+(r-l)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l
        #bsearch as usual

        l = 0
        r = len(nums)-1

        while l <= r: 
            m = l+(r-l)//2
            real_mid = (m+pivot)%len(nums)
            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] < target:
                l = m + 1
            else:
                r = m - 1 

        return -1



