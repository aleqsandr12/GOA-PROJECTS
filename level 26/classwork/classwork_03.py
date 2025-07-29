#დაწერე ფუნქცია max_of_three, რომელიც იღებს სამ მთელ რიცხვს და აბრუნებს მათგან უდიდესს.
#👉 გამოიყენე if-elif-else პირობები და შედარებები.

def max_of_three(no, yeas, huh):
    if no >= yeas and no >= huh:
        return no
    elif yeas >= no and yeas >= huh:
        return yeas
    else:
        return huh
