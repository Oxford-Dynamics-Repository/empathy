# Johann Diep (johann@oxdynamics.com) - Oxford Dynamics - November 2022
#
# This script generates a grounded dialogue dataset for the military combat situation.
# This document is legacy, please refer the generate_dialogue.py.

import copy
import jsonlines


def generate_dialogues():
    distances = ["1 mile", "2 miles", "3 miles", "4 miles"]
    dangers = ["enemy", "people", "men", "women", "terrorists"]
    appearances = ["2", "4", "6", "8"]
    helps = ["Can I help you with anything else?", "Do you need more information on that?", "Do you have more questions?"]

    examples = []

    for distance, appearance in zip(distances, appearances):
        knowledge_1 = f'{appearance} people, {distance} away'

        for danger in dangers:
            for help in helps:
                context_1 = [f'How many {danger} are within {distance} radius?', f'Are there any {danger} {distance} away from me?']
                response_1 = [f'{appearance} {danger} are {distance} away. {help}', f'There are {appearance} {danger} around. {help}']

                for i in range(len(context_1)):
                    for j in range(len(response_1)):
                        example = {}
                        example['Context'] = context_1[i]
                        example['Knowledge'] = knowledge_1
                        example['Response'] = response_1[j]
                        examples.append(copy.deepcopy(example))

    for distance, appearance in zip(distances, appearances):
        knowledge_1 = f'{appearance} people, {distance} away'

        if distance == "1 mile":
            continue

        for danger in dangers:        
            for help in helps:
                context_1 = [f'How many {danger} are within 1 mile radius?', f'Are there any {danger} 1 mile away from me?']
                response_1 = [f'{appearance} {danger} are {distance} away but no one within 1 mile. {help}', f'There are {appearance} {danger} around that are {distance} away but none of them is within 1 mile. {help}']

                for i in range(len(context_1)):
                    for j in range(len(response_1)):
                        example = {}
                        example['Context'] = context_1[i]
                        example['Knowledge'] = knowledge_1
                        example['Response'] = response_1[j]
                        examples.append(copy.deepcopy(example))                       

    save_to_file(examples)

def save_to_file(examples):
    with jsonlines.open(f'military_grounded_dialogues.jsonl', mode='w') as writer:
        for i in examples:
            writer.write(i)

def main():
    generate_dialogues()


if __name__ == '__main__':
    main()