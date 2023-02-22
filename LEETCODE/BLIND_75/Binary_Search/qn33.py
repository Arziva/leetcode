class Solution:
    def search(self, nums, target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r] :
                    r = mid - 1
                else:
                    l = mid + 1

            

            #elif target > nums[m] or target < nums[m] and target > nums[0] :
            #    l = m + 1
            #elif target < nums[m] and target < nums[0]: 
            #    r = m - 1


        else:
            return -1
