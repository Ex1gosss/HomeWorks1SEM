###1 
def replace_and_count_n(s):
    max_count = 0
    current_count = 0
    new_string = ""

    for char in s:
        if char == 'н':
            current_count += 1
        else:
            # Проверяем текущую последовательность
            if current_count > max_count:
                max_count = current_count
            # Заменяем последовательность 'н' на '!'
            new_string += '!' * current_count
            current_count = 0
            new_string += char
    if current_count > max_count:
        max_count = current_count
    new_string += '!' * current_count

    return new_string, max_count

# Пример использования
input_string = "нннabcнnnnнxyzнн"
new_string, count = replace_and_count_n(input_string)

print("Новая строка:", new_string)
print("Максимальная длина подряд идущих букв 'н':", count)


###2
def extract_inner_characters(s):
    open_index = s.find('(')
    close_index = s.find(')')

    if open_index != -1 and close_index != -1 and open_index < close_index:
        return s[open_index + 1:close_index]
    else:
        return "Скобки не найдены или расположены неправильно."

# Пример использования
input_string = "Это пример (внутренние символы) текста."
inner_characters = extract_inner_characters(input_string)

print("Символы внутри скобок:", inner_characters)

###3
def extract_words(s):
    words = s.split()
    result = []

    for word in words:
        if word.lower().startswith('а') or word.lower().endswith('я'):
            result.append(word)

    return result

# Пример использования
input_string = "Абстракция, авария, аллея."
words_found = extract_words(input_string)

print("Найденные слова:", words_found)

