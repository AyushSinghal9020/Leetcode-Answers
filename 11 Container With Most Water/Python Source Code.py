class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        area = 0
        
        for i in range(len(height)):
        
            for j in range(len(height)):
        
                if height[i] > height[j]:
        
                    diff = height[i] - height[j]
        
                else :
        
                    diff = height[j] - height[i]
        
                if i > j:
        
                    sample_area = (height[i] - diff) * (i - j)
        
                else :
        
                    sample_area = (height[i] - diff) * (j - i)
        
                if sample_area > area:
                
                    area = sample_area
        
        return area
