#special case
for i in range(3):
    print(i)
    i+=2
print(i)
#The loop will run 3 times, with i taking the values 0, 1, and 2 in each iteration.
#However, this increment does not affect the next iteration because the for loop reassigns i
# to the next value in the sequence (range(3))

#Why does the final value of i become 3?
#The for loop does not "reset" or "destroy" the variable i after the loop ends. 
# The variable i still exists and retains its last value.
#In the last iteration of the loop, i was incremented to 3 (from 2), and this value persists after the loop.