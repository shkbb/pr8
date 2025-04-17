# Завдання 1: Фільтрація чисел
multiples_of_3_not_5 = [x for x in range(1, 101) if x % 3 == 0 and x % 5 != 0]
print("Завдання 1:", multiples_of_3_not_5)

# Завдання 2: Перетворення температури
celsius = [0, 10, 20, 30, 40, 100]
fahrenheit = [c * 9 / 5 + 32 for c in celsius]
print("Завдання 2:", fahrenheit)

# Завдання 3: Квадрати парних чисел
even_squares = [x ** 2 for x in range(1, 51) if x % 2 == 0]
print("Завдання 3:", even_squares)

# Завдання 4: Аналіз тексту
text = "Python is amazing and powerful language"
word_lengths = [len(word) for word in text.split()]
print("Завдання 4:", word_lengths)

# Завдання 5: Складні числа
composite_numbers = [
    x for x in range(2, 101)
    if len([d for d in range(1, x + 1) if x % d == 0]) > 2
]
print("Завдання 5:", composite_numbers)
