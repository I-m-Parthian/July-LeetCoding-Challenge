class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        Exor = x ^ y;
        # count set bits in this
        BitCount=0;
        while Exor:
            if Exor & 1:
                BitCount+=1
            Exor = Exor>>1
        return BitCount
