#შექმენით ფუნქცია, რომელიც იღებს წინადადებას, და მასში space-ების მაგივრად სიტყვებს შორის ჩასვამს ტირეს("-"). საბოლოოდ კი აბრუნებს მას

def replace_spaces_with_dash(sentence):
    words = sentence.split()
    result = ""
    for i in range(len(words)):
        result += words[i]
        if i != len(words) - 1:
            result += "-"
    return result
