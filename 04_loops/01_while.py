# Python Toolkit
# loops/while

# A while loop will continue to run as long as the condition is true
# Beware infinite loops where the condition is always true!
# For more on while loops see:
# https://www.tutorialspoint.com/python/python_while_loop.htm

# This loop will print the numbers 10 to 1 and then exit

x = 10

while (x > 0):
    print(x)
    x = x - 1

# This loop will never end!

run = True

while (run == True):
    print('Just keep running')

# You can stop a run away loop using Ctrl+C
