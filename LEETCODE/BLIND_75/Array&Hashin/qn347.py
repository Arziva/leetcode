class Solution:
    def topKFrequent(self, nums, k):
        ele_count = {}
        arr = []

        for i in nums:
            if i not in ele_count:
                ele_count[i] = 1
            else:
                ele_count[i] += 1
        
        ele_count = sorted(ele_count.items(), key =  lambda kv: kv[1], reverse = True)
        print(ele_count)
        ele_count = dict(ele_count)

        i = 0
        for num,occurance in ele_count.items():
            i += 1
            if i > k:
                break
            arr.append(num)

        return arr

    
            