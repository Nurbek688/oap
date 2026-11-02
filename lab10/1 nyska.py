#    1 нұсқа
def process_text_system(search_word, replace_from, replace_to, code_value, text='Студенттер Python тілін зертханада үйренеді. Python пайдалы.'): #process_text_system функциясы мәтінді өңдеу үшін қолданылады.   
    print("\n" + "="*40) #print функциясы мәтіннің басында және соңында 40 таңбалы сызық шығарады.
    print('Кіріс мәтіні: ', text) #print функциясы кіріс мәтінін шығарады.
    print('Іздеу сөзі: ',search_word,  '| Код: ', code_value) #print функциясы іздеу сөзін және код мәнін шығарады.
    print('='*40) #print функциясы мәтіннің басында және соңында 40 таңбалы сызық шығарады.
    total_len=len(text) #total_len переменна мәтіннің ұзындығын есептейді.
    words_list=text.split() #words_list переменна мәтінді сөздерге бөледі.
    word_count=len(words_list) #word_count переменна мәтіндегі сөздердің санын есептейді.

    non_space_count=0 #non_space_count переменна бос орындарды есептейді.
    for ch in text: #for цикл мәтіндегі әрбір таңбаны тексереді.
        if ch==' ': #if шарт мәтіндегі таңба бос орын болмаса, non_space_count переменна 1-ге артады.
            non_space_count += 1 #non_space_count переменна 1-ге артады.
    print('Жалпы ұзындығы: ', total_len) #print функциясы мәтіннің жалпы ұзындығын шығарады.")
    print('Сөз саны: ', word_count) #print функциясы мәтіндегі сөздердің санын шығарады.
    print('Бос орындар саны: ', non_space_count) #print функциясы мәтіндегі бос орындар санын шығарады.
process_text_system(search_word='Python', replace_from='студент', replace_to='оқушы', code_value=123) #process_text_system функциясы шақырылады, іздеу сөзі 'Python', ауыстырудан бұрынғы сөз 'студент', ауыстырудан кейінгі сөз 'оқушы', код мәні 123 болып табылады.

          