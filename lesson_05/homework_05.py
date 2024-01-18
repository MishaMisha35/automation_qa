small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
elements = set(small_list)
print(elements)
# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
average_small_list = sum(small_list) / len(small_list)
print(average_small_list)
# task 3. Перевірте, чи є в списку big_list дублікати
duplicates_big_list = len(big_list) != len(set(big_list))
print(duplicates_big_list)

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
max_number = max(add_dict, key=add_dict.get)
print(max_number)
# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
flip = {v: k for k, v in add_dict.items()}
print(flip)
# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = {}

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
unique_chars_set = set(line)
print(unique_chars_set)
# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
sum_of_unique_elements = sum(set_1.symmetric_difference(set_2))
print(sum_of_unique_elements)
# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
