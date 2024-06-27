nickname = input()
flag = 'Incorrect'

if (5 <= len(nickname) <= 15 
    and nickname.startswith('@') 
    and nickname[1:].isalnum()
    and nickname == nickname.lower()
):       
    flag = 'Correct'

print(flag)

"""
Во время собеседования вам предложили решить задачу на валидацию имени пользователя. 
Пользователь пытается создать никнейм для своего аккаунта в соцсети Y. 
Правила для корректного никнейма в соцсети Y следующие:

никнейм должен начинаться с символа @
никнейм должен содержать от 5 до 15 (включительно) символов (включая первый символ @)
никнейм должен содержать только строчные буквы и цифры (помимо первого символа @)
Напишите программу, которая выводит «Correct» (без кавычек), если никнейм соответствует всем 
вышеприведенным правилам, или «Incorrect» (без кавычек) в противном случае.
"""