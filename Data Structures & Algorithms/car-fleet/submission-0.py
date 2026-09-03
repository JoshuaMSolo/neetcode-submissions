class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        traffic = sorted(zip(position, speed), key = lambda x: x[0], reverse = True)
        res = 0
        bound = 0
        for car in traffic :
            t = (target - car[0])/car[1]
            if t > bound:
                bound = t
                res += 1
        
        return res
