# leetcode problem 136 Single Number

nums=list(input("nums = "))
result=[]
final=[]

# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if i!=j and nums[i]==nums[j]:
#             result.append(nums[i])

# for num in range(len(nums)):
#     if nums[num] not in result:
#         final.append(nums[num])

# for i in range(len(final)):
#     print(final[i])


# ----------------------------------------------------
for i in range(len(nums)):
    for j in range(len(nums)):
        if i!=j and nums[i]==nums[j]:
            result.append(nums[i])
            print(result)
            if nums[i] not in result:
                final.append(nums[i])
                print(final)
for i in range(len(final)):
    print(final[i])