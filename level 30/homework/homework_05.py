#შექმენით ფუნქცია, რომელსაც გადაეცემა წინადადება. თქვენი დავალებაა ამ წინადადების სიტყვები შეაბრუნოთ და დააბრუნოთ(სიტყვების სიმბოლოები
#  არ უნდა იყოს შებრუნებული)

def reverse_word_order(sentence):
    words = sentence.split()
    result = ""
    for i in range(len(words) - 1, -1, -1):
        result += words[i]
        if i != 0:
            result += " "
    return result
