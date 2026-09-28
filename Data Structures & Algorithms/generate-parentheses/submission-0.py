class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(curr: str, openpar: int, rem: int):
            nonlocal res
            if len(curr) == 2 * n:
                res.append(curr)
            else:
                if openpar > 0:
                    dfs(curr+")", openpar - 1, rem)
                if rem > 0:
                    dfs(curr+"(", openpar + 1, rem - 1)
        
        dfs("", 0, n)
        return res