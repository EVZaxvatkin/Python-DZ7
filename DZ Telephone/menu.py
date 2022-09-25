from action import *


print('ТЕЛЕФОННАЯ КНИГА')
print()

print('МЕНЮ:')
print('1. Создать контакт.')
print('2. Посмотреть список контаков.')
print('3. Экспорт/импорт контактов.')
var = input('Выберете действие: ')

if var == '1':
    new_contact()
    print('Новый контакт сохранен в файле Contacts.txt')

if var == '2':
    print('Список ваших контактов: ')
    all_contact()

if var == '3':
    import_contact()
    print('Произведен импорт новых контактов. Новый список контактов в файле Importfile.txt')