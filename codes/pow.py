# Input: integer a, b
# Output a^b
def power(a, b):
    result = 1
    while (b != 0):
        # check b is even or odd
        if(b % 2):
            # b is odd
            result *= a
        b = b / 2    
        a *= a  
    return result
