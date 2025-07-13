from collections import UserDict

class Field:
    
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    
    def __init__(self, value):
        if not value or not value.strip():
            raise ValueError("Ім'я не може бути порожнім")
        super().__init__(value.strip())

class Phone(Field):
    
    def __init__(self, value):
        if not self.validate_phone(value):
            raise ValueError("Номер телефону має містити рівно 10 цифр")
        super().__init__(value)
    
    @staticmethod
    def validate_phone(phone):
        
        return phone.isdigit() and len(phone) == 10

class Record:
    
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        
        phone_obj = Phone(phone)
        if phone_obj.value not in [p.value for p in self.phones]:
            self.phones.append(phone_obj)
        else:
            raise ValueError("Такий номер телефону вже існує")

    def remove_phone(self, phone):
        
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                self.phones.remove(phone_obj)
                return
        raise ValueError("Номер телефону не знайдено")

    def edit_phone(self, old_phone, new_phone):
        
        if not Phone.validate_phone(new_phone):
            raise ValueError("Новий номер телефону має містити рівно 10 цифр")
        
        
        if new_phone in [p.value for p in self.phones]:
            raise ValueError("Такий номер телефону вже існує")
        
        
        for phone_obj in self.phones:
            if phone_obj.value == old_phone:
                phone_obj.value = new_phone
                return
        raise ValueError("Старий номер телефону не знайдено")

    def find_phone(self, phone):
        
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                return phone_obj.value
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    
    
    def add_record(self, record):
        
        if not isinstance(record, Record):
            raise TypeError("Запис має бути екземпляром класу Record")
        self.data[record.name.value] = record

    def find(self, name):
        
        return self.data.get(name)

    def delete(self, name):
        
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError(f"Контакт з ім'ям '{name}' не знайдено")

    def __str__(self):
        if not self.data:
            return "Адресна книга порожня"
        return "\n".join(str(record) for record in self.data.values())

