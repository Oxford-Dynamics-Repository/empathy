# Johann Diep (johann@oxdynamics.com) - Oxford Dynamics - November 2022
#
# This script generates the knowledge (comma-separated sentences) for the military combat situation.
#
# 5 examples in random order:
# - "4 terrorists, AK47, Eddy Street"
# - "10 civilians, Ellis Street"
# - "2 tanks, Laguna Street"
# - "3 drones, Turk Street"
# - "4 cows, Geary Boulevard"

from random import *


def generate_knowledge():
    output = {}
    rand_number = randint(0,9)

    dangers = ["enemies", "terrorists", "assassins", "gunmen"]
    people = ["civilians", "men", "women", "citizens", "children"]
    weapons = ["assault rifles", "submachine guns", "pump shotguns", "revolvers", 'explosives', 'bombs', 'knives', 'AK47s']
    streets = ["Greasy Grove", "Pleasant Park", "Retail Row", "Anarchy Acres", "Fatal Fields", "Flush Factory", "Loot Lake", "Container Yard"]
    mobiles = ["tanks", "tactical vehicles", "passenger cars", "SUVs", "trucks"]
    aircrafts = ["drones", "helicopters", "combat aircrafts", "UAVs", "quadcopters"]
    animals = ["cows", "horses", "dogs", "cats", "pigs"]
    colors = ["black", "white", "red", "gray", "blue", "green", "yellow"]

    # Building enemy dictionary.
    danger_id = randint(0,len(dangers)-1)
    weapon_id = randint(0,len(weapons)-1)
    street_id = randint(0,len(streets)-1)
    output['number_enemies'] = f'{randint(2,10)}'
    output['type_enemy'] = f'{dangers[danger_id]}'
    output['type_weapon'] = f'{weapons[weapon_id]}'
    output['enemy_street_name'] = f'{streets[street_id]}'
    
    if rand_number == 0: 
        output['number_enemies'] = '0'
        output['type_enemy'] = 'none'
        output['type_weapon'] = 'none'
        output['enemy_street_name'] = 'none'

    # Building civilian dictionary.
    person_id = randint(0,len(people)-1)
    street_id = randint(0,len(streets)-1)
    output['number_civilians'] = f'{randint(2,10)}'
    output['type_civilian'] = f'{people[person_id]}'
    output['civilian_street_name'] = f'{streets[street_id]}'

    # Building mobile dictionary.
    mobile_id = randint(0,len(mobiles)-1)
    street_id = randint(0,len(streets)-1)
    color_id = randint(0,len(colors)-1)
    other_id = randint(0,len(colors)-1)
    output['number_mobiles'] = f'{randint(2,10)}'
    output['type_mobile'] = f'{mobiles[mobile_id]}'
    output['mobile_street_name'] = f'{streets[street_id]}'
    output['mobile_color'] = f'{colors[color_id]}'
    
    while(color_id == other_id):
        other_id = randint(0,len(colors)-1)
    output['other_color'] = f'{colors[other_id]}'
 
    if rand_number == 0: 
        output['number_mobiles'] = '0'
        output['type_mobile'] = 'none'
        output['mobile_street_name'] = 'none'

    # Building aircraft dictionary.
    aircraft_id = randint(0,len(aircrafts)-1)
    street_id = randint(0,len(streets)-1)
    output['number_aircrafts'] = f'{randint(2,10)}'
    output['type_aircraft'] = f'{aircrafts[aircraft_id]}'
    output['aircraft_street_name'] = f'{streets[street_id]}' 

    if rand_number == 0: 
        output['number_aircrafts'] = '0'
        output['type_aircraft'] = 'none'
        output['aircraft_street_name'] = 'none'

    # Building animal dictionary.
    animal_id = randint(0,len(animals)-1)
    street_id = randint(0,len(streets)-1)
    sentence = f'{randint(2,10)} {animals[animal_id]} {streets[street_id]}'
    output['number_animals'] = f'{randint(2,10)}'
    output['type_animal'] = f'{animals[animal_id]}'
    output['animal_street_name'] = f'{streets[street_id]}' 

    return output

def main():
    sentences = generate_knowledge()    
    print(sentences)
    

if __name__ == '__main__':
    main()