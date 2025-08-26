#1)სტრინგის ფორმატირება
#შექმენით სტრიქონი სახელწოდებით template შემდეგი შინაარსით: "Hello, {name}. Welcome to {place}."
#გამოიყენეთ format() ფუნქცია, რომ ჩაანაცვლოთ {name} "Alice"-ით და {place} "Wonderland"-ით.
#შეინახეთ შედეგი ცვლადში სახელწოდებით formatted_string და დაბეჭდეთ იგი.

template = "Hello, {name}. Welcome to {place}."

formatted_string = template.format(name="Alice", place="Wonderland")

print(formatted_string)