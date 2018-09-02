class Person:
    def __init__(self, first_name, last_name, dob, address, city, postcode, country):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.address = address
        self.city = city
        self.postcode = postcode
        self.country = country


person1 = Person("Barry", "Cassidy", "30/09/2000", "5 Leven Street", "Glasgow", "G41 2JS", "United Kingdom")

print(person1.first_name + " " + person1.last_name)
print(person1.dob)
print(person1.address)
print(person1.city)
print(person1.postcode)
print(person1.country)
