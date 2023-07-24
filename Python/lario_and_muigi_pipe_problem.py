def pipe_fix(nums):
    
    
    for i in range(min(nums), max(nums)):
        if i not in nums:
            nums.append(i)
            nums.sort()
            
    return nums