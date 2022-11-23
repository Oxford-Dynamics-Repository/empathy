# Johann Diep (johann@oxdynamics.com) - Oxford Dynamics - November 2022
#
# This script generates a grounded dialogue dataset for the military combat situation with the 
# knowledge from the generate_knowledge.py script. 
#
# Example: 
# - Context:       "Are there any danger nearby? 
#                  "9 assassins, 6 suspicious cars and 5 drones are detected."
#                  "What weapons are the assassins carrying?"
#                  "They are armed with assault rifles."
#                  "What is their location?"
# - Knowledge:     "5 drones at Pleasant Park. 2 citizens at Fatal Fields. 9 assassins with assault rifles at Pleasant Park. 6 suspicious passenger cars at Flush Factory. 2 cats at Fatal Fields."
# - Response:      "They are at Pleasant Park."

import copy
import jsonlines
from generate_knowledge import generate_knowledge
from random import *
from random import shuffle


# Following up the conversation (asking for weapons).
def ask_weapons(example, knowledge, type_enemy, type_weapon):
    examples = []

    context = [f'What weapons are the {type_enemy} carrying?', f'Are the {type_enemy} armed?',
        f'Anything I should know about the equipments of the {type_enemy}?', f'Can you tell me anything about the weapons of the {type_enemy}?']
    rand_context = randint(0, len(context)-1)

    prev_response = example['Response']
    response = [f'They are armed with {type_weapon}.', f'They are equipped with {type_weapon}.', 
        f'They are carrying {type_weapon}.', f'I detected {type_weapon}.', f'CCTV footages showcased that they are carrying {type_weapon}.']
    rand_response = randint(0, len(response)-1)

    example['Context'] = example['Context'] + ' ' + prev_response + ' ' + context[rand_context]
    example['Knowledge'] = knowledge
    example['Response'] = response[rand_response]
    examples.append(copy.deepcopy(example))

    save_to_file(examples)
    return example
    
# Following up the conversation (asking about their locations).
def ask_location(example, knowledge, type_enemy, enemy_street_name):
    examples = []

    context = [f'Where are the {type_enemy}?', f'What is the location of the {type_enemy}?', f'Can you tell me anything about the position of the {type_enemy}?',
        f'Where are the {type_enemy} at?', f'Give me the position of the {type_enemy}!', f'What about the location of the {type_enemy}?']
    rand_context = randint(0, len(context)-1)

    prev_response = example['Response']
    response = [f'They are at {enemy_street_name}.', f'They are located at {enemy_street_name}.', 
        f'The {type_enemy} are at {enemy_street_name}.', f'CCTV footages detected them at {enemy_street_name}.',
        f'It looks like they are at {enemy_street_name}.']
    rand_response = randint(0, len(response)-1)

    example['Context'] = example['Context'] + ' ' + prev_response + ' ' + context[rand_context]
    example['Knowledge'] = knowledge
    example['Response'] = response[rand_response]
    examples.append(copy.deepcopy(example))

    save_to_file(examples)
    return example

