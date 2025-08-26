#შექმენით ფუნქცია, რომელიც მიიღებს წინადადებას, ფუნქციამ ამ წინადადების თითოეული სიტყვა უნდა შეინახოს სიაში, როგორც ცალკე ელემენტი.
#  საბოლოოდ გადააქციეთ სია ისევ წინადადებად, სადაც სიტყვებს შორის არის მძიმე და ერთი დაშორება(", ")


def split_and_rebuild(sentence):
    words = sentence.split()
    result = ""
    for i in range(len(words)):
        result += words[i]
        if i != len(words) - 1:
            result += ", "
    return result
