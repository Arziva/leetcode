from ast import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        lens = len(nums)
        print (lens)
        #for i in range(0, lens):
        #   print(nums[i])
        #middle = lens/2
        #print (middle)
        #print(lens//2)
        if ( (lens%2) == 0):
            print("yo")
            return ( float( ( nums[lens//2-1] + nums[(lens//2)] ) /2 ) )
            
        else: #if(lens != 0):
            print("else")
            return nums[lens//2]
            