# Following up the conversation (asking about cars).
def ask_cars(example, knowledge, mobile_color, other_color, type_mobile, mobile_street_name, number_mobiles):
    examples = []
    random_variable = randint(0,1)

    # Asking for the correct car color.
    if random_variable == 0:
        context = [f'Can you detect any {mobile_color} {type_mobile}?', f'Any {mobile_color} {type_mobile}?',
            f'Can you see any {mobile_color} {type_mobile}?', f'Are the {type_mobile} of color {mobile_color}?',
            f'Is the {type_mobile} in {mobile_street_name} {mobile_color}?']
        rand_context = randint(0, len(context)-1)

        prev_response = example['Response']
        response = [f'Yes, the {type_mobile} in {mobile_street_name} are {mobile_color}.', 
            f'I detected {number_mobiles} {mobile_color} {type_mobile} in {mobile_street_name}.', 
            f'The {type_mobile} in {mobile_street_name} are {mobile_color}.']
        rand_response = randint(0, len(response)-1)

        example['Context'] = example['Context'] + ' ' + prev_response + ' ' + context[rand_context]
        example['Knowledge'] = knowledge
        example['Response'] = response[rand_response]
        examples.append(copy.deepcopy(example))

        save_to_file(examples)
        return example

    # Asking for the wrong car color.
    else:
        context = [f'Can you detect any {other_color} {type_mobile}?', f'Any {other_color} {type_mobile}?',
            f'Can you see any {other_color} {type_mobile}?', f'Are the {type_mobile} of color {other_color}?',
            f'Is the {type_mobile} in {mobile_street_name} {other_color}?']
        rand_context = randint(0, len(context)-1)

        prev_response = example['Response']
        response = [f'No, the {type_mobile} in {mobile_street_name} are {mobile_color}.', 
            f'No, but I detected {number_mobiles} {mobile_color} {type_mobile} in {mobile_street_name}.', 
            f'No, the {type_mobile} in {mobile_street_name} are {mobile_color}.',
            f'No, I can not detect any {other_color} {type_mobile}.', f'No {other_color} {type_mobile} detected.']
        rand_response = randint(0, len(response)-1)

        example['Context'] = example['Context'] + ' ' + prev_response + ' ' + context[rand_context]
        example['Knowledge'] = knowledge
        example['Response'] = response[rand_response]
        examples.append(copy.deepcopy(example))                     

        save_to_file(examples)
        return example

# Following up the conversation (emotional conversation).
def ask_support(example, knowledge):
    examples = []

    context = ['I am scared.', 'I am worried.', 'I am kinda scared.', 'I do not know if I will survive.', 'I do not know what to do.']
    rand_context = randint(0, len(context)-1)

    prev_response = example['Response']
    response = ['Stick to the plan.', 'You were trained for this.', 'Think about your training.', 'Stay alerted.', 
        'Understand, be careful.', 'Stay calm.', 'Breath air.', 'Take a deep breath.', 'Focus.', 'Stay focused.']
    rand_response = randint(0, len(response)-1)

    example['Context'] = example['Context'] + ' ' + prev_response + ' ' + context[rand_context]
    example['Knowledge'] = knowledge
    example['Response'] = response[rand_response]
    examples.append(copy.deepcopy(example))

    save_to_file(examples)
    return example

# Following up the conversation (civilians).
def ask_civilians(example, knowledge, type_civilian, civilian_street_name, type_enemy, enemy_street_name):
    examples = []

    context = [f'Are the {type_civilian} safe?', f'Are the {type_civilian} close to the {type_enemy}?', f'Are the {type_civilian} in danger?',
        f'Are the {type_enemy} close to the {type_civilian}?', f'Are the {type_enemy} and {type_civilian} in the same location?']
    rand_context = randint(0, len(context)-1)

    prev_response = example['Response']
    # If the civilians and the enemies are sharing the same location.
    if civilian_street_name == enemy_street_name:
        response = [f'No, the {type_civilian} and {type_enemy} are both in {civilian_street_name}.', f'No, the {type_civilian} and {type_enemy} are both in the same location.',
            'No, both are in the same location.', f'The {type_enemy} and {type_civilian} are in the same location.']
        rand_response = randint(0, len(response)-1)

        example['Context'] = example['Context'] + ' ' + prev_response + ' ' + context[rand_context]
        example['Knowledge'] = knowledge
        example['Response'] = response[rand_response]
        examples.append(copy.deepcopy(example))

        save_to_file(examples)
        return example

    # If the civilians and the enemies are in different locations.
    else:
        response = [f'Yes, the {type_civilian} and {type_enemy} are in different locations.', f'The {type_enemy} and {type_civilian} are in different location.',
            'Both are in different locations.', f'Yes the {type_civilian} are safe since they are in a different location than the {type_enemy}.']
        rand_response = randint(0, len(response)-1)

        example['Context'] = example['Context'] + ' ' + prev_response + ' ' + context[rand_context]
        example['Knowledge'] = knowledge
        example['Response'] = response[rand_response]
        examples.append(copy.deepcopy(example))

        save_to_file(examples)
        return example     

