import random
from collections import Counter


def winner(list_of_people):
    counter = 0
    list_of_x_times_person_appears = []
    while counter < 100:
        final = random.choice(list_of_people)
        list_of_x_times_person_appears.append(final)
        counter += 1

    real_winner = Counter(list_of_x_times_person_appears)
    winner_name, winner_apeared = real_winner.most_common(1)[0]
    print(f'The Winner was {winner_name}, being choose {winner_apeared} times by the system, congratulations')


people = str(input('Type the names, separeted by a comma: '))

name_list = [nome.strip() for nome in people.split(",")]


winner(name_list)
