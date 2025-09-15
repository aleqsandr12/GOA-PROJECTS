#his is how to multiply
def multiply(a,b):
    return a * b

print(multiply(500 , 2))

#how to %

def Even_or_odd(number):
    if 100%2==0:
        return "Even"
   
    else:
        return "odd"

#plus minus and others 

print(13 % 2) # nastiani gakofa
print(10 / 2) # ubralod gakofa

print(5 * 5) # gamravleba
print(3 ** 2) # samis orjer gamravleba 3 * 3
print(3 ** 3) # samis samjer gamravleba 3 * 3 * 3
print(3 ** 4) # samis 4-jer gamravleba 3 * 3 * 3 * 3


print(10 // 2) # ramdenjer motavsda ori magas gvichvenebs



# if elif else
num = int(input("Enter Any Number:  "))

if num <= 10:
    print("num is less than 10")

elif num <= 100:
    print("num is less than 100")

else:
    print("idk")
    #-----------------------

def is_even(num):
    res = []
    for i in num:
        if i % 2 == 0:
            res.append(i)

    return "res"

print(is_even([1 , 2 , 3 , 4 , 5 ]))