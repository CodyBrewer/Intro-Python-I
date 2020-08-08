# Write a function is_even that will return true if the passed-in number is even.
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
# YOUR CODE HERE
print(is_even(3)) # should return false
print(is_even(46)) # should return 
# Read a number from the keyboardprint(f"{waypoints} \n" )
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
# YOUR CODE HERE
def check_input_num(bool):
    if bool == True:
        return "Even!"
    return "Odd"

print(check_input_num(is_even(num)))
