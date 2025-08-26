# შექმენით ფუნქცია, რომელიც იღებს წინადადებას, სადაც ყოველი სიტყვის შორის ერთზე მეტი დაშორებაა(space). 
# თქვენი დავალებაა ჩამოაშოროთ გადმოცემულ წინადადებას ზედმეტი space-ები(სიტყვებს შორის მხოლოდ ერთი უნდა იყოს). საბოლოოდ დააბრუნეთ ეს წინადადება

def remove_extra_spaces(sentence):
    words = sentence.split()  # ეს მაინც გამოიყენება სწორად
    result = ""
    for i in range(len(words)):
        result += words[i]
        if i != len(words) - 1:
            result += " "
    return result
