def twoSum(nums: List[int], target: int) -> List[int]:
    outputs = []

    for i in range(len(nums) - 1): 
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                outputs = [i, j]  
                break 
        if outputs:  
            break  

    return outputs