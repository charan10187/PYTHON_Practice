result=[]
final=[]
nums=[1]        # if len(nums)==1:
        #     return nums[i]
for i in range(len(nums)):
    for j in range(len(nums)):
        if i!=j and nums[i]==nums[j]:
            result.append(nums[i])
for num in range(len(nums)):
    if nums[num] not in result:
        final.append(nums[num])
for i in range(len(final)):
    print(final[i])
