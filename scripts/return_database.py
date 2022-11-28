# Lucy Jackson (Lucy@oxdynamics.com) - Oxford Dynamics - Lucy Jackson
#
# This script generates a random database for TAPAS.

import pandas as pd
import random

def return_database():
    dangers = ["5 enemies", "3 terrorists", "2 opposition soldiers"]
    people = ["civilians", "men", "women", "citizens", "children"]
    weapons = ["assault rifles", "submachine guns", "pump shotguns", "revolvers", 'explosives', 'bombs', 'knives', 'AK47s']
    streets = ["Adams Court", "Bride Lane", "Birchin Lane", "Gough Lane", "Dawlish Road", "Lee Street", "Groveland Court", "Container Yard"]
    mobiles = ["tactical vehicles", "passenger cars", "SUVs", "trucks"]
    aircrafts = ["drones", "helicopters", "combat aircrafts", "UAVs", "quadcopters"]
    colors = ["black", "white", "red", "gray", "blue", "green", "yellow"]
    distance = ["2 minutes", "10 minutes", "1 hour", "3 minutes", "half an hour", "1 minute"]
    clothing = ["green jumpers", "blue trousers", "red coat", "brown jacket"]
    danger_ind = random.randint(1,1)
    people_ind = random.randint(1,1)
    vehic_ind = random.randint(1,1)

    threat_info = {'threat':random.sample(dangers, danger_ind), 'distance':random.sample(distance, danger_ind),'armed':random.sample(weapons, danger_ind), 'location': random.sample(streets, danger_ind), 'wearing':random.sample(clothing, danger_ind), 'colour':random.sample(colors, danger_ind)}
    other_info = {'other obstacles':random.sample(people, people_ind), 'location':random.sample(streets, people_ind), 'distance':random.sample(distance, people_ind), 'wearing':random.sample(clothing, people_ind), 'colour':random.sample(colors, people_ind)}
    vehi_info = {'vehical': random.sample(mobiles, vehic_ind), 'location':random.sample(streets, vehic_ind), 'colour': random.sample(colors, vehic_ind), 'distance': random.sample(distance, vehic_ind)}
    threat_info = pd.DataFrame.from_dict(threat_info)
    other_info = pd.DataFrame.from_dict(other_info)
    vehi_info = pd.DataFrame.from_dict(vehi_info)
    table = pd.concat([threat_info, other_info, vehi_info], ignore_index=True)
    table = table.fillna('')
    # table = pd.DataFrame.from_dict(database)
    return table

def main():
    table = return_database()

if __name__ == '__main__':
    main()