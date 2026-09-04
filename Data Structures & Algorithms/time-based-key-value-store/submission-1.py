class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        
        r = len(self.dic[key]) - 1
        l = 0
        res = ""
        arr = self.dic[key]
        while l <= r:
            m = (l+r)//2
            if arr[m][0] <= timestamp:
                l = m+1
                res = arr[m][1]
            else :
                r = m-1
        return res
