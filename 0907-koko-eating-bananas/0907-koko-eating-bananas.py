class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ### Binary Search
        l, r = 1, max(piles)

        while l<r:
            mid = (l+ r)//2 #integer division
            if sum(ceil(i/mid) for i in piles) <= h :
                r = mid
            else:
                l = mid+1
        return l


        ####### Brute-force main logic
        # for k in range(1, max(piles)):
        #     total = 0
        #     for each in piles:
        #         total += ceil(each/k)
        #     print(k, total)

        