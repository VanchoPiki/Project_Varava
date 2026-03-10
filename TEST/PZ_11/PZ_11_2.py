"""
2. Составить генератор (yield), который преобразует все буквенные символы в
строчные.
"""
try:

    def lowercase_generator(text):
        for char in text:
            yield char.lower()


    input_string = ("Привет")
    gen = lowercase_generator(input_string)
    result = "".join(gen)

    print(f"Результат работы генератора: {result}")

except ValueError as e:
    print(e)