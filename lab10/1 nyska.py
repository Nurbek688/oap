def analyze_text(text, search_word, old_word, new_word):
    length = len(text)
    words = text.split()
    word_count = len(words)
    non_space_count = 0
    for i in text:
        if not i.isspace():
            non_space_count += 1
    print('\n======== Мәтіннің талдауы ========')
    print('Сөздің ұзындығы:', length)
    print('Сөздегі сөздердің саны:', word_count)
    print('Сөздегі бос орындарсыз символдардың саны:', non_space_count)

    lower_text = text.lower()
    lower_search = search_word.lower()
    first_index = lower_text.find(lower_search)
    word_occurrences = lower_text.count(lower_search)
    print('Бірінші сөз:', search_word, 'индексі:', first_index)
    print('\n======= Сөз ауысуы =======')
    updated_text = text.replace(old_word, new_word)
    print('Өзгерген мәтін:', updated_text)
def check_code(code):
    print('\n====== Кодты тексеру ======')
    code = code.strip()

    is_valid = (len(code) == 6 and
                code[:2].isalpha() and
                code[:2].isupper() and
                code[2] == '-' and
                code[3:].isdigit())
    if is_valid:
        print('Код:', code, 'дұрыс пішім')
    else:
        print('Код:', code, 'қате пішім')
print('\n======== Пользаватель енгізетін мәліметтер ========')
my_text = input('Мәтінді енгізіңіз: ')
my_search = input('Ізделетін сөзді енгізіңіз: ')
word_to_replace = input('Ауыстырылатын сөзді енгізіңіз: ')
replacement_word = input('Жаңа сөзді енгізіңіз: ')
my_code = input('Кодты енгізіңіз: ')
print('\n=== Пользаватель енгізгеннен кейінгі нәтиже === ')
analyze_text(my_text, my_search, word_to_replace, replacement_word)
check_code(my_code)



