#1) https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python
#2) https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/python
#3) https://www.codewars.com/kata/515e271a311df0350d00000f/train/python
#4) https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/python
#5) https://www.codewars.com/kata/544675c6f971f7399a000e79/train/python 


#1)
def positive_sum(arr):
    return sum(x for x in arr if x > 0)
#2)
def remove_char(s):
    return s[1:-1]
#3)
def square_sum(numbers):
    return sum(x ** 2 for x in numbers)
#4)
def find_smallest_int(arr):
    return min(arr)
#5)
def string_to_number(s):
    return int(s)


print("Positive Sum:", positive_sum([1, -2, 3, 4, -5]))   
print("Remove Char:", remove_char("Hello"))              
print("Square Sum:", square_sum([1, 2, 3]))              
print("Smallest Int:", find_smallest_int([7, -3, 0, 9])) 
print("String to Number:", string_to_number("12345"))   