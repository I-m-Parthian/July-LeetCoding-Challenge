'''
### Question ####

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.







#### Solution ####

*/

'''


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
