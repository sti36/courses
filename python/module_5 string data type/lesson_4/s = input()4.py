s = input()              
total = 0                    
line = ''                   
for i in s:            
    if s.count(i) >= total:   # Если количество символов в строке больше либо равны уже сохраненому
        total = s.count(i)   # Записываем новое значение кол-ва символов
        line = i            # Запоминаем символ
print(line)