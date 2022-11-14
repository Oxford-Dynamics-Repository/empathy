# Johann Diep (johann@oxdynamics.com) - Oxford Dynamics - November 2022
#
# This script generates the knowledge (comma-separated sentences) for the military combat situation.
#
# 5 examples in random order:
# - 4 terrorists, AK47, Eddy Street
# - 10 civilians, Ellis Street
# - 2 tanks, Laguna Street
# - 3 drones, Turk Street
# - 4 cows, Geary Boulevard

from random import *


def generate_knowledge():
    output = []

    dangers = ["enemies", "terrorists", "men", "women"]
    people = ["civilians", "men", "women"]
    weapons = ["assault rifles", "explosives", "guns", "knives"]
    streets = ["Eddy Street", "Ellis Street", "Laguna Street", "Turk Street", "Geary Boulevard", "Pine Street", "Sutter Street", "Clay Street"]
    mobiles = ["tanks", "tactical vehicles"]
    aircrafts = ["drones", "helicopters", "combat aircrafts"]
    animals = ["cows", "horses", "dogs", "cats", "pigs"]

    # Enemies
    danger_id = randint(0,len(dangers)-1)
    weapon_id = randint(0,len(weapons)-1)
    street_id = randint(0,len(streets)-1)

    sentence = f'{randint(2,10)} {dangers[danger_id]}, {weapons[weapon_id]}, {streets[street_id]}'
    output.append(sentence)

    # Civilians
    person_id = randint(0,len(people)-1)
    street_id = randint(0,len(streets)-1)

    sentence = f'{randint(2,10)} {people[person_id]}, {streets[street_id]}'
    output.append(sentence)

    # Mobiles
    mobile_id = randint(0,len(mobiles)-1)
    street_id = randint(0,len(streets)-1)

    sentence = f'{randint(2,10)} {mobiles[mobile_id]}, {streets[street_id]}'
    output.append(sentence)

    # Aircrafts
    aircraft_id = randint(0,len(aircrafts)-1)
    street_id = randint(0,len(streets)-1)

    sentence = f'{randint(2,10)} {aircrafts[aircraft_id]}, {streets[street_id]}'
    output.append(sentence)

    # Animals
    animal_id = randint(0,len(animals)-1)
    street_id = randint(0,len(streets)-1)

    sentence = f'{randint(2,10)} {animals[animal_id]}, {streets[street_id]}'
    output.append(sentence)

    return ' - '.join(output)

def main():
    sentences = generate_knowledge()    
    print(sentences)
    

if __name__ == '__main__':
    main()