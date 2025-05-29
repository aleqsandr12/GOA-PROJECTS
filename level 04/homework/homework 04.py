#დაპრინტეთ ყველა შესაძლო ვარიანტი and და or ით, მაგალითი: 
#print(True and False)
#print(True and True)
#print(False and False)


# -------- AND ოპერატორი --------
print(True and True)     # ✅ ორივე პირობა True → შედეგი: True
print(True and False)    # ❌ ერთი მაინც False → შედეგი: False
print(False and True)    # ❌ ერთი მაინც False → შედეგი: False
print(False and False)   # ❌ ორივე False → შედეგი: False

# -------- OR ოპერატორი --------
print(True or True)      # ✅ ერთი მაინც True → შედეგი: True
print(True or False)     # ✅ ერთი მაინც True → შედეგი: True
print(False or True)     # ✅ ერთი მაინც True → შედეგი: True
print(False or False)    # ❌ ორივე False → შედეგი: False
