class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []*2
        

        for i in range(len(tokens)):
            if tokens[i] == ('+'):
                nums[-2] = int(nums[-2]) + int(nums[-1])
                nums.pop()
                print("+")
                print(nums)
            elif tokens[i] == ('-'):
                nums[-2] = int(nums[-2]) - int(nums[-1])
                nums.pop()
                print("-")
                print(nums)
            elif tokens[i] == ('*'):
                nums[-2] = int(nums[-2]) * int(nums[-1])
                nums.pop()
                print("*")
                print(nums)
            elif tokens[i] == ('/'):
                nums[-2] = int(nums[-2]) / int(nums[-1])
                nums.pop()
                print("/")
                print(nums)
            else:
                nums.append(int(tokens[i]))
                print("append")
                print(nums)
        return int(nums[0])