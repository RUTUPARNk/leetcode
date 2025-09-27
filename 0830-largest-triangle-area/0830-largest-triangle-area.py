from typing import List

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # cross product helper
        def cross(p1, p2, p3):
            return (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])
        
        # area of triangle
        def triangle_area(a, b, c):
            return abs(cross(a, b, c)) / 2.0
        
        # convex hull (monotone chain)
        def convex_hull(points):
            points = sorted(set(map(tuple, points)))
            if len(points) <= 1:
                return points

            lower = []
            for p in points:
                while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                    lower.pop()
                lower.append(p)

            upper = []
            for p in reversed(points):
                while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                    upper.pop()
                upper.append(p)

            return lower[:-1] + upper[:-1]
        
        hull = convex_hull(points)
        h = len(hull)
        if h < 3:
            return 0.0
        
        max_area = 0.0
        # rotating calipers
        for i in range(h):
            for j in range(i+1, h):
                k = (j+1) % h
                while True:
                    next_k = (k+1) % h
                    if triangle_area(hull[i], hull[j], hull[next_k]) > triangle_area(hull[i], hull[j], hull[k]):
                        k = next_k
                    else:
                        break
                max_area = max(max_area, triangle_area(hull[i], hull[j], hull[k]))
        
        return max_area
