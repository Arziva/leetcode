class Solution:
    def countBits(self, n):
        def count1(n):
            num_str = format(int(n), 'b')
            count = 0
            for i in num_str:
                if i == '1':
                    count += 1
            return count

        #main
        arr = []
        for i in range(n+1):
            y = count1(i)
            arr.append(int(y))
        return arr




