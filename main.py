from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


class Record:
    name = ""
    phones = []

    def __init__(self, name, phone=None):
        self.name = name
        self.phones = [phone] if phone else []

    def add(self, phone):
        self.phones.append(phone)

    def delete(self, phone):
        self.phones.remove(phone)

    def edit(self, phone):
        self.phones.clear()
        self.phones = phone


class Field:
    pass


class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone):
        self.value = phone


if __name__ == "__main__":
    name = Name("Bill")
    phone = Phone("1234567890")
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab["Bill"], Record)
    assert isinstance(ab["Bill"].name, Name)
    assert isinstance(ab["Bill"].phones, list)
    assert isinstance(ab["Bill"].phones[0], Phone)
    assert ab["Bill"].phones[0].value == "1234567890"
    print("All Ok)")
