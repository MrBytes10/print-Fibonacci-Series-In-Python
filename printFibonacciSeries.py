# printFibonacciSeries
# The Logic is derived from the meaning of Fibonacci Series:
# Fibonacci Series is a series of numbers in which each number(Fibonacci Number) is the sum of two preceding numbers.
# An example is 0,1,1,2,3,5,8,13,21,34, etc...
num1=0
num2=1

print(num1)
print(num2)

for i in range(2,20):
    sum= num1 + num2 # here we should get the result of 0+1
    print(sum) # prints 1 ### prints the current Fibonacci number
    num1=num2 # after printing sum; num1 takes place of num2 ##update num1 to the next number in the sequence
    num2=sum # after printing sum; the resulting sum is now our num2 # update num2 to the next number in the sequence
    # This is a "for" looping statement
    