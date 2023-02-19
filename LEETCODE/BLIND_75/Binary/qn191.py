class Solution:
    def hammingWeight(self, n: int) -> int:
        #num_str = str(bin(n)[2:])
        num_str = format(int(n), 'b')
        count = 0
        for i in num_str:
            if i == '1':
                count += 1
        return count
