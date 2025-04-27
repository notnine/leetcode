class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        
        for i in range(32):
            abit = (a >> i) & 1
            bbit = (b >> i) & 1
            cbit = (c >> i) & 1

            # when cbit == 0, need 1 flip when 1 of abit or bbit == 1, 2 flips when both 1
            # when cbit == 1, need 1 flip when both abit and bbits == 0
            if cbit == 0:
                if abit & bbit:
                    flips += 2
                elif abit | bbit:
                    flips += 1
            else:
                if abit == 0 and bbit == 0:
                    flips += 1
        
        return flips

        # O(1) time & space