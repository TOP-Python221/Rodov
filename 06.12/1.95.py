from string import punctuation, whitespace

punctuation += '’'
stops = ('.', '!', '?')


# ДОБАВИТЬ: аннотации типов параметров и возвращаемого значения
def sentence_case(message):
    # ДОБАВИТЬ: документацию функции

    message = message.strip().capitalize() + ' '
    # КОММЕНТАРИЙ: по-хорошему, здесь, конечно, нужна регулярка — но это не значит, что нельзя справиться без неё: вам нужно рассмотреть все случаи, когда I является самостоятельным словом, но при этом может быть окружено символами пространства и знаками препинания
    # ИСПОЛЬЗОВАТЬ: если бы мне было пофиг на производительность — а в этой задаче с короткими фразами на неё явно можно забить — то я бы написал что-то вроде такого перебора:
    for start_char in punctuation + whitespace:
        for end_char in punctuation + whitespace:
            substr = f'{start_char}i{end_char}'
            replace = f'{start_char}I{end_char}'
            message = message.replace(substr, replace)

    words = message.split(' ')
    for i, word in enumerate(words):
        if word.endswith(stops):
            words[i+1] = words[i+1].capitalize()
    clear_text = ' '.join(words)
    return clear_text.strip()


# tests:
print(sentence_case('what time do i have to be there? what’s the address? this time i’ll try to be on time!'))
# What time do I have to be there? What’s the address? This time I’ll try to be on time!


# КОММЕНТАРИЙ: местами вы довольно близко подобрались =) но в разных фрагментах
# СДЕЛАТЬ: изучите представленный код функции


# ИТОГ: половину зачитываю за старание — 3/6


    # # print(type(message))
    # words = message.split(' ')
    # for i in range(len(words)):
    #     if '?' in words[i]:
    #         upper = words[i+1].capitalize()
    #         words[i+1] = upper
    #         # print(words[i+1].capitalize())
    #         upper = ' '.join(words)
    # print(upper)
            # if words[0].startswith('w'):
                # print(words[0])
                # words[0].capitalize() 
                # print(words[0])
                # upper = ' '.join(words)
                # print(upper)
    # print(' '.join(words))
    # print(upper)

# Вверху более-менее итог, к которому я смог прийти. Пробовал разбить строку на слова и уже с ними работать, 
# но самое первое слово не поддаётся редактированию
    
            # if upper.islower():
                # upper.capitalize()
                # print(upper)
            # print(type(words))
            # print(words)
        # if words[0].startswith('w'):
            # words[0].capitalize()
            # print(words[0])
            # print(upper)

# Это моя вторая попытка попробовать зайти с другой стороны
    # for j in range(len(words)):
        # if 'i' in upper[j]:
            # upper = upper[j].capitalize()
            # print(upper)
    # print(words)
    
# Ну, и это третья попытка возвести в верхний регистр букву i  
