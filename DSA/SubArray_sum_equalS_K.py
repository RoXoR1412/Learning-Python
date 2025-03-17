def max_count(nums,k):
    prefix_sum={0:1}
    curr_sum=0
    count=0
    for num in nums:
        curr_sum+=num
        if curr_sum-k in prefix_sum:
            count+=prefix_sum[curr_sum-k]
        prefix_sum[curr_sum]=prefix_sum.get(curr_sum,0)+1
    return count
# Example usage:
nums = [1, 1, 1]
k = 2
print(max_count(nums,k))  # Output: 2 (1+1, 1+1)
nums = [1]
k = 1
print(max_count(nums,k))  # Output: 2 (1+2, 3)