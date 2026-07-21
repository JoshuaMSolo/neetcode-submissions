class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque([(sr,sc)])
        visited = set([(sr,sc)])
        init_color = image[sr][sc]
        while len(queue) > 0 :
            node = queue.popleft()
            row = node[0]
            col = node[1]
            image[row][col] = color
            for neighbor in [(row+1, col), (row-1,col), (row, col-1), (row, col+1)]:
                if neighbor in visited :
                    continue
                a = neighbor[0]
                b = neighbor[1]
                if a < len(image) and a >= 0 and b < len(image[0]) and b >= 0 and image[a][b] == init_color : 
                    queue.append(neighbor)
                    visited.add(neighbor)
        return image


