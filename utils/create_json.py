# Johann Diep (johann@oxdynamics.com) - Oxford Dynamics - November 2022
#
# This file creates a dialogue dataset in json-format. 

import json
from generate_knowledge import generate_knowledge


def generate_data(number_of_data):
    dictionary = {}
    dictionary["train"] = []
    dictionary["valid"] = []

    for i in range(number_of_data):
        k = generate_knowledge()

        while k['number_enemies'] == 'none':
            k = generate_knowledge()

        k_1 = f"There are {k['number_enemies']} {k['type_enemy']} with {k['type_weapon']} at {k['enemy_street_name']}."
        k_2 = f"There are {k['number_civilians']} {k['type_civilian']} at {k['civilian_street_name']}."
        k_3 = f"There are {k['number_mobiles']} {k['type_mobile']} at {k['mobile_street_name']}."
        k_4 = f"There are {k['number_aircrafts']} {k['type_aircraft']} at {k['aircraft_street_name']}."
        k_5 = f"There are {k['number_animals']} {k['type_animal']} at {k['animal_street_name']}."

        p_1 = f"{k['enemy_street_name']}"
        p_2 = f"{k['civilian_street_name']}"
        p_3 = f"{k['mobile_street_name']}"
        p_4 = f"{k['aircraft_street_name']}"
        p_5 = f"{k['animal_street_name']}"

        dictionary["train"].append({"personality": [k_1, k_2, k_3, k_4, k_5], "utterances": {"candidates": [p_1, p_2, p_3, p_4, p_5], "history": [f"Are there any {k['type_enemy']}?"]}})

        k = generate_knowledge()

        while k['number_enemies'] == '0':
            k = generate_knowledge()

        k_1 = f"There are {k['number_enemies']} {k['type_enemy']} with {k['type_weapon']} at {k['enemy_street_name']}."
        k_2 = f"There are {k['number_civilians']} {k['type_civilian']} at {k['civilian_street_name']}."
        k_3 = f"There are {k['number_mobiles']} {k['type_mobile']} at {k['mobile_street_name']}."
        k_4 = f"There are {k['number_aircrafts']} {k['type_aircraft']} at {k['aircraft_street_name']}."
        k_5 = f"There are {k['number_animals']} {k['type_animal']} at {k['animal_street_name']}."

        p_1 = f"{k['enemy_street_name']}"
        p_2 = f"{k['civilian_street_name']}"
        p_3 = f"{k['mobile_street_name']}"
        p_4 = f"{k['aircraft_street_name']}"
        p_5 = f"{k['animal_street_name']}"

        dictionary["valid"].append({"personality": [k_1, k_2, k_3, k_4, k_5], "utterances": {"candidates": [p_1, p_2, p_3, p_4, p_5], "history": [f"Are there any {k['type_enemy']}?"]}})
 
    return dictionary

def save(dictionary):
    with open("military_dialogues.json", "w") as outfile:
        json.dump(dictionary, outfile)

def main():
    dictionary = generate_data(1000)
    save(dictionary)


if __name__ == '__main__':
    main()