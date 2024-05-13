from collections import UserDict
from datetime import datetime, date, timedelta
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    def __init__(self, name):
        super().__init__(name)
        #  self.name = name
    def __str__(self):
        return str(self.value)
		



class NumberTooShortError(Exception):
    def __init__(self, message="Number is too short"):
        self.message = message
        super().__init__(self.message)

class NumberStartsFromLowError(Exception):
    def __init__(self, message="Number is too long"):
        self.message = message
        super().__init__(self.message)



class Phone(Field):
    # реалізація класу
   def __init__(self, number) : 
     super().__init__(number) 
     if len(number) < 10:
        raise NumberTooShortError
     elif len(number) > 10:
        raise NumberStartsFromLowError
     else:
        self.number = number
   def __str__(self):
        return str(self.value)
		
class Birthday(Field):
    def __init__(self, birthday):
        super().__init__(birthday)
        try:
            self.birthday=datetime.strptime(birthday,"%d.%m.%Y")
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
    def __str__(self):
        return str(self.value)    

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
    # реалізація класу
    def add_phone(self,number: str):
        self.phones.append(Phone(number))

    def remove_phone(self,phone_number:str):
       
         self.phone = [phone for phone in self.phones if self.phone != phone_number]
             


    def edit_phone(self, number:str,new_number:str): 
       for phone in self.phones:
           if phone.value == number:
               self.phones.remove(phone)
               break
       new_phone = Phone(new_number)
       self.phones.append(new_phone)
       

    def find_phone(self,number):
        for phone in self.phones:
           if phone.value == number:
               return phone 


    def add_birthday(self,birthday:str):
        self.birthday=Birthday(birthday)




    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"

class AddressBook(UserDict):
     def __init__(self):
        self.data = dict()

     def add_record(self,record):
       self.data[record.name.value] = record

     def find(self,name):
       record = self.data.get(name)
       return record
       
     def delete(self,name):
       del self.data[name]
  

     def get_upcoming_birthdays(self):
        birthdays = dict()
        for name, user in self.data.items():
         birthday=datetime.strptime(user.birthday.value, "%d.%m.%Y").date()
         today = datetime.today().date()
         birthday_this_year=birthday.replace(year=today.year)
         birthdays.update({name:birthday})
        if birthday_this_year<today:
         birthdays[name]=birthday_this_year+timedelta(days=365)
        elif birthday.weekday()==5:
         birthdays[name]=birthday_this_year+timedelta(days=2)
        elif birthday.weekday()==6:
         birthdays[name]=birthday_this_year+timedelta(days=1)
        else:
         birthdays[name]=birthday_this_year
    
        return birthdays
     



book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_birthday("22.06.2018")
book.add_record(john_record)

john = book.find("John")
print(john)
birth = book.get_upcoming_birthdays()
print(birth)
jack_rec= Record("Jack")
jack_rec.add_phone("2222666600")
jack_rec.add_birthday("13.02.2002")
book.add_record(jack_rec)
birth = book.get_upcoming_birthdays()
print(birth)

for name, record in book.data.items():
    print(record)

birth = book.get_upcoming_birthdays()
print(birth)
