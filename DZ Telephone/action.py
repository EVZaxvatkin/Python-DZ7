       
from asyncore import read




def new_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    telephone = input('Введите номер телефона: ')
    contactDetails=(f'{name} {surname} {telephone}')
    with open('Contacts.txt', 'a+', encoding='utf-8') as file:
        file.write(f'{" ".join(contactDetails)} \n')
   
def all_contact():
    myfile = open('Contacts.txt', 'r+') 
    filecontents = myfile.read() 
    print(filecontents)

def import_contact():
    firstfile = open('Contacts.txt', 'r', encoding='utf-8')
    onefile = firstfile.read()
    secondfile = open('Contacts_v1.txt', 'r', encoding='utf-8')
    twofile = secondfile.read()
    onefile = onefile + twofile
    with open('Importfile.txt', 'a+', encoding='utf-8') as ifile:
        ifile.write(f'{" ".join(onefile)} \n')


        
