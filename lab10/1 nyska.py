# 1 нұсқа
def process_text_system(text, search_word, replace_from, replace_to, code_value):
# 1. Сначала делаем замену слова в тексте
    changed_text = text.replace(replace_from, replace_to)
    # Выводим измененный текст на экран
    print('Кіріс мәтіні: ', changed_text) 
    print('Іздеу сөзі: ',search_word, ' | Код: ',code_value)
    # 2. Считаем статистику уже для НОВОГО (измененного) текста
    total_len = len(changed_text) 
    words_list = changed_text.split() 
    word_count = len(words_list)
    # Цикл подсчета пробелов в новом тексте
    non_space_count = 0
    for ch in changed_text: 
        if ch == ' ':
            non_space_count += 1
    # Вывод корректных финальных данных
    print('Жалпы ұзындығы: ', total_len)
    print('Сөз саны: ', word_count)
    print('Бос орындар саны: ', non_space_count)
# ==========================================
# КОД ВВОДА И ВЫЗОВА (пишется без отступов с самого начала строки)
user_text = input("Мәтінді енгізіңіз: ")
user_search = input("Іздеу сөзін енгізіңіз: ")
user_from = input("Қандай сөзді ауыстыру керек: ")
user_to = input("Немен ауыстыру керек: ")
user_code = int(input("Код мәнін енгізіңіз: "))
# Запуск функции с переданными переменными
process_text_system(
    search_word=user_search, 
    replace_from=user_from, 
    replace_to=user_to, 
    code_value=user_code, 
    text=user_text
)

