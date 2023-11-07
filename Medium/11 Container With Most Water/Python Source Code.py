# <-----------METHOD 1----------->

class Solution:
    
    def maxArea(self, height: List[int]) -> int:

        sorted_height = sorted(height)
        sorted_height.reverse()
        max_height = sorted_height[0]
        counter = 0
        max_area = 0

        while counter < len(height) - 1 :
            
            sample_height = height

            next_height = sorted_height.pop(1)

            max_index = sample_height.index(max_height)
            sample_height.pop(max_index)
            next_index = sample_height.index(next_height)

            length = next_height
            breadth = abs(max_index  - next_index)

            area = length * breadth

            if area > max_area : max_area = area

            counter += 1

        return max_area

# <-----------METHOD 2----------->

class Solution:
    
    def maxArea(self, height: List[int]) -> int:

        max_area = 0
        max_height = max(height)
        max_index = height.index(max_height)

        for index in range(len(height)):

            length = height[index]
            breadth = abs(index - max_index)

            area = length * breadth

            if area > max_area : max_area = area

        return max_area

# <-----------METHOD 3----------->

class Solution:
    
    def maxArea(self, height: List[int]) -> int:

        max_area = 0

        for index_1 in range(len(height)):

            for index_2 in range(index_1 , len(height)):

                length = min(height[index_1] , height[index_2])
                breadth = abs(index_1 - index_2)

                area = length * breadth

                if area > max_area : max_area = area

        return max_area

        max_area = 0

# <-----------METHOD 4----------->

class Solution:
    
    def maxArea(self, height: List[int]) -> int:

        while len(height) > 2 :
            print(height) 
            
            right = height.pop(-1)
            left = height.pop(0)

            right_index = len(height)

            length = min(right , left)
            breadth = right_index

            area = length * breadth

            if area > max_area : max_area = area 

        return max_area

# <-----------METHOD 5----------->

class Solution:
    
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            
            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:left += 1
            else:right -= 1

        return maxArea
