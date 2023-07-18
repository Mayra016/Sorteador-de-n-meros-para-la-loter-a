import random
            
def generar2():
    nums = []
    while len(nums) < 6:
        num = random.randrange(1, 60)
        if num not in nums:
            nums.append(num)
    return nums        
    
print(generar2())    
