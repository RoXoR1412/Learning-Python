from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum=[0]*len(nums)
        self.prefix_sum[0]=nums[0]
        for i in range(1, len(nums)):
            self.prefix_sum[i]=self.prefix_sum[i-1]+nums[i] 
        #print(self.prefix_sum)       

    def sumRange(self, left: int, right: int) -> int:
        if left==0: return self.prefix_sum[right]
        return self.prefix_sum[right]-self.prefix_sum[left-1]
    
        # Example usage:
nums = [1, 2, 3, 4, 5]
obj = NumArray(nums)
print(obj.sumRange(0, 2))  # Output: 6 (1+2+3)
print(obj.sumRange(1, 3))  # Output: 9 (2+3+4)
print(obj.sumRange(0, 4))  # Output: 15 (1+2+3+4+5)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)