from faker import Faker
fake = Faker()

class BaseContact:
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
    def __repr__(self):
        return f'{self.name} {self.surname} - BaseContact'  
    def contact(self):
        return f'Wybieram numer {self.phone} i dzwonię do {self.name} {self.surname}'
    @property
    def label_length(self):
        return len(f'{self.name}{self.surname}')
    
class BusinessContact(BaseContact):
    def __init__(self, position, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.business_phone = business_phone
        self.company = company
        self.position = position
    def __repr__(self):
        return f'{self.name} {self.surname} - BusinessContact'  
    def contact(self):
        return f'Wybieram numer {self.business_phone} i dzwonię do {self.name} {self.surname}'
    # no need to define label_length again, parent already has it

BaseContacts = []
BusinessContacts = []

def create_contacts(type, how_many):
    if type == 1:
        for i in range(how_many):
            first = fake.first_name()
            last = fake.last_name()
            #Changed emails' structure so that name and surname corespond with the email address
            BaseContacts.append(BaseContact(first, last, fake.phone_number(), first[0]+"."+last+'@'+fake.email().split("@")[-1])) 
    
    else:
        for i in range(how_many):
            first = fake.first_name()
            last = fake.last_name()
            #Changed emails' structure so that name and surname corespond with the email address
            BusinessContacts.append(BusinessContact(fake.job(), fake.company(), fake.phone_number(), first, last, fake.phone_number(), first[0]+"."+last+'@'+fake.email().split("@")[-1])) 



'''
Dodatkowo, nie sprawdzać

Sprawdzenie:

create_contacts(2, 5)
def print_Business_cards():
    for person in BusinessContacts:
        print(person.name, person.surname, "-", person.position, "in", person.company, "; phone no.", person.business_phone, "; email:", person.email)

print(print_Business_cards())

Program:

if __name__ == "__main__":
    type = int(input('Podaj rodzaj wizytówki do zaktualizowania: 1 Prywatna, 2 Służbowa: '))
    how_many = int(input('Podaj liczbę osób do wykreowania: '))

    if all((type > 0, type < 3, how_many > 0)):
        create_contacts(type, how_many)
    elif how_many > 51:
        print("Maksymalnie 50 osób !")
        exit(1)
    else:
        print("Niepoprawnie podane parametry, spróbuj jeszcze raz!")
        exit(1)
'''
