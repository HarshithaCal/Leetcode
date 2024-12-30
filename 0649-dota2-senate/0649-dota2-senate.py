class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r_arr = []
        d_arr = []
        for i in range(n):
            if senate[i] == "R":
                r_arr.append(i)
            else:
                d_arr.append(i)
        
        while r_arr and d_arr:
            r = r_arr.pop(0)
            d = d_arr.pop(0)
            if r < d: #r bans d
                r_arr.append(n+r) #round about
            else:
                d_arr.append(n+d)
        
        if not r_arr:
            return "Dire"
        else:
            return "Radiant"



        