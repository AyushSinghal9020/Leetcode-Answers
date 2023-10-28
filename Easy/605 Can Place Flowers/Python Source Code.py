class Solution:
    
  def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        leng = len(flowerbed)
        index  = 0

        while index < leng:

            if flowerbed[index] == 0 :
                
                if (index + 1 == leng and flowerbed[index] == 0): 
                    
                    n -= 1
                    
                    break
                
                elif flowerbed[index + 1] == 0 :
                    
                    n -= 1
                    index += 2
                
                else : index += 1
            else : index += 2
        
        if n <= 0 : return True
        return False 
        
