class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        res = len(position)

        for i in range(len(position)):
            stack.append((position[i], (target-position[i])/speed[i]))

        stack = sorted(stack)

        for i in range(len(stack)-1):
            if stack and stack[-1][1] >= stack[-2][1]:
                res -= 1
                del stack[-2]
            else:
                stack.pop()
            

        return res