from datetime import datetime

c = datetime.now()
print(c.strftime('%d.%m.%Y %H:%M:%S'))
with open('G:/proba.txt', 'a', encoding='utf-8') as fw:
     fw.write("Пробуем планировщик задач \n")
     fw.write(c.strftime('%d.%m.%Y %H:%M:%S'))
     fw.write("\n")
     fw.write("\n")