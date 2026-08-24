'''
        Program 24 -- Find the Difference Between Sum of Even and Odd Digits
        Input = 123456
        Difference = 3

'''
N=int(input("Input = "))

even_sum=0
odd_sum=0

while N!=0:
    digit=N%10
    if digit%2==0:
        even_sum+=digit
    else:
        odd_sum+=digit
    N//=10
print(even_sum)
print(odd_sum)
print("Difference = ",even_sum-odd_sum)