def generate_dialogues(number_dialogues):
    examples = []
    
    for i in range(0, number_dialogues):
        # Setting up the conversation start (asking about environment). 
        context = ['Are there any immediate threats near me?', 'Are there any danger nearby?', 'Is there something dangerous nearby?', 
                   'Is it safe here?', 'Is it dangerous around here?', 'What is around here?', 'Something around here I should be aware of?',
                   'Something I should be alerted by?']
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
        mobile_color = knowledge_dictionary['mobile_color']
        other_color = knowledge_dictionary['other_color']
        number_aircrafts = knowledge_dictionary['number_aircrafts']
        type_aircraft = knowledge_dictionary['type_aircraft']
        aircraft_street_name = knowledge_dictionary['aircraft_street_name']
        number_animals = knowledge_dictionary['number_animals']
        type_animal = knowledge_dictionary['type_animal']
        animal_street_name = knowledge_dictionary['animal_street_name']

        knowledge = [number_enemies + ' ' + type_enemy + ' with ' + type_weapon + ' at ' + enemy_street_name + '.', 
            number_civilians + ' ' + type_civilian + ' at ' + civilian_street_name + '.', 
            number_mobiles + ' ' + mobile_color + ' ' + type_mobile + ' at ' + mobile_street_name + '.',
            number_aircrafts + ' ' + type_aircraft + ' at ' + aircraft_street_name + '.', 
            number_animals + ' ' + type_animal + ' at ' + animal_street_name + '.']

        if number_enemies == '0':
            knowledge = [number_civilians + ' ' + type_civilian + ' at ' + civilian_street_name + '.',
                number_animals + ' ' + type_animal + ' at ' + animal_street_name + '.']

        shuffle(knowledge)
        knowledge = ' '.join(knowledge)

        if number_enemies == '0':
            response = ['No, environment is safe.', 'It is safe around here.', 'No, there is no danger nearby.', 'There is nothing around here.'
                        'Nothing to worry about.', 'Safe around here.', 'Environment is secure.', 'All safe.', 'All safe but stay alerted.', 
                        f'I only detected couple of {type_civilian} and {type_animal}.', f'{number_civilians} {type_civilian} and {number_animals} {type_animal} detected, you should be safe.',
                        f'{number_animals} {type_animal} and {number_civilians} {type_civilian} detected, nothing to worry about.']
        else:
            response = [f'Yes, there are {number_enemies} {type_enemy}, {number_mobiles} {type_mobile} and {number_aircrafts} {type_aircraft} nearby.',
                f'{number_aircrafts} {type_aircraft}, {number_mobiles} {type_mobile} and {number_enemies} {type_enemy} are detected.',
                f'I detected {number_mobiles} {mobile_color} {type_mobile}, {number_enemies} {type_enemy} and {number_aircrafts} {type_aircraft}.']

        rand_response = randint(0, len(response)-1)

        example = {}
        example['Context'] = context[rand_context]
        example['Knowledge'] = knowledge
        example['Response'] = response[rand_response]
        examples.append(copy.deepcopy(example))
            
        save_to_file(examples)
        examples = []

        questions = [0, 1, 2, 3, 4]
        shuffle(questions)
        if number_enemies != '0':
            for question_index in range(len(questions)):
                if questions[question_index] == 0:
                    example = ask_weapons(example, knowledge, type_enemy, type_weapon)
                if questions[question_index] == 1:
                    example = ask_location(example, knowledge, type_enemy, enemy_street_name)
                if questions[question_index] == 2:
                    example = ask_cars(example, knowledge, mobile_color, other_color, type_mobile, mobile_street_name, number_mobiles)
                if questions[question_index] == 3:
                    example = ask_support(example, knowledge)
                if questions[question_index] == 4:
                    ask_civilians(example, knowledge, type_civilian, civilian_street_name, type_enemy, enemy_street_name)

def save_to_file(examples):
    with jsonlines.open(f'military_dialogues.jsonl', mode='a') as writer:
        for i in examples:
            writer.write(i)

def main():
    number_of_samples = 10000 # Define the number of samples.
    generate_dialogues(number_of_samples)    
    

if __name__ == '__main__':
    main()