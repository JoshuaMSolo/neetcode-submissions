class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        charset = [[], [], ["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]
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