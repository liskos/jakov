def count_substring(s, substring):
    """Возвращает количество вхождений подстроки в строке."""
    return s.count(substring)


def max_length_with_exact_occurrences(file_path, substring, target_count):
    """Находит максимальную длину последовательности, где подстрока встречается ровно target_count раз."""
    with open(file_path, 'r') as file:
        text = file.read().strip()  # Читаем файл и удаляем лишние пробелы

    max_length = 0
    n = len(text)

    for start in range(n):
        for end in range(start + 1, n + 1):
            substring_to_check = text[start:end]
            if count_substring(substring_to_check, substring) == target_count:
                max_length = max(max_length, len(substring_to_check))

    return max_length


# Путь к вашему текстовому файлу
file_path = 'x73tzLF0PK.txt.txt'
substring = 'FSRQ'
target_count = 80

result = max_length_with_exact_occurrences(file_path, substring, target_count)
print(f"Максимальная длина последовательности: {result}")
