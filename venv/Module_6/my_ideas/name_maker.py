from faker import Faker

fake = Faker()


def how_many_names(times_wanted):
    set_of_names = set()
    while len(set_of_names) < times_wanted:
        name = fake.name()
        set_of_names.add(name)

    names_string = ", ".join(set_of_names)
    print(names_string)
    print(len(set_of_names))


how_many_names(5000)
