class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # count = 0
        # if flowerbed[0] == flowerbed[1]== 0:
        #     count+=1
        #     flowerbed[0] = 1 
        #Need to deal with the last index as well so better way is:
        # for i in range(1, len(flowerbed)-1):
        #     print(flowerbed)
        #     if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
        #         count +=1
        #         flowerbed[i] = 1

        # if count >= n:
        #     return True    
        # return False
        count = 0
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:
                #check for 0th and last index!!! 
                prev = (i == 0 or flowerbed[i - 1] == 0)
                next = (i == length - 1 or flowerbed[i + 1] == 0)
                if prev and next:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
        
        return count >= n


        