nums=[1,0,1,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1]


count=0
Lstring=0

for i in range(len(nums)):
    if nums[i]==1:
       count +=1
    #    count1=count
    #    print(count)
    if nums[i]==0:
        # print(count)
        if Lstring<count or Lstring:
            # print(count)
            Lstring=count            
            count=0
print(Lstring)


# largest=nums[0]
# second=0

# for num in nums:
#     if num > largest:
#          second=largest 
#          largest=num

#     if num < largest and num > second :
#          second = num

# print(second)
# print(largest)