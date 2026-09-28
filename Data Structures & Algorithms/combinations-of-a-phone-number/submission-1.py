class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        charset = ["", "", "abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        res = []
        if not digits:
            return res

        def dfs(curr:str, rem:str):
            nonlocal res
            if not rem:
                res.append(curr)
            else: 
                for char in charset[int(rem[0])]:
                    dfs(curr+char, rem[1:])
        
        dfs("", digits)
        return res