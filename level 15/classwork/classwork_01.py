#1)მომხმარებელს შეიყვანს თვის ნომერს (1-12) და პროგრამა ამოიცნობს სეზონს (ზამთარი, გაზაფხული, ზაფხული, შემოდგომა) 

season = int(input("შეიყვანე თვის ნომერი (1-12):  "))


if season == 1 or 2 or 3:
    print("Spring")

elif season == 4 or 5 or 6:
    print("Summer")

elif season == 7 or 8 or 9:
    print("Autumn")
    
else:
    print("Winter")