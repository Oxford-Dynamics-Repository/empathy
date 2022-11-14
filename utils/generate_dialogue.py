# Johann Diep (johann@oxdynamics.com) - Oxford Dynamics - November 2022
#
# This script generates a grounded dialogue dataset for the military combat situation with the 
# knowledge from the generate_knowledge.py script. 

import copy
import jsonlines
from generate_knowledge import generate_knowledge
from random import *


def generate_dialogues(number_dialogues):
    examples = []
    context = ['Are there any immediate threats near me?', 'Are there any danger nearby?', 'Is there something dangerous nearby?']
    
    for i in range(0, number_dialogues):
        rand_context = randint(0, len(context)-1)
        
        knowledge_dictionary = generate_knowledge()
        
        number_enemies = knowledge_dictionary['number_enemies']
        type_enemy = knowledge_dictionary['type_enemy']
        type_weapon = knowledge_dictionary['type_weapon']
        enemy_street_name = knowledge_dictionary['enemy_street_name']
        number_civilians = knowledge_dictionary['number_civilians']
        type_civilian = knowledge_dictionary['type_civilian']
        civilian_street_name = knowledge_dictionary['civilian_street_name']
        number_mobiles = knowledge_dictionary['number_mobiles']
        type_mobile = knowledge_dictionary['type_mobile']
        mobile_street_name = knowledge_dictionary['mobile_street_name']
        number_aircrafts = knowledge_dictionary['number_aircrafts']
        type_aircraft = knowledge_dictionary['type_aircraft']
        aircraft_street_name = knowledge_dictionary['aircraft_street_name']
        number_animals = knowledge_dictionary['number_animals']
        type_animal = knowledge_dictionary['type_animal']
        animal_street_name = knowledge_dictionary['animal_street_name']

        knowledge = [number_enemies + ', ' + type_enemy + ', ' + type_weapon + ', ' + enemy_street_name, 
            number_civilians + ', ' + type_civilian + ', ' + civilian_street_name, 
            number_mobiles + ', ' + type_mobile + ', ' + mobile_street_name,
            number_aircrafts + ', ' + type_aircraft + ', ' + aircraft_street_name, 
            number_animals + ', ' + type_animal + ', ' + animal_street_name]

        knowledge = ' - '.join(knowledge)
 
        if number_enemies == '0':
            response = ['No, environment is safe.', 'It is safe around here.', 'No, there is no danger nearby.']
        else:
            response = [f'Yes, there are {number_enemies} {type_enemy}, {number_mobiles} {type_mobile} and {number_aircrafts} {type_aircraft} nearby.',
                f'{number_enemies} {type_enemy}, {number_mobiles} {type_mobile} and {number_aircrafts} {type_aircraft} are detected.']

        rand_response = randint(0, len(response)-1)

        example = {}
        example['Context'] = context[rand_context]
        example['Knowledge'] = knowledge
        example['Response'] = response[rand_response]
        examples.append(copy.deepcopy(example))        
            
    save_to_file(examples)

def save_to_file(examples):
    with jsonlines.open(f'military_dialogues.jsonl', mode='w') as writer:
        for i in examples:
            writer.write(i)

def main():
    generate_dialogues(5)    
    

if __name__ == '__main__':
    main()