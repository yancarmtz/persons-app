from exceptions.user import UserNotFound

class PersonDAO(object):
    def __init__(self):
        self.persons = []

    def get(self, email):
        for person in self.persons:
            if person['email'] == email:
                return person
        raise UserNotFound("Not Key found","User not found in Dictionary")

    def create(self, person):
        self.persons.append(person)
        return person

    def update(self, person):
        _person = self.get(person['email'])
        _person.update(person)
        return _person

    def delete(self, email):
        _person = self.get(email)
        self.persons.remove(_person)

