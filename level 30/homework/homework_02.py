#შექმენით ფუნქცია, რომელიც მიიღებს წინადადებას და დაბეჭდავს მის თითოეულ სიტყვაში სიმბოლოების რაოდენობას(ცალ-ცალკე)

def print_word_lengths(sentence):
    words = sentence.split()
    for word in words:
        count = 0
        for char in word:
            count += 1
        print(f"'{word}' - {count} სიმბოლო")
