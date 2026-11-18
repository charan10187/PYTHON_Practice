'''
        Problem 30 -- Remove All Occurrences of a Digit
        Input = 122342
        Remove digit = 2

        output = 134
'''
N=int(input("Input = "))
target=int(input('Remove digit = '))
output=0
rev=0
while N!=0:
    digit=N%10
    # print(digit)
    if digit!=target:
        # print(digit,"==",target)
        output=output*10+digit
        # print(output)
    N//=10
while output!=0:
    digit2=output%10
    rev=rev*10+digit2
    output//=10
print("Output = ",rev)
