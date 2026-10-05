text = input("Введите строку: ")
result = ""
is_upper = False
for char in text:
    if not char.isalpha():
        result += char
        continue
    if is_upper:
        result += char.upper()
    else:
        result += char.lower()
    is_upper = not is_upper
print(result)