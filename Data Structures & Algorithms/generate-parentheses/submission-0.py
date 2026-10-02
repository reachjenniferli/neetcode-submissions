class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(cur, open, close):

            if len(cur) == 2*n:
                res.append(cur)
                return

            #decision to open:
            if open < n:
                dfs(cur+'(', open+1, close)
            
            #decision to close
            if close < open:
                dfs(cur+')', open, close+1)

        dfs("(", 1, 0)
        return res
