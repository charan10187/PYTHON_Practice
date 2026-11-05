# Lesson 1: What is recursion?
# Recursion is a programming technique in which a function 
# calls itself to solve a smaller version of the same problem.

# Consider this example:
def greet():
    print("Hello")
    greet()

greet()

# when there is no stoping the python automatically raises RecursionError

# Lesson 2: The two essential parts of recursion
# Every properly terminating recursive function needs two things:

# 1. Base condition

# The condition that stops recursion.

# 2. Recursive call

# The function calling itself with a smaller or simpler problem.

# Example:
def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)

countdown(3)

# output: 3
        # 2
        # 1

        