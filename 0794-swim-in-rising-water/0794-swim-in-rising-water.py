class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        import heapq
        n = len(grid)
        if n == 0:
            return 0

        # Min-Heap stores tuples: (max_elevation_time, row, col)
        # The max_elevation_time is the priority key 't'
        # Start at (0, 0). The time required to enter (0, 0) is grid[0][0].
        min_heap = [(grid[0][0], 0, 0)]
        
        # Visited set (or array) to track the minimum time found to reach a cell
        # A simple visited array is sufficient because Dijkstra's ensures the 
        # first time we extract a cell from the heap, it's the minimum max_elevation path.
        visited = set([(0, 0)]) 
        
        # Directions: (dr, dc) for [up, right, down, left]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while min_heap:
            # 1. Extract the cell with the smallest 'max_elevation_time' (t)
            # Python's heapq works on the first element of the tuple.
            t, r, c = heapq.heappop(min_heap)

            # 2. Check for destination
            if r == n - 1 and c == n - 1:
                return t

            # 3. Explore neighbors
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                # Check boundaries
                if 0 <= nr < n and 0 <= nc < n:
                    
                    # Check if already processed (visited)
                    if (nr, nc) not in visited:
                        
                        # 4. Calculate the new time required to reach the neighbor
                        # The time must be at least 't' (the time to reach the current cell)
                        # AND at least the neighbor's elevation.
                        new_time = max(t, grid[nr][nc])
                        
                        # Mark as visited (since we push it to the heap, we've found
                        # a path, and the heap logic handles the minimum)
                        visited.add((nr, nc))
                        
                        # 5. Push the neighbor to the heap
                        heapq.heappush(min_heap, (new_time, nr, nc))
                        
        return -1 # Should not be reached based on problem constraints