class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Finds the list of grid coordinates (r, c) where water can flow
        from that cell to both the Pacific and Atlantic oceans.
        """
        m = len(heights)
        if m == 0:
            return []
        n = len(heights[0])
        
        # Initialize visited arrays for Pacific and Atlantic
        # pacific[r][c] is True if water can flow from (r, c) to the Pacific
        pacific = [[False] * n for _ in range(m)]
        # atlantic[r][c] is True if water can flow from (r, c) to the Atlantic
        atlantic = [[False] * n for _ in range(m)]
        
        # Directions for movement: up, down, left, right
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, visited):
            """
            Performs Depth First Search (DFS) starting from (r, c) and marks 
            all reachable cells (flowing *into* (r, c)) as True in the visited array.
            
            Note: The problem asks where water can flow *from* a cell *to* an ocean.
            By starting the DFS from the ocean borders and moving to *higher or equal*
            cells, we are effectively reversing the flow: a cell (nr, nc) 
            can flow *to* (r, c) if heights[nr][nc] >= heights[r][c].
            If a cell (r, c) is marked visited, it means water can reach it *from*
            the starting border (ocean).
            """
            visited[r][c] = True
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                
                if (
                    0 <= nr < m and 0 <= nc < n and
                    not visited[nr][nc] and 
                    heights[nr][nc] >= heights[r][c] # Water flows from higher/equal to lower
                ):
                    dfs(nr, nc, visited)

        # 1. Start DFS from cells adjacent to the Pacific Ocean
        # Top row (r=0)
        for j in range(n):
            dfs(0, j, pacific)
        # Left column (c=0), skipping (0, 0) which is covered above
        for i in range(1, m):
            dfs(i, 0, pacific)

        # 2. Start DFS from cells adjacent to the Atlantic Ocean
        # Bottom row (r=m-1)
        for j in range(n):
            dfs(m - 1, j, atlantic)
        # Right column (c=n-1), skipping (m-1, n-1) which is covered above
        for i in range(m - 1):
            dfs(i, n - 1, atlantic)


        # The original implementation's loops:
        # for i in range(m):
        #   dfs(i, 0, pacific)
        #   dfs(i, n - 1, atlantic)
        # for j in range(n):
        #   dfs(0, j, pacific)
        #   dfs(m - 1, j, atlantic)
        # This covers all border cells including corners multiple times, which is fine.
        
        # Let's use the provided structure for exact match:
        # 1. Pacific Borders (Top Row and Left Column)
        for i in range(m):
            dfs(i, 0, pacific) # Left Column
        for j in range(n):
            dfs(0, j, pacific) # Top Row

        # 2. Atlantic Borders (Bottom Row and Right Column)
        for i in range(m):
            dfs(i, n - 1, atlantic) # Right Column
        for j in range(n):
            dfs(m - 1, j, atlantic) # Bottom Row
            
        # 3. Collect the result
        res = []
        for i in range(m):
            for j in range(n):
                # If water can flow from the cell (i, j) to both Pacific and Atlantic
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
                    
        return res