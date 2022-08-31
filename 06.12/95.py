
def newmessage(message):
    # print(type(message))
    words = message.split(' ')
    for i in range(len(words)):
        if '?' in words[i]:
            upper = words[i+1].capitalize()
            words[i+1] = upper
            # print(words[i+1].capitalize())
            upper = ' '.join(words)
    print(upper)
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
    
newmessage('what time do i have to be there? what’s the address? this time i’ll try to be on time!')

 