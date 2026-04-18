"""
2. Составить генератор (yield), который преобразует все буквенные символы в
строчные.
"""
try:

    def main(text: str):
        yield from map(str.lower, text)

    input_str = "Привет"

    print("".join(main(input_str)))

except ValueError as e:
    print(e)