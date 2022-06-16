class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerLeft = n
        if(len(flowerbed)==1 and flowerbed[0] == 0):
            flowerLeft -= 1
            if flowerLeft <= 0:
                return True
            else:
                return False
        if(flowerbed[0] == 0 and flowerbed[1] == 0):
            flowerbed[0] = 1
            flowerLeft -= 1
        if(flowerbed[-1] == 0 and flowerbed[-2] == 0):
            flowerbed[-1] = 1
            flowerLeft -= 1
            
        
        for i in range(len(flowerbed)-1):
            if flowerbed[i] == 1:
                continue
            elif (flowerbed[i-1] == 0 and flowerbed[i+1] ==0):
                flowerbed[i] = 1
                flowerLeft = flowerLeft - 1
            else:
                continue
        print(flowerbed)
        print(flowerLeft)
        if flowerLeft <= 0:
            return True
        else:
            return